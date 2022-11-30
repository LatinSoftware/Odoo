from odoo import models, fields

class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    currency_id = fields.Many2one('res.currency', string="Currency",
                                 related='company_id.currency_id',
                                 default=lambda
                                 self: self.env.user.company_id.currency_id.id)

    subtotal = fields.Monetary(string= "Sub Total")
    itbis = fields.Monetary(string= "ITBIS")
    total = fields.Monetary(string="Total")


    account_move_name =  fields.Char(related="equipment_id.account_move_id.name", string="Numero de Factura")
    partner_phone= fields.Char(related="equipment_id.res_partner_id.phone", string="Teléfono")
    partner_mobile= fields.Char(related="equipment_id.res_partner_id.mobile", string="Móvil")
    partner_email= fields.Char(related="equipment_id.res_partner_id.email", string="Correo electrónico")
    partner_direction = fields.Char(related="equipment_id.res_partner_id.street", string="Dirección")
    partner_city = fields.Char(related="equipment_id.res_partner_id.city", string="Ciudad")
    partner_province = fields.Char(related="equipment_id.res_partner_id.state_id.name", string="Provincia")