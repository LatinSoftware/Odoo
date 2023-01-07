{
    'name': "Ubicacion de republica dominicana",
    'summary': """
        Este modulo incorpora la localizacion en republica dominicana, agrega mantenimiento de 
        - Ciudad
        - Municipio
        - Provincia
        - Sectores
        - Secciones
        - Regiones
        - Zonas
        """,
    'author': "Caonabo Mena",
    'license': 'LGPL-3',
    'category': 'Generic Modules',
    'version': '15.0.1.0.0',
    'installable': True,
    'application': False,
    'auto_install': False,
    # any module necessary for this one to work correctly
    'depends': ['base', 'web_domain_field'],

    # always loaded
    'data': [
        './views/municipio.xml',
        './views/ciudad.xml',
        './views/distrito_municipal.xml',
        './views/seccion.xml',
        './views/sector.xml',
        './security/ir.model.access.csv',
        './views/menu.xml'
    ],

}
