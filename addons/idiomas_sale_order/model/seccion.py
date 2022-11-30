from odoo import fields, models, api
from odoo.exceptions import ValidationError
import json

class Seccion(models.Model):
    _name = 'sale.seccion'
    _description = 'Mantenimiento de las secciónes'

    name = fields.Char(string='Sección', required = True)
    code = fields.Char(string='Código', required = True, size=8)
    languaje_id = fields.Many2one(comodel_name='sale.languaje', string='Idioma', required = True)
    level_id = fields.Many2one(comodel_name='sale.level', string='Nivel', required = True)
    room_id = fields.Many2one(comodel_name='sale.room', string='Aula', required = True)
    schedule_id = fields.Many2one(comodel_name='sale.schedule', string='Horario', required = True)
    student_qty = fields.Integer(string='Cantidad de estudiantes', required = True)
    professor_id = fields.Many2one(comodel_name='sale.professor', string='Profesor', required = True)

    level_id_domain = fields.Char(
        compute="_compute_level_id_domain",
        readonly=True,
        store=False,
    )

    @api.depends('languaje_id')
    def _compute_level_id_domain(self):
       for rec in self:
           rec.level_id_domain = json.dumps([('languaje_id', '=', rec.languaje_id.id)])

    _sql_constraints = [
        ('section_unique_code', 'unique(code)', 'Codigo ya existe'),
        ('section_unique_name', 'unique(name)', 'Nombre ya existe')
    ]

    @api.constrains('code')
    def _check_code(self):
        if len(self.code) != 8:
            raise ValidationError("El codigo debe ser de 8 digitos")

    @api.constrains('schedule_id', 'room_id')
    def _check_chedule_id_room_id_exist(self):
        count = self.search([('schedule_id.id', '=', self.schedule_id.id), 
                             ('room_id.id', '=', self.room_id.id)])
        if(len(count) > 1):
            raise ValidationError("Ya existe una seccion con la misma aula y horario que esta.")
    
    
    
    