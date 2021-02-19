# -*- coding: utf-8 -*-
{
    'name': "Discográfica",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [      
        'security/discografica_security.xml',  
        'security/ir.model.access.csv',
        'views/discografica_view.xml',
        'views/artista_view.xml',
        'views/album_view.xml',
        'views/cancion_view.xml',
        'views/gira_view.xml',
        'views/concierto_view.xml',
        'views/entrada_view.xml',
        'views/cliente_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':'True',
    'application':'True',
}
