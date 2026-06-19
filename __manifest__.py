{
    'name': 'Help Desk Custom',
    'version': '0.1',
    'author': 'Aliasghar',
    'depends': ['base', 'mail', 'calendar', 'contacts'],
    'category': 'Services/Helpdesk',
    'summary': "Helpdesk ticketing with priorities, assignments, and PDF reports",
    'data':[
        'security/ir.model.access.csv',
        'data/help_desk_ticket.xml',
        'views/help_desk_ticket.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
}