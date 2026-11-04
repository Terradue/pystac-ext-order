from datetime import UTC, datetime

import pytest
from jsonschema.exceptions import ValidationError

import pystac
from pystac.extensions.order import SCHEMA_URI, OrderExtension


@pytest.fixture
def item() -> pystac.Item:
    return pystac.Item("example", None, None, datetime(2026, 1, 1, tzinfo=UTC), {})


@pytest.fixture
def collection() -> pystac.Collection:
    return pystac.Collection(
        "orders",
        "Order examples",
        pystac.Extent(
            pystac.SpatialExtent([-180, -90, 180, 90]),
            pystac.TemporalExtent([[datetime(2026, 1, 1, tzinfo=UTC), None]]),
        ),
    )


@pytest.mark.parametrize(
    "unsupported",
    [
        pystac.Catalog("catalog", "Unsupported"),
        pystac.Link("related", "https://example.com"),
        object(),
    ],
)
def test_unsupported_targets_are_rejected(unsupported: object) -> None:
    entry_point = "ext"
    with pytest.raises(pystac.ExtensionTypeError, match="Unsupported extension target"):
        getattr(OrderExtension, entry_point)(unsupported, add_if_missing=True)


@pytest.fixture(params=["item", "collection", "asset", "item_asset"])
def target(
    request: pytest.FixtureRequest, item: pystac.Item, collection: pystac.Collection
) -> pystac.Item | pystac.Collection | pystac.Asset | pystac.ItemAssetDefinition:
    if request.param == "item":
        return item
    if request.param == "collection":
        return collection
    if request.param == "asset":
        asset = pystac.Asset("https://example.com/data.tif")
        item.add_asset("data", asset)
        return asset
    definition = pystac.ItemAssetDefinition({"type": "image/tiff"})
    definition.set_owner(collection)
    collection.item_assets = {"data": definition}
    return collection.item_assets["data"]


def test_registration_required_and_added_once(
    target: pystac.Item | pystac.Collection | pystac.Asset | pystac.ItemAssetDefinition,
    item: pystac.Item,
    collection: pystac.Collection,
) -> None:
    with pytest.raises(pystac.ExtensionNotImplemented):
        OrderExtension.ext(target)
    assert OrderExtension.ext(target, add_if_missing=True).obj is target
    OrderExtension.ext(target, add_if_missing=True)
    assert item.stac_extensions + collection.stac_extensions == [SCHEMA_URI]
    assert OrderExtension.has_extension(item) or OrderExtension.has_extension(collection)
    assert OrderExtension.get_schema_uri() == SCHEMA_URI


def test_registration_requires_exact_version(item: pystac.Item) -> None:
    previous_uri = "https://stac-extensions.github.io/order/v1.0.0/schema.json"
    item.stac_extensions = [previous_uri]
    assert not OrderExtension.has_extension(item)
    with pytest.raises(pystac.ExtensionNotImplemented):
        OrderExtension.ext(item)
    OrderExtension.ext(item, add_if_missing=True)
    assert item.stac_extensions == [previous_uri, SCHEMA_URI]


@pytest.mark.parametrize("field", ["status", "id", "date", "expiration_date"])
def test_property_storage_null_and_removal(
    target: pystac.Item | pystac.Collection | pystac.Asset | pystac.ItemAssetDefinition,
    field: str,
) -> None:
    extension = OrderExtension.ext(target, add_if_missing=True)
    properties = (
        target.properties
        if isinstance(target, (pystac.Item, pystac.ItemAssetDefinition))
        else target.extra_fields
    )
    key = f"order:{field}"
    assert getattr(extension, field) is None
    setattr(extension, field, "2026-01-01T00:00:00Z")
    assert properties[key] == "2026-01-01T00:00:00Z"
    assert getattr(extension, field) == properties[key]
    extension.set_null(field)
    assert key in properties and properties[key] is None
    assert getattr(extension, field) is None
    setattr(extension, field, None)
    assert key not in properties
    setattr(extension, field, "value")
    extension.clear(field)
    extension.clear(field)
    assert key not in properties


def test_apply_preserves_omitted_fields_and_rejects_unknown_names(item: pystac.Item) -> None:
    extension = OrderExtension.ext(item, add_if_missing=True)
    extension.apply(status="pending", id="order-1")
    extension.apply()
    extension.apply(status="succeeded")
    assert extension.id == "order-1"
    assert extension.status == "succeeded"
    with pytest.raises(TypeError, match="Unknown extension field"):
        extension.apply(status="failed", unknown="value")
    assert extension.status == "succeeded"
    extension.apply(id=None)
    assert "order:id" not in item.properties


@pytest.mark.parametrize("operation", ["clear", "set_null"])
def test_unknown_fields_are_rejected(item: pystac.Item, operation: str) -> None:
    extension = OrderExtension.ext(item, add_if_missing=True)
    with pytest.raises(KeyError, match="unknown"):
        getattr(extension, operation)("unknown")
    assert item.properties == {}


def test_item_asset_inheritance_and_null_masking(item: pystac.Item) -> None:
    OrderExtension.ext(item, add_if_missing=True).apply(status="pending", id="parent")
    asset = pystac.Asset("https://example.com/data.tif")
    item.add_asset("data", asset)
    extension = OrderExtension.ext(asset)
    assert extension.status == "pending"
    assert extension.id == "parent"
    extension.status = "succeeded"
    assert extension.status == "succeeded"
    assert item.properties["order:status"] == "pending"
    extension.set_null("status")
    assert OrderExtension.ext(asset).status is None
    extension.clear("status")
    assert extension.status == "pending"


def test_collection_asset_does_not_inherit(collection: pystac.Collection) -> None:
    OrderExtension.ext(collection, add_if_missing=True).status = "pending"
    asset = pystac.Asset("https://example.com/data.tif")
    collection.add_asset("data", asset)
    assert OrderExtension.ext(asset).status is None


def test_unowned_asset_can_be_wrapped_but_not_registered_or_validated() -> None:
    asset = pystac.Asset("https://example.com/data.tif")
    extension = OrderExtension.ext(asset)
    assert extension.obj is asset
    with pytest.raises(pystac.STACError):
        OrderExtension.ext(asset, add_if_missing=True)
    with pytest.raises(pystac.STACError, match="requires an owner"):
        extension.validate()


def test_serialization_round_trip(item: pystac.Item) -> None:
    extension = OrderExtension.ext(item, add_if_missing=True)
    extension.apply(
        status="pending",
        id="order-1",
        date="2026-01-01T00:00:00Z",
        expiration_date="2026-02-01T00:00:00Z",
    )
    restored = OrderExtension.ext(pystac.Item.from_dict(item.to_dict()))
    assert (restored.status, restored.id, restored.date, restored.expiration_date) == (
        extension.status,
        extension.id,
        extension.date,
        extension.expiration_date,
    )


def test_validate_accepts_supported_targets(
    target: pystac.Item | pystac.Collection | pystac.Asset | pystac.ItemAssetDefinition,
    item: pystac.Item,
) -> None:
    extension = OrderExtension.ext(target, add_if_missing=True)
    extension.apply(status="pending", id="order-1", date="2026-01-01T00:00:00Z")
    if isinstance(target, pystac.Asset):
        OrderExtension.ext(item).status = "pending"
    extension.validate()


@pytest.mark.parametrize(
    "field,value",
    [
        ("status", None),
        ("status", 1),
        ("id", 1),
        ("date", "not-a-date"),
        ("date", "2026-01-01T01:00:00+01:00"),
        ("expiration_date", "not-a-date"),
    ],
)
def test_validate_rejects_invalid_values(item: pystac.Item, field: str, value: object) -> None:
    extension = OrderExtension.ext(item, add_if_missing=True)
    extension.status = "pending"
    item.properties[f"order:{field}"] = value
    with pytest.raises(ValidationError):
        extension.validate()


def test_validate_requires_status_and_registration(item: pystac.Item) -> None:
    extension = OrderExtension.ext(item, add_if_missing=True)
    with pytest.raises(ValidationError):
        extension.validate()
    extension.status = "pending"
    item.stac_extensions.clear()
    with pytest.raises(ValidationError):
        extension.validate()


def test_asset_validation_checks_entire_owner(item: pystac.Item) -> None:
    OrderExtension.ext(item, add_if_missing=True)
    asset = pystac.Asset("https://example.com/data.tif")
    item.add_asset("data", asset)
    extension = OrderExtension.ext(asset)
    extension.status = "pending"
    with pytest.raises(ValidationError):
        extension.validate()
    OrderExtension.ext(item).status = "pending"
    extension.validate()


def test_summary_registration_and_representation_replacement(collection: pystac.Collection) -> None:
    with pytest.raises(pystac.ExtensionNotImplemented):
        OrderExtension.summaries(collection)
    summaries = OrderExtension.summaries(collection, add_if_missing=True)
    assert OrderExtension.has_extension(collection)
    assert summaries.status is None
    summaries.status = ["pending", "succeeded"]
    assert summaries.status == ["pending", "succeeded"]
    summaries.status = pystac.RangeSummary("pending", "succeeded")
    status_range = summaries.status
    assert isinstance(status_range, pystac.RangeSummary)
    assert status_range.minimum == "pending"
    assert status_range.maximum == "succeeded"
    summaries.status = {"type": "string", "enum": ["pending"]}
    assert summaries.status == {"type": "string", "enum": ["pending"]}
    assert collection.to_dict()["summaries"]["order:status"] == summaries.status
    summaries.status = None
    assert summaries.status is None
    assert "order:status" not in collection.summaries.to_dict()
