# -*- coding: utf-8 -*-
{
    'name': "Floristeria",

    'summary': """
       Floristeria, 
        This module add sale and invoice legal letter report,replace contacts to make them apart""",

    'description': """
        This module add sale and invoice legal letter report.
        Change res partner contacts.
        
    """,

    'author': "Caonabo Mena Perez",
    'website': "http://billsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sale_management', 'account', 'web_domain_field'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_contacts.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'report/card_media_papel_format.xml',
        'report/sale_order_media_carta.xml',
        'report/report_invoice_media_carta.xml',
        'report/report.xml',
        # 'report/sale_order_test.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'application': True,
}
