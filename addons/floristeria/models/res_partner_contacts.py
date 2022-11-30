from email.policy import default
from secrets import choice
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import random

class ResPartnerContacts(models.Model):
    _name = 'res.partner.contacts'
    _descripcion = 'Contacts'

    def _get_default_country(self):
        if self.env.company.country_id and self.env.company.country_id.code.upper() == 'DO':
            return self.env.company.country_id.id
        return 0 

    def _set_kanban_color(self):
        random.choice(range(1, 5))

    partner_id = fields.Many2one("res.partner", string="Cliente", ondelete="cascade")
    name = fields.Char(string="Nombre del contacto", required=True)
    street = fields.Char(string="Direccion", required=True)
    state_id = fields.Many2one("res.country.state", string="Ciudad", ondelete="restrict")
    country_id = fields.Many2one("res.country", string="Pais", ondelete="restrict", default=_get_default_country)
    phone = fields.Char(string="Telefono", size=11)
    email = fields.Char(string="Email")
    image_128 = fields.Binary(string="Imagen")
    color = fields.Integer(string='Color', compute="_set_kanban_color")

    # @api.constrains('email')
    # def validate_email(self):
    #     """
    #     Raise a Validation Error when user enters incorrect email
    #     ---------------------------------------------------------
    #     """
    #     for obj in self:
    #         if obj.email \
    #             and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|\
    #                 [0-9]{1,3})(\\]?)$", obj.email) is None:
    #             raise ValidationError(_(
    #                 """Please add valid Email Address:%s""" % obj.email))
    #     return True

    