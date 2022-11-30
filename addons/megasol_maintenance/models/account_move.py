from odoo import models, fields
from datetime import datetime

class AccountModel(models.Model):
    _inherit = "account.move"

    equipment_or_maintenance_was_created = fields.Boolean(string="Garantia o Mantenimiento creado")
    type_of_sale = fields.Selection(
        [
            ("equipment", "Equipos"),
            ("maintenance", "Mantenimientos"),
            ("services", "Servicios")
        ],
        string="Tipo de venta",
        tracking=True,
        states={"draft": [("readonly", False)]},
        copy=False,
        required=True
    )
    has_maintenance = fields.Boolean(
        string= "Mantenimiento",
        states={"draft": [("readonly", False)]},
    )
    has_warranty = fields.Boolean(
        string= "Garantía",
        states={"draft": [("readonly", False)]},
    )
    warranty_expiration_date = fields.Date(
        string= "Fecha garantía",
        states={"draft": [("readonly", False)]},
        tracking=True,
    )

    next_maintenance_date = fields.Date(
        string= "Prox. Mantenimiento",
        states={"draft": [("readonly", False)]},
        tracking=True,
    )

    def action_post(self):
        super(AccountModel, self).action_post()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", self.ids)
        if not self.ids:
            return

        if(self.equipment_or_maintenance_was_created):
             return
        
        account_move_id = self.ids[0]
        sale_order = self.env['sale.order'].sudo().search([['name', '=' , self.invoice_origin]])

        if not sale_order:
            return

        if sale_order.type_of_sale == "services":
            return

        maintenance_equipment = self.env['maintenance.equipment'].sudo().browse(sale_order.maintenance_equipment_id.id)
        if not maintenance_equipment:
            equipment = {
                "name": f"Garantia - {self.partner_id.vat} - {self.name}",
                "account_move_id": account_move_id,
                "res_partner_id": self.partner_id.id,
                "maintenance_team_id": 1,
                "period": 365,
                "warranty_date": sale_order.warranty_expiration_date,
                "assign_date": datetime.today(),
                'maintenance_qty': sale_order.logic_maintenance
            }
            equipment_id = maintenance_equipment.create(equipment)
            self.create_maintenance(
                res_partner=self.partner_id, 
                equipment_id=equipment_id.id,
                sale_order=sale_order,
                account_move = self
            )
        else:
            self.create_maintenance(
                res_partner=self.partner_id, 
                equipment_id=maintenance_equipment.id,
                sale_order=sale_order,
                account_move = self
            )
        self.equipment_or_maintenance_was_created = True

    def create_maintenance(self, res_partner, equipment_id, sale_order, account_move):
        maintenance =  {
            "name": f"mantenimiento - {res_partner.name} - {account_move.name}",
            "equipment_id": equipment_id,
            "maintenance_team_id": 1,
            "priority" : "2" if sale_order.type_of_sale == "maintenance" else "1",
            "schedule_date": sale_order.next_maintenance_date,
            "subtotal": account_move.amount_untaxed,
            "itbis": account_move.amount_tax,
            "total": account_move.amount_total,
        }
        return self.env["maintenance.request"].create(maintenance)
