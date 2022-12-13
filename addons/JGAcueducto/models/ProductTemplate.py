from odoo import models, fields, api, exceptions
import json

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    area_id = fields.Many2one(comodel_name='stock.area', string='Area', required=True)

    area_id_domain = fields.Char(
        compute="_compute_area_id_domain",
        readonly=True,
        store=False,
    )

    @api.depends('categ_id')
    def _compute_area_id_domain(self):
       for rec in self:
           rec.area_id_domain = json.dumps([('category_id', '=', rec.categ_id.id)])

    @api.onchange('area_id', 'standard_price')
    def _onchange_area_id(self):
        if(self.area_id.cost_percentage and self.standard_price):
            self.list_price = self.standard_price + (self.standard_price * (self.area_id.cost_percentage / 100))
    
    @api.model
    def create(self, values):
        # Create and assing unique code base on stock area data
        res = super(ProductTemplate, self).create(values)
        for rec in res:
            rec.default_code = rec.area_id.GenerateSecuence()
        return res

    @api.model
    def write(self, values):
        # verify list_price > standard_price
        for rec in self:
            if(rec.list_price < rec.standard_price):
                raise exceptions.ValidationError("El precio de venta no puede ser menor al costo del producto")
        return super(ProductTemplate, self).write(values)
    
    
    