# -*- coding: utf-8 -*-
{
    'name': "Internship Management",
    'summary': """
        Internship Management PT Tigernix Solutions Indonesia""",
    'description': """
        Internship Management for Students
    """,
    'version': '1.0',
    'category': 'Management',
    'author': 'TigernixERP',
    'website': 'https://www.tigernix.com',
    'depends': [
        'base',
        'mail',
        'report_xlsx',
    ],
    'data': [
        'data/data.xml',
        'views/student.xml',
        'views/staff.xml',
        'views/company.xml',
        'views/submission.xml',
        'views/intern_directory.xml',
        'views/internship_management_view.xml',
        'views/intern_tasklist.xml',
        'views/report_template.xml',
        'wizard/report_tasklist.xml',
        'report/report_submission.xml',
        'report/report_letter.xml',
        'report/report_all_tasklist.xml',
        'report/report.xml',
        'security/v11_internship_security.xml',
    ],
}