# -*- coding: utf-8 -*-
{
    'name': "Practica Final",

    'summary': """
        Proyecto Final de Odoo 14, clases de Desarrollo Multiplataformas
    """,

    'description': """
        Proyecto final con relaciones entre tablas, funciones en campos, y foto de modulo
    """,

    'author': "Ricardo Quinn Romeijn",
    'website': "https://github.com/RicardoQ-Romeijn/Odoo14Final",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/templates.xml', # Plantilla de View
        #'security/ir.model.access.csv', # Accesso a los Archivos
        'security/security.xml', # Seguridad e Usuarios
        'security/ir.model.access.csv', # Accesso a los Archivos
        # Views
        'views/view_clientes.xml',
        'views/view_proveedores.xml',
        'views/view_empleados.xml',
        'views/view_categorias.xml',
        'views/view_productos.xml',
        'views/view_pedidos.xml',
        'views/view_detpedidos.xml',
        # Reports
        'report/report_clientes.xml',
        'report/report_proveedores.xml',
        'report/report_empleados.xml',
        'report/report_categorias.xml',
        'report/report_productos.xml',
        'report/report_pedidos.xml',
        'report/report_detpedidos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
