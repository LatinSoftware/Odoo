{
    'name': 'Idiomas Sale Oorder',
    'version': '15.0.1.0.1',
    'summary': '''
        Agrega campos de idioma, seccion, aula, nivel, horario y bimestre al las ordenes de compras y al reporte.
    ''',
    'category': 'sale',
    'author': 'Caonabo Mena',
    'maintainer': 'Rafael Abreu',
    'depends': [
        'web_domain_field',
        'sale_management'
    ],
    'data': [
        'views/languaje.xml',
        'views/level.xml',
        'views/room.xml',
        'views/schedule.xml',
        'views/seccion.xml',
        'views/professor.xml',
        'views/bimestre.xml',
        'views/menu.xml',
        'views/sale_order.xml',
        'security/ir.model.access.csv',
        'data/week_days.xml',
        'report/sale_order.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
