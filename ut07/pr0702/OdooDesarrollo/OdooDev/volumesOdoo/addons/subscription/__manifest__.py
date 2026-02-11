# -*- coding: utf-8 -*-
{
    'name': "subscription",

    'summary': 'Gestión de suscripciones',

    'description': 'En esta primera práctica sobre vistas practicaremos con las principales opciones que tiene la vista de tipo lista para personalizar los datos que se muestran al usuario',

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_basico.xml',
        'views/views_uso.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
