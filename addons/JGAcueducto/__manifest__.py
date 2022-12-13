{
    'name': "JG Acueductos",
    'summary': """
        Incorpora funcionalidades para que jg acueductos funcione
        """,
    'author': "Caonabo Mena",
    'license': 'LGPL-3',
    'category': 'Generic Modules',
    'version': '15.0.1.0.0',
    'installable': True,
    'application': False,
    'auto_install': False,
    # any module necessary for this one to work correctly
    'depends': ['stock', 'web_domain_field'],

    # always loaded
    'data': [
        'views/area_view.xml',
        'views/product_category.xml',
        'views/product_template.xml',
        'security/ir.model.access.csv'
    ],

}
