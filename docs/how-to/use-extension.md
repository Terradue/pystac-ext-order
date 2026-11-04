<!--
Copyright 2026 Terradue

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Work with Order metadata

## Update an Item

Using the Item from the [tutorial](../tutorials/first-steps.md):

```python
order.apply(status="succeeded")
assert order.id == "order-1"  # Omitted fields are preserved.
order.id = None  # Remove order:id.
order.clear("date")  # Removal is also available by Python property name.
```

Use `set_null("id")` only when you deliberately need an explicit JSON null.
The Order schema requires strings, so explicit null fails validation.

## Attach metadata to Assets

```python
asset = pystac.Asset(href="https://example.com/data.tif")
item.add_asset("data", asset)
asset_order = OrderExtension.ext(asset)
assert asset_order.status == "succeeded"  # Falls back to Item metadata.
asset_order.status = "pending"
assert asset.extra_fields["order:status"] == "pending"
assert order.status == "succeeded"
asset_order.clear("status")
assert asset_order.status == "succeeded"
```

Registration is checked on the owner. Attach Assets and item asset definitions
before using `add_if_missing=True`. Collection-owned Assets do not inherit
Collection fields. Asset validation checks the entire owner, including siblings.

## Collections and summaries

```python
collection = pystac.Collection(
    id="orders",
    description="Order examples",
    extent=pystac.Extent(
        pystac.SpatialExtent([[-180, -90, 180, 90]]),
        pystac.TemporalExtent([[None, None]]),
    ),
)
collection_order = OrderExtension.ext(collection, add_if_missing=True)
collection_order.status = "pending"
summaries = OrderExtension.summaries(collection)
summaries.status = ["pending", "succeeded"]
assert collection.summaries.to_dict()["order:status"] == ["pending", "succeeded"]
summaries.status = None  # Remove the summary.
```

For an item asset definition, attach a `pystac.ItemAssetDefinition` to the
Collection's `item_assets`, then retrieve `collection.item_assets["data"]`
and pass that definition to `OrderExtension.ext()`. PySTAC copies definitions
when assigning the mapping, so retrieve the attached definition before editing it.
