from odoo import models, fields, api
import json
class Seccion(models.Model):
    _name = 'seccion'
    _description = 'Modelo de secciones'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True, unique=True)

    country_id = fields.Many2one('res.country', string='Pais')

    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    provincia_id_domain = fields.Char(compute='_compute_provincia_id_domain', store=False)

    municipio_id = fields.Many2one('municipio', string='Municipio')
    municipio_id_domain = fields.Char(compute='_compute_municipio_id_domain', store=False)


    @api.depends('country_id')
    def _compute_provincia_id_domain(self):
        for rec in self:
            if rec.country_id:
                rec.provincia_id_domain = json.dumps([('country_id', '=', rec.country_id.id)])


    @api.depends('provincia_id')
    def _compute_municipio_id_domain(self):
        for rec in self:
            if rec.provincia_id:
                rec.municipio_id_domain = json.dumps([('provincia_id', '=', rec.provincia_id.id)])
            