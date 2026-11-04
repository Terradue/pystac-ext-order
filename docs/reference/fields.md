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

# Order fields

`OrderExtension.ext()` supports Items, Collections, Assets, and item asset
definitions. Catalogs and Links are unsupported.

| STAC field | Python property | Value type | Notes |
| --- | --- | --- | --- |
| `order:status` | `status` | `str` | Required on Item properties; also exposed in summaries |
| `order:id` | `id` | `str` | Optional order identifier |
| `order:date` | `date` | `str` | Optional UTC date-time string; use a `Z` suffix |
| `order:expiration_date` | `expiration_date` | `str` | Deprecated; optional UTC date-time string |

All four fields are supported on all four targets. The embedded schema accepts
arbitrary status strings; the wrapper does not impose an enum. Collection
validation accepts its schema's alternatives for top-level fields, Assets,
item asset definitions, or summaries.

## Storage and inheritance

Items and item asset definitions use `properties`; Collections and Assets use
`extra_fields`. Wrappers mutate these dictionaries directly. Item-owned Assets
fall back to Item properties when a local field is absent. Explicit null masks
that fallback. Other targets do not inherit owner metadata.

## Update semantics

- Getters return `None` for missing values without a fallback, or explicit null.
- Setters and `apply()` remove fields assigned `None`.
- `apply()` preserves omitted fields and rejects unknown names with `TypeError`
  before changing any fields.
- `clear(name)` removes a field and is safe to repeat.
- `set_null(name)` stores explicit null, which the string fields reject during validation.
- `clear()` and `set_null()` accept Python property names and raise `KeyError` for unknown names.
- Setters do not validate values; call `validate()` explicitly.

## Collection summaries

`OrderExtension.summaries(collection)` exposes only `status`. It accepts lists,
`pystac.RangeSummary` objects, JSON Schema dictionaries, or `None`. A dictionary
with `minimum` and `maximum` is returned as a `RangeSummary`. Assignments replace
the previous representation; `None` removes it. The helper does not compute
summaries from Items and has no `apply()` method.
