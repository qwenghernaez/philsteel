# -*- coding: utf-8 -*-
{
    'name': "Philsteel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website'],

    # always loaded
    'data': [
        'security/philsteel_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/amrequests.xml',
        'data/ir_sequence_data.xml',
        'views/dailypas.xml',
        'views/weeklypas.xml',
        'views/department.xml',
        'views/inquiry.xml',
        'views/customerinquiry.xml',
        'views/product_view.xml',
        'views/website_materials.xml',
        'views/materials_installed.xml',
        'views/nica.xml',
        'views/contact.xml',
        'views/pisreport.xml',
        'views/positions.xml',
        'views/projects.xml',
        'views/session_board.xml',
        'views/ccaa.xml',
        'views/work_scope.xml',
        'views/project_manpower.xml',
        'views/rfamimages.xml',
        'views/project_activities.xml',
        'views/sheet.xml',
        'views/user_dashboard.xml',
        'views/cicf.xml',
        'views/iras.xml',
        'views/android_user.xml',
        'views/accomplishment_report.xml',
        'views/nica_report.xml',
        'views/philstee_report.xml',
        'views/menu.xml',
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}