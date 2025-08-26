from odoo import models, fields

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    priority = fields.Selection(
        string='priority',
        selection=[('0', 'baja'), 
                   ('1', 'media'),
                   ('2', 'alya')],
        default='1'   
    )
    