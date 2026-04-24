from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    main_supplier_id = fields.Many2one(
        comodel_name="res.partner",
        string="Fournisseur principal",
        compute="_compute_main_supplier",
        store=True,
    )
    main_supplier_code = fields.Char(
        string="Code fournisseur",
        compute="_compute_main_supplier",
        store=True,
    )
    main_supplier_price = fields.Float(
        string="Prix fournisseur",
        compute="_compute_main_supplier",
        store=True,
    )
    main_supplier_delay = fields.Integer(
        string="Délai fournisseur (j)",
        compute="_compute_main_supplier",
        store=True,
    )
    main_supplier_min_qty = fields.Float(
        string="Qté min. fournisseur",
        compute="_compute_main_supplier",
        store=True,
    )

    @api.depends(
        "seller_ids",
        "seller_ids.sequence",
        "seller_ids.partner_id",
        "seller_ids.product_code",
        "seller_ids.price",
        "seller_ids.delay",
        "seller_ids.min_qty",
    )
    def _compute_main_supplier(self):
        for rec in self:
            seller = rec.seller_ids[:1]
            rec.main_supplier_id = seller.partner_id or False
            rec.main_supplier_code = seller.product_code or False
            rec.main_supplier_price = seller.price or 0.0
            rec.main_supplier_delay = seller.delay or 0
            rec.main_supplier_min_qty = seller.min_qty or 0.0
