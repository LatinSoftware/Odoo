# -*- coding: utf-8 -*-
{
    'name': 'Mantenimientos',
    'category': 'Generic Modules',
    'version': '15.0.1.0.0',
    'author': 'Caonabo Mena',
    'summary': 'Modulo para la gestion de mantenimientos y garantias de productos',
    'images': ['static/description/banner.png'],
    'description': "Gestion de mantenimientos y garantias de productos.",
    'depends': [
        'maintenance',
        'sale_management',
        'l10n_do_accounting',
        'purchase'
    ],
    'data': [
       'views/maintenance_equipment_view.xml',
       'views/sale_order.xml',
       'views/request.xml',
       'report/sale_order_report.xml',
       'report/account_move_report.xml',
       'report/payment_report.xml',
       'report/purchase_order_report.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
