# -*- coding: utf-8 -*-
{
    'name': "Inyeccion_de_bebidass",
    'summary': "Modulo para saber la bebida respecto al nivel de sueno del alumno",
    'description': """Un grupo de alumnos del Daniel Castelao, se están acostando tarde porque 
estudian mucho y pican mucho código en casa. En ocasiones, a la mañana 
siguiente en el centro, tienen sueño en clase, pero no tienen claro por qué opción 
decantarse de entre las maravillosas ofertas de los establecimientos que rodean el 
centro. Como tienen dudas de qué escoger, un compañero decide realizar un 
módulo sencillo que establece la bebida que deben tomar en función del nivel de 
sueño que tengan.""",
    'author': "Piero López",
    'website': "https://www.danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

