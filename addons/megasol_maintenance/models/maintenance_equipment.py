from odoo import models, fields, api

class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    account_move_id = fields.Many2one(
        comodel_name="account.move", 
        string="Factura",
        domain="[('move_type', '=', 'out_invoice')]",
        tracking=True
        )
    res_partner_id = fields.Many2one(
        comodel_name="res.partner", 
        string="Cliente",
        tracking=True,
    )
    maintenance_qty = fields.Integer(string="Cant. Mantenimiento")

    partner_vat = fields.Char(related="res_partner_id.vat", string="RNC / Cedula")
    partner_phone= fields.Char(related="res_partner_id.phone", string="Teléfono")
    partner_mobile= fields.Char(related="res_partner_id.mobile", string="Móvil")
    partner_email= fields.Char(related="res_partner_id.email", string="Correo electrónico")
    partner_direction = fields.Char(related="res_partner_id.street", string="Dirección")
    partner_city = fields.Char(related="res_partner_id.city", string="Ciudad")
    partner_province = fields.Char(related="res_partner_id.state_id.name", string="Provincia")

    
    @api.onchange("account_move_id")
    def _get_partner_id(self):
        for rec in self:
            rec.res_partner_id = rec.account_move_id.partner_id.id