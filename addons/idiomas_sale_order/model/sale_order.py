from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    seccion_id = fields.Many2one(comodel_name='sale.seccion', string='Seccion', required = True)
    bimestre_id = fields.Many2one(comodel_name='sale.bimestre', string='Bimestre', required = True)

    ## related seccion field
    languaje_name = fields.Char(related="seccion_id.languaje_id.name", string="Idioma")
    level_name = fields.Char(related="seccion_id.level_id.name", string="Nivel")
    room_name = fields.Char(related="seccion_id.room_id.name", string="Aula")
    schedule_name = fields.Char(related="seccion_id.schedule_id.code", string="Horario")
    professor_name = fields.Char(related="seccion_id.professor_id.name", string="Profesor")
