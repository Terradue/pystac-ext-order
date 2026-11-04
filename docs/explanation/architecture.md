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

# Scope, architecture, and validation

## Package structure

The distribution is `pystac-ext-order`; the import is `pystac.extensions.order`.
The wheel excludes the shared namespace initializer owned by PySTAC.
`OrderExtension` wraps existing metadata dictionaries, so PySTAC's normal
serialization preserves changes. It does not submit or monitor orders.

The module is generated. Schema-defined changes belong in the source schema
and repository generation workflow, rather than manual edits to generated Python.

## Owners and summaries

Assets and item asset definitions check registration on their owner. Item-owned
Assets inherit missing fields from Item properties; explicit null masks an
inherited value. Collection-owned Assets do not inherit Collection fields.
Collections expose direct metadata and a separate status summary wrapper.
Summaries preserve lists, ranges, and JSON Schema dictionaries without computing
values from child Items.

## Validation boundaries

Install `pystac[validation]` to use validation. `OrderExtension.validate()`
validates the entire Item or Collection against the embedded Order schema with
format checking. For Assets and item asset definitions it validates their owner;
an unowned object raises `pystac.STACError`. Invalid documents raise
`jsonschema.exceptions.ValidationError`.

This extension-only check does not validate the STAC core schema. Use
`item.validate()` or `collection.validate()` for core and registered extension
validation; that path may retrieve remote schemas.

Property assignment, `apply()`, and `to_dict()` do not validate the schema.
`apply()` checks field names before mutation. Explicit null is distinct from a
missing field, but is not valid for the schema's string fields. Use UTC date-time
strings ending in `Z` for dates, which remain strings throughout serialization.

## Schema registration and versions

`SCHEMA_URI` identifies Order v1.1.0. `has_extension()` checks that exact URI.
`ext()` and `summaries()` require registration on STAC objects unless
`add_if_missing=True` is supplied. Adding this URI does not migrate older metadata.
Owned objects use their owner's registration. An unowned Asset may be wrapped
without adding registration, but cannot be validated until it has an owner.
