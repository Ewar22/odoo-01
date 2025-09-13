{
    'name': 'Planets',
    'description': 'planets info',
    'author': 'Eduard Montano',
    
    # ✅ CATEGORÍA ÚNICA PARA PLANETS
    'category': 'Productivity',  # ← Diferente a Sales
    
    'version': '16.0.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/planets_views.xml',
        'views/planets_menu.xml',
        
        
    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}