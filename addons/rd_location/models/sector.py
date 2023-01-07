from odoo import models, fields, api
import json

class Sector(models.Model):
    _name = 'sector'
    _description = 'Modelo de sectores'

    name = fields.Char(string='Nombre', required=True)
    # Agregamos un nuevo campo "Código" único al modelo "Sector"
    code = fields.Char(string='Código', required=True, unique=True)

    country_id = fields.Many2one('res.country', string='Pais')

    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    provincia_id_domain = fields.Char(compute='_compute_provincia_id_domain', store=False)

    municipio_id = fields.Many2one('municipio', string='Municipio')
    municipio_id_domain = fields.Char(compute='_compute_municipio_id_domain', store=False)
    
    city_id = fields.Many2one('seccion', string='Sección', required=True)
    city_id_domain = fields.Char(compute='_compute_city_id_domain', store=False)

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

    @api.depends('municipio_id')
    def _compute_city_id_domain(self):
        for rec in self:
            if rec.municipio_id:
                rec.municipio_id_domain = json.dumps([('municipio_id', '=', rec.municipio_id.id)])

    @api.depends('city_id')
    def _compute_city_id_domain(self):
        for rec in self:
            if rec.city_id:
                rec.city_id_domain = json.dumps([('city_id', '=', rec.city_id.id)])
