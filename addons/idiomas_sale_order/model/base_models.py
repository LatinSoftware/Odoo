from odoo import fields, models, api

class Languaje(models.Model):
    _name = 'sale.languaje'
    _description = 'Mantenimiento de idiomas'

    name = fields.Char(string='Idioma', required = True)
    code = fields.Char(string='Código', required = True)

    _sql_constraints = [
    ('languaje_unique_code', 'unique(code)', 'Codigo ya existe')
]
    
class Level(models.Model):
    _name = 'sale.level'
    _description = 'Mantenimiento de los niveles'

    code = fields.Char(string='Código', required = True)
    name = fields.Char(string='Asignatura', required = True)
    languaje_id = fields.Many2one(comodel_name='sale.languaje', string='Idioma', required = True)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f"{rec.code} - {rec.name}"))
        return result

    _sql_constraints = [
    ('level_unique_code', 'unique(code)', 'Codigo ya existe')
    ]
    

class Schedule(models.Model):
    _name = 'sale.schedule'
    _description = 'Mantenimiento de los horarios'

    code = fields.Char(string='Código', required = True)
    days_of_week = fields.Many2many(comodel_name='sale.weekday', string='Dias', required = True)
    start_date = fields.Datetime(string='Fecha de inicio.', required = True)
    end_date = fields.Datetime(string='Fecha Fin', required = True)
    name = fields.Char(string='nombre');

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, rec.code))
        return result

    _sql_constraints = [
        ('scheduke_unique_code', 'unique(code)', 'Codigo ya existe')
    ]

class DayOfWeeks(models.Model):
    _name = 'sale.weekday'
    name = fields.Selection(string='Dia', required=True, selection=[('sunday', 'Domingo'), 
                                                     ('monday', 'Lunes'),
                                                     ('tuesday', 'Martes'),
                                                     ('wednesday', 'Miercoles'),
                                                     ('thuesday', 'Jueves'),
                                                     ('friday', 'Viernes'),
                                                     ('saturday', 'Sabado'),
                                                     ])
    

class Room(models.Model):
    _name = 'sale.room'
    _description = 'Mantenimiento de las aulas'

    name = fields.Char(string='Aula', required = True)
    code = fields.Char(string='Código', required = True)

    _sql_constraints = [
        ('room_unique_code', 'unique(code)', 'Codigo ya existe')
    ]

class Bimestre(models.Model):
    _name = 'sale.bimestre'
    _description = 'Mantenimiento Bimestre'

    name = fields.Char(string='Bimestre', required = True)