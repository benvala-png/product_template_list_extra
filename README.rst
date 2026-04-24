Product Template List Extra Columns
=====================================

Extends the ``product.template`` list view with optional columns (all hidden by default).

**Added columns:**

- Image thumbnail
- Deposit flag & linked deposit product (``pos_container_deposit``)
- Main supplier: partner, supplier code, price, lead time, min qty
- POS: available in POS, to weigh, POS category
- References: internal reference, barcode
- Categorisation: internal category, product tags
- Prices: sales price, cost, customer taxes, vendor taxes
- Stock: product type, on-hand qty, forecasted qty
- Units of measure: UoM, purchase UoM
- Misc: active, can be sold, can be purchased, company, responsible, weight, volume

All columns are ``optional="hide"`` — users activate them individually via the column chooser.

**Computed stored fields on product.template:**

- ``main_supplier_id``: first vendor by sequence
- ``main_supplier_code``: vendor product code
- ``main_supplier_price``: vendor price
- ``main_supplier_delay``: vendor lead time (days)
- ``main_supplier_min_qty``: vendor minimum quantity
