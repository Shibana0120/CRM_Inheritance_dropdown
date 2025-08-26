{
    'name': "CRM Restrict Kanban Drag",
    'summary': """
        Prevents CRM pipeline stages from being dragged backward in Kanban view.""",
    'description': """
        This module inherits the CRM Lead model and modifies the Kanban view behavior
        to ensure that once a lead is moved to a new stage, it cannot be dragged
        back to a previous stage.
    """,
    'author': "Your Name",
    'website': "http://www.yourwebsite.com",
    'category': 'Sales/CRM',
    'version': '1.0',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}