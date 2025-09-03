# __manifest__.py
{
    'name': 'Custom Sales',
    'description': 'Personalización de ventas', 
    'author': 'Eduard Montano',
    'category': 'Sales',  # ✅ Debe ser 'Sales'
    'version': '16.0.0.1',
    'depends': ['sale'],  # ✅ DEBE DEPENDER DE SALE
    'data': [
        'views/custom_sale_order_view.xml',
    ],
    'license': 'AGPL-3',
    'application': True,  # ✅ DEBE SER TRUE
    'installable': True,
    'auto_install': False,
}