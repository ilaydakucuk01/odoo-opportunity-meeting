# -*- coding: utf-8 -*-
{
    'name': "opportunity meeting",

    'summary': """
        Track meetings related to opportunities and suppliers""",

    'description': """
        This module allows tracking of meetings related to opportunities and suppliers
    """,

    'author': "ilayda kucuk",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'crm', 'calendar'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/opportunity_meeting_view.xml',
        'views/res_partner.xml',
        'reports/opportunity_meeting_report.xml',
    ],
}
