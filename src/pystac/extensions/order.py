# Copyright 2026 Terradue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generated PySTAC extension. Edit the source schema and regenerate to update."""

from __future__ import annotations

import json
from typing import Any, Generic, TypeVar, cast

from pystac.extensions.base import (
    ExtensionManagementMixin,
    PropertiesExtension,
    SummariesExtension,
)

import pystac

SCHEMA_URI = "https://stac-extensions.github.io/order/v1.1.0/schema.json"
SCHEMA: dict[str, Any] = json.loads(
    '{"$schema": "http://json-schema.org/draft-07/schema#", "$id": "https://stac-extensions.github.io/order/v1.1.0/schema.json#", "title": "order Extension", "description": "STAC order Extension for STAC Items and STAC Collections.", "oneOf": [{"$comment": "This is the schema for STAC Items. Remove this object if this extension only applies to Collections.", "allOf": [{"type": "object", "required": ["stac_extensions"], "properties": {"stac_extensions": {"type": "array", "contains": {"const": "https://stac-extensions.github.io/order/v1.1.0/schema.json"}}}}, {"type": "object", "required": ["type", "properties", "assets"], "properties": {"type": {"const": "Feature"}, "properties": {"allOf": [{"$comment": "Require fields here for Item Properties.", "required": ["order:status"]}, {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}]}, "assets": {"$comment": "This validates the fields in Item Assets, but does not require them.", "type": "object", "additionalProperties": {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}}}}]}, {"$comment": "This is the schema for STAC Collections.", "type": "object", "allOf": [{"required": ["type"], "properties": {"type": {"const": "Collection"}}}, {"type": "object", "required": ["stac_extensions"], "properties": {"stac_extensions": {"type": "array", "contains": {"const": "https://stac-extensions.github.io/order/v1.1.0/schema.json"}}}}], "anyOf": [{"$comment": "This is the schema for the top-level fields in a Collection. Remove this if this extension does not define top-level fields for Collections.", "allOf": [{"$comment": "Require fields here for Collections (top-level).", "required": ["order:status"]}, {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}]}, {"$comment": "This validates the fields in Collection Assets, but does not require them.", "required": ["assets"], "properties": {"assets": {"type": "object", "not": {"additionalProperties": {"not": {"allOf": [{"$comment": "Please list all fields here so that we can force the existence of one of them in other parts of the schemas.", "anyOf": [{"required": ["order:status"]}]}, {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}]}}}}}}, {"$comment": "This is the schema for the fields in Item Asset Definitions. It doesn\'t require any fields.", "required": ["item_assets"], "properties": {"item_assets": {"type": "object", "not": {"additionalProperties": {"not": {"allOf": [{"$comment": "Please list all fields here so that we can force the existence of one of them in other parts of the schemas.", "anyOf": [{"required": ["order:status"]}]}, {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}]}}}}}}, {"$comment": "This is the schema for the fields in Summaries. By default, only checks the existence of the properties, but not the schema of the summaries.", "required": ["summaries"], "properties": {"summaries": {"$comment": "Please list all fields here so that we can force the existence of one of them in other parts of the schemas.", "anyOf": [{"required": ["order:status"]}]}}}]}], "definitions": {"stac_extensions": {"type": "object", "required": ["stac_extensions"], "properties": {"stac_extensions": {"type": "array", "contains": {"const": "https://stac-extensions.github.io/order/v1.1.0/schema.json"}}}}, "require_any_field": {"$comment": "Please list all fields here so that we can force the existence of one of them in other parts of the schemas.", "anyOf": [{"required": ["order:status"]}]}, "fields": {"$comment": "Add your new fields here. Don\'t require them here, do that above in the item schema.", "type": "object", "properties": {"order:status": {"type": "string"}, "order:id": {"type": "string"}, "order:date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$"}, "order:expiration_date": {"type": "string", "format": "date-time", "pattern": "(\\\\+00:00|Z)$", "deprecated": true}}, "patternProperties": {"^(?!order:)": {"$comment": "Above, change `order` to the prefix of this extension"}}, "additionalProperties": false}}}'
)
FIELD_TARGETS = {
    "order:date": ["asset", "collection", "item", "item_asset"],
    "order:expiration_date": ["asset", "collection", "item", "item_asset"],
    "order:id": ["asset", "collection", "item", "item_asset"],
    "order:status": ["asset", "collection", "item", "item_asset", "summary"],
}
FIELD_NAMES = {
    "date": "order:date",
    "expiration_date": "order:expiration_date",
    "id": "order:id",
    "status": "order:status",
}
TARGETS = ["asset", "collection", "item", "item_asset", "summary"]
T = TypeVar(
    "T", bound="pystac.Collection | pystac.Item | pystac.Asset | pystac.ItemAssetDefinition"
)


def _target_for(obj: object) -> str:
    """Identify supported STAC targets, checking Collection before its Catalog base."""
    target_types = (
        (pystac.Collection, "collection"),
        (pystac.Catalog, "catalog"),
        (pystac.Item, "item"),
        (pystac.Asset, "asset"),
        (pystac.ItemAssetDefinition, "item_asset"),
        (pystac.Link, "link"),
    )
    for object_type, target in target_types:
        if isinstance(obj, object_type):
            if target not in TARGETS:
                break
            return target
    raise pystac.ExtensionTypeError(f"Unsupported extension target: {type(obj).__name__}")


def _validation_document(obj: object) -> dict[str, Any]:
    """Serialize a real STAC owner rather than an arbitrary asset container."""
    if not isinstance(obj, pystac.STACObject):
        raise pystac.STACError("Full schema validation requires an owner")
    return obj.to_dict()


def _encode(value: Any) -> Any:
    """Convert generated objects at any depth into plain JSON containers."""
    if isinstance(value, dict):
        return {key: _encode(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_encode(child) for child in value]
    return value


class OrderExtension(
    PropertiesExtension,
    ExtensionManagementMixin[pystac.Item | pystac.Collection | pystac.Catalog],
    Generic[T],
):
    """Typed property wrapper; use ext() to check/register the extension.

    Setters preserve JSON representations, including date/time strings and nested
    dictionaries. None removes a property; set_null() explicitly writes JSON null.
    Validate the owning STAC object to enforce full schema constraints.
    """

    def __init__(self, obj: T, target: str) -> None:
        """Bind a schema-supported STAC object's metadata for live updates."""
        self.obj: T = obj
        self._target = target
        self.additional_read_properties: list[dict[str, Any]] | None = None
        if isinstance(obj, (pystac.Item, pystac.ItemAssetDefinition)):
            self.properties = obj.properties
        else:
            self.properties = obj.extra_fields
        if isinstance(obj, pystac.Asset) and isinstance(obj.owner, pystac.Item):
            self.additional_read_properties = [obj.owner.properties]

    @classmethod
    def get_schema_uri(cls) -> str:
        """The canonical schema identifier used for extension registration."""
        return SCHEMA_URI

    @classmethod
    def has_extension(cls, obj: pystac.STACObject) -> bool:
        """Check this exact schema version; migrations are not generated."""
        return SCHEMA_URI in (obj.stac_extensions or [])

    @classmethod
    def ext(cls, obj: T, add_if_missing: bool = False) -> OrderExtension[T]:
        """Wrap a schema-supported object and optionally register its extension."""
        target = _target_for(obj)
        if isinstance(obj, (pystac.Asset, pystac.ItemAssetDefinition, pystac.Link)):
            cls.ensure_owner_has_extension(obj, add_if_missing)
        else:
            cls.ensure_has_extension(obj, add_if_missing)
        return cls(obj, target)

    def _check_field(self, key: str) -> None:
        if self._target not in FIELD_TARGETS[key]:
            raise pystac.ExtensionTypeError(f"{key} does not apply to {self._target}")

    def clear(self, name: str) -> None:
        """Remove a field using its generated Python attribute name."""
        key = FIELD_NAMES[name]
        self._check_field(key)
        self.properties.pop(key, None)

    def set_null(self, name: str) -> None:
        """Write explicit JSON null; schema validation checks whether it is permitted."""
        key = FIELD_NAMES[name]
        self._check_field(key)
        self._set_property(key, None, pop_if_none=False)

    def validate(self) -> None:
        """Validate the whole Item/Collection against this extension's schema.

        Assets are validated through their owner; unowned assets cannot be checked.
        STAC core validation remains available separately through obj.validate().
        """
        from jsonschema import FormatChecker
        from jsonschema.validators import validator_for

        obj = self.obj
        if isinstance(obj, (pystac.Asset, pystac.ItemAssetDefinition, pystac.Link)):
            document = _validation_document(obj.owner)
        else:
            document = obj.to_dict()
        validator_for(SCHEMA)(SCHEMA, format_checker=FormatChecker()).validate(document)

    def apply(self, **values: Any) -> None:
        """Update only supplied fields; omitted fields are preserved.

        Keys are generated Python attribute names. Unknown or inapplicable fields
        are rejected before mutation. Validate the STAC object to check values afterwards.
        """
        for name in values:
            if name not in FIELD_NAMES:
                raise TypeError(f"Unknown extension field: {name}")
            self._check_field(FIELD_NAMES[name])
        for name, value in values.items():
            setattr(self, name, value)

    @property
    def date(self) -> str | None:
        "order:date"
        self._check_field("order:date")
        if "order:date" in self.properties:
            return cast("str | None", self.properties["order:date"])
        return cast("str | None", self._get_property("order:date", object))

    @date.setter
    def date(self, value: str | None) -> None:
        self._check_field("order:date")
        self._set_property("order:date", _encode(value))

    @property
    def expiration_date(self) -> str | None:
        "order:expiration_date"
        self._check_field("order:expiration_date")
        if "order:expiration_date" in self.properties:
            return cast("str | None", self.properties["order:expiration_date"])
        return cast("str | None", self._get_property("order:expiration_date", object))

    @expiration_date.setter
    def expiration_date(self, value: str | None) -> None:
        self._check_field("order:expiration_date")
        self._set_property("order:expiration_date", _encode(value))

    @property
    def id(self) -> str | None:
        "order:id"
        self._check_field("order:id")
        if "order:id" in self.properties:
            return cast("str | None", self.properties["order:id"])
        return cast("str | None", self._get_property("order:id", object))

    @id.setter
    def id(self, value: str | None) -> None:
        self._check_field("order:id")
        self._set_property("order:id", _encode(value))

    @property
    def status(self) -> str | None:
        "order:status"
        self._check_field("order:status")
        if "order:status" in self.properties:
            return cast("str | None", self.properties["order:status"])
        return cast("str | None", self._get_property("order:status", object))

    @status.setter
    def status(self, value: str | None) -> None:
        self._check_field("order:status")
        self._set_property("order:status", _encode(value))

    @classmethod
    def summaries(
        cls, obj: pystac.Collection, add_if_missing: bool = False
    ) -> SummariesOrderExtension:
        """Wrap schema-declared Collection summaries and optionally register the extension."""
        if not isinstance(obj, pystac.Collection):
            raise pystac.ExtensionTypeError("Summaries require a Collection")
        cls.ensure_has_extension(obj, add_if_missing)
        return SummariesOrderExtension(obj)


class SummariesOrderExtension(SummariesExtension):
    """Collection summaries; ranges, lists and JSON Schema objects are preserved."""

    @property
    def status(self) -> list[Any] | pystac.RangeSummary[Any] | dict[str, Any] | None:
        value = self.summaries.to_dict().get("order:status")
        if isinstance(value, dict) and "minimum" in value and "maximum" in value:
            return self.summaries.get_range("order:status")
        return value

    @status.setter
    def status(self, value: list[Any] | pystac.RangeSummary[Any] | dict[str, Any] | None) -> None:
        self.summaries.remove("order:status")
        self._set_summary("order:status", value)
