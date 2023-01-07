# from odoo import models, fields, api
# import json

# class Zone(models.Model):
#     _name = 'zone'
#     _description = 'Modelo de zonas'

#     codigo = fields.Char(string='Código', size=5, unique=True)
#     nombre = fields.Char(string='Nombre', size=50)
#     country_id = fields.Many2one('res.country', string='País')

#     provincia_id = fields.Many2one('res.country.state', string='Provincia')
#     provincia_ids = fields.One2many(comodel_name='', inverse_name='', string='')
    

#     provincia_id_domain = fields.Char(compute='_compute_provincia_id_domain', store=False)

#     @api.depends('country_id')
#     def _compute_provincia_id_domain(self):
#         for rec in self:
#             if rec.country_id:
#                 rec.provincia_id_domain = json.dumps([('country_id', '=', rec.country_id.id)])

