from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string='Codigo', required=True)