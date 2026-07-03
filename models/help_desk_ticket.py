from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date


class HelpDeskTicket(models.Model):
    _name = 'help.desk.ticket'
    _description = 'Help Desk Ticket'
    _rec_name = 'title'

    title = fields.Char(string="Title", size=100,
                        help="Brief title of the ticket", required=True, translate=True)
    ticket_number = fields.Char(string="Tickt Code",help="Unique ticket code (auto-generated)", 
                                readonly=True, copy=False)
    problem_description = fields.Text(string="Description", translate=True,
                                      help="Full description of the problem", required=True)
    solution = fields.Text(string="Solution",translate=True,
                           help="Solution provided by support agent")
    priority = fields.Selection(selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                                string="Priority", default='medium', required=True)
    state = fields.Selection(selection=[('new', 'New'), ('in_progress', 'Progress'), ('done', 'Done'),
                                        ('closed', 'Closed'),], string="Status",
                            default='new', required=True, group_expand="_group_expand_state")
    customer_id = fields.Many2one('res.partner', string="Customer Name", required=True,
                                  help='The customer who reported the issue')
    assignee_id = fields.Many2one('res.users', string="Assigned To", 
                                   help='Support agent responsible for this ticket',
                                   domain="[('share', '=', False)]")
    days_open = fields.Integer(string='Days Open', compute="_compute_days_open")
    active = fields.Boolean(default=True, help='Set to False to archive the ticket')
    notes = fields.Html('Notes')

    @api.depends('state')
    def _compute_days_open(self):
        for ticket in self: 
            if ticket.state in ('done', 'closed'):
                ticket.days_open = 0
            elif ticket.create_date:
                delta = date.today() - ticket.create_date.date()
                ticket.days_open = delta.days
            else:
                ticket.days_open = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ticket_number'] = self.env['ir.sequence'].next_by_code('help.desk.ticket') or _('New')
        return super().create(vals_list)

    #Action buttons to change status
    def action_new(self):
        self.state = 'new'
    def action_progress(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def action_close(self):
        self.state = 'closed'

    @api.model
    def _group_expand_state(self, stages, domain):
        desired_order = ['new', 'in_progress', 'done', 'closed']
        all_states = dict(self._fields['state'].selection).keys()
        
        result = []
        for state in desired_order:
            if state in all_states:
                result.append(state)
        return result
    
