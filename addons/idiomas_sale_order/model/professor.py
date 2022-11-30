from odoo import  fields, models


class Professor(models.Model):
    _name = 'sale.professor'
    _description = 'Mantenimiento de profesores.'

    name = fields.Char(string='Nombre', required=True)
    document = fields.Char(string='Cedula / Pasaporte', required=True)
    phone_number = fields.Char(string='Telefono', required=True)
    profession = fields.Char(string='Profesion', required=True)
    mail = fields.Char(string='Correo Electronico', required=True)