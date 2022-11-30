from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    type_of_sale = fields.Selection(
        [
            ("equipment", "Equipos"),
            ("maintenance", "Mantenimientos"),
            ("services", "Servicios")
        ],
        string="Tipo de venta",
        tracking=True,
        default="equipment",
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
        compute= "_compute_is_require_warranty"
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

    logic_maintenance = fields.Integer(string="Cant. Mantenimiento")

    maintenance_equipment_id = fields.Many2one(
        comodel_name= "maintenance.equipment", 
        string= "Mantenimiento",
        domain="[('res_partner_id', '=?', partner_id)]"
    )

    @api.model
    def _prepare_invoice(self):
        self.ensure_one()
        invoice =  super(SaleOrder, self)._prepare_invoice()
        invoice['type_of_sale'] = self.type_of_sale
        invoice['has_maintenance'] = self.has_maintenance
        invoice['has_warranty'] = self.has_warranty
        invoice['warranty_expiration_date'] = self.warranty_expiration_date
        invoice['next_maintenance_date'] = self.next_maintenance_date
        return invoice

    def action_confirm(self):
        before_date = self.date_order
        res = super(SaleOrder, self).action_confirm()
        self.date_order = before_date
        return res
        
        


    @api.depends("type_of_sale")
    def _compute_is_require_warranty(self):
        if(self.type_of_sale == "equipment"):
            self.has_warranty = True
        else:
            self.has_warranty = False

    @api.onchange('type_of_sale')
    def calculate_default_fields_value(self):
        
        if(self.type_of_sale == 'equipment'):
            self.has_maintenance = True
            self.warranty_expiration_date = self.date_order + relativedelta(years=10)
            self.next_maintenance_date = self.date_order + relativedelta(years=1)
        elif self.type_of_sale == 'maintenance':
            self.next_maintenance_date = self.date_order + relativedelta(years=1)
        else:
            self.has_maintenance = False
            self.warranty_expiration_date = None
            self.next_maintenance_date = None
            self.logic_maintenance = 0

    @api.onchange('date_order')
    def calculate_default_date_value(self):
        if(self.type_of_sale == 'equipment'):
            self.warranty_expiration_date = self.date_order + relativedelta(years=10)
            self.next_maintenance_date = self.date_order + relativedelta(years=1)
        elif self.type_of_sale == 'maintenance':
            self.next_maintenance_date = self.date_order + relativedelta(years=1)

    @api.onchange("warranty_expiration_date")
    def validate_warranty_expiration_date(self):
        if(self.warranty_expiration_date == False or self.warranty_expiration_date == None):
            return
        maxDate = self.date_order + relativedelta(years=10)
        if(self.warranty_expiration_date > maxDate.date()):
            raise UserError("La fecha no debe superar los 10 años")

    @api.onchange("next_maintenance_date")
    def validate_next_maintenance_date(self):
        print(self.next_maintenance_date)
        print(self.warranty_expiration_date)
        if(self.next_maintenance_date == False or self.type_of_sale != 'equipment'):
            return
        if(self.next_maintenance_date > self.warranty_expiration_date):
            raise UserError("La fecha de proximo mantenimiento no debe ser mayor a la fecha de garantia")