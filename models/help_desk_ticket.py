from odoo import api, fields, models, _


class HelpDeskTicket(models.Model):
    _name = 'help.desk.ticket'
    _description = 'Help Desk Ticket'
    _rec_name = 'title'

    title = fields.Char(string="Title", size=100,
                        help="Brief title of the ticket", required=True, translate=True)
    ticket_number = fields.Char(string="Tickt Code",help="Unique ticket code (auto-generated)", 
                                required=True, readonly=True, copy=False)
    problem_description = fields.Char(string="Description", 
                                      help="Full description of the problem", required=True)
    solution = fields.Char(string="Solution", help="Solution provided by support agent")
    priority = fields.Selection(selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                                string="Priority", default='medium', required=True, translate=True)
    state = fields.Selection(selection=[('new', 'New'), ('in_progress', 'Progress'), ('done', 'Done'),
                                        ('closed', 'Closed'),], string="Status",
                            default='new', required=True, translate=True)
    customer_id = fields.Many2one('res.partner', string="Customer Name", required=True,
                                  help='The customer who reported the issue')
    assignee_id = fields.Many2many('res.users', string="Assigned To", 
                                   help='Support agent responsible for this ticket')
    days_open = fields.Integer(string='Days Open', compute="_comput_days_open")
    active = fields.Boolean(default=True, help='Set to False to archive the ticket')