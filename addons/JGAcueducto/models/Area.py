from odoo import models, fields

class StockArea(models.Model):
    _name="stock.area"

    code = fields.Char("Codigo")
    category_id = fields.Many2one(comodel_name='product.category', string='Categoria', required=True)
    name = fields.Char(string='Nombre', required=True)
    incremental = fields.Integer(string='Incremental', default=1, required=True)
    mida_secuence = fields.Integer(string='Mida de secuencia', help='número de 0 que se colocara. A la de izquierda', required=True)
    next_number = fields.Integer(string='Próximo número', help='número inicial en que se empezara a contabilizar', default=0, required=True)
    cost_percentage = fields.Float(string='Porcentaje de venta sobre el costo', required=True)
    
    
    def GenerateSecuence(self):
        number = str(self.next_number).zfill(self.mida_secuence)
        secuence = self.category_id.code + self.code + number
        self.next_number += self.incremental
        return secuence
    
    _sql_constraints = [
        ('code_uk_field', 'unique(code)', 'Codigo ya esta registrado en el sistema.')
    ]
    
    
    

    