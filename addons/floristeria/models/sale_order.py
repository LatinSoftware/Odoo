from odoo import _, api, fields, models
import json
class SaleOrder(models.Model):
     _inherit = 'sale.order'

     contact_shipping_id = fields.Many2one("res.partner.contacts", string="Direccion de entrega", ondelete="restrict")
     contact_shipping_id_domain = fields.Char(
       compute="_compute_contact_shipping_iddomain",
       readonly=True,
       store=False) 

     @api.depends('partner_id')
     def _compute_contact_shipping_iddomain(self):
          for rec in self:
               rec.contact_shipping_id_domain = json.dumps( [('partner_id', '=', rec.partner_id.id)])
