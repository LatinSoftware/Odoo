from odoo import _, api, fields, models

class ResPartner(models.Model):
     _inherit = 'res.partner'

     contact_ids = fields.One2many('res.partner.contacts', 'partner_id', string="Contactos")