# -*- coding: utf-8 -*-
{
    'name': "incidencias",

    'summary': """Módulo de incidiencias""",

    'description': """Regristro de las incidencias de los municipios de Gran Canaria""",

    'author': "Diego",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
        'reports/municipios_report.xml'
        'reports/municipios_report_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',
}