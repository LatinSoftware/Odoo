from odoo import models, fields, api
import json

class Ciudad(models.Model):
    _name = 'ciudad'
    _description = 'Modelo de ciudades'

    codigo = fields.Char(string='Código', size=3, unique=True)
    nombre = fields.Char(string='Nombre', size=50)
    country_id = fields.Many2one('res.country', string='País')
    municipio_id = fields.Many2one('municipio', string='Municipio')
    municipio_id_domain = fields.Char(compute='_compute_municipio_id_domain', store=False)

    @api.depends('country_id')
    def _compute_municipio_id_domain(self):
        for rec in self:
            if rec.country_id:
                rec.municipio_id_domain = json.dumps([('country_id', '=', rec.country_id.id)])
            else:
                rec.municipio_id_domain = False