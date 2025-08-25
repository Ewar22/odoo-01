from odoo import models, fields 

class Planets(models.Model):

    _name = 'planets'
    _description = 'Planets'

    name = fields.Char(string='Name')
    masa = fields.Float(string='Masa')
    volumen  = fields.Integer(string='volumen')
    distance_sun = fields.Float(
        string='Diostance Sun',
        domain=[('distance_sun', '>=', 0)]
    )

    have_moons = fields.Selection(
        string='have_moons',
        selection=[('0', 'no'), ('1', 'yes')],
        default='0'
    )
    