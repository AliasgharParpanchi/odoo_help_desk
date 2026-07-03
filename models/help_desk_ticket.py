from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date


class HelpDeskTicket(models.Model):
    _name = 'help.desk.ticket'
    _description = 'Help Desk Ticket'
    _rec_name = 'title'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string="Title", size=100, tracking=4,
                        help="Brief title of the ticket", required=True, translate=True)
    ticket_number = fields.Char(string="Tickt Code",help="Unique ticket code (auto-generated)", 
                                readonly=True, copy=False)
    problem_description = fields.Text(string="Description", translate=True,tracking=2,
                                      help="Full description of the problem", required=True)
    solution = fields.Text(string="Solution",translate=True,tracking=3,
                           help="Solution provided by support agent")
    priority = fields.Selection(selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                                string="Priority", default='medium', required=True, tracking=8)
    state = fields.Selection(selection=[('new', 'New'), ('in_progress', 'Progress'), ('done', 'Done'),
                                        ('closed', 'Closed'),], string="Status", tracking=1,
                            default='new', required=True, group_expand="_group_expand_state")
    customer_id = fields.Many2one('res.partner', string="Customer Name", required=True,
                                  help='The customer who reported the issue', tracking=6)
    assignee_id = fields.Many2one('res.users', string="Assigned To", 
                                   help='Support agent responsible for this ticket',
                                   domain="[('share', '=', False)]", tracking=5)
    days_open = fields.Integer(string='Days Open', compute="_compute_days_open")
    active = fields.Boolean(default=True, help='Set to False to archive the ticket',tracking=7)
    notes = fields.Html('Notes')
    close_date = fields.Datetime(
        string="Close Date",
        help="Date and time when ticket was closed",
        readonly=True,
        copy=False
    )

    @api.depends('state', 'create_date', 'close_date')
    def _compute_days_open(self):
        for ticket in self:
            if ticket.state in ('done', 'closed'):
                # Closed ticket: Use close_date
                if ticket.close_date:
                    delta = ticket.close_date - ticket.create_date
                    ticket.days_open = delta.days
                else:
                    # If close_date is empty (due to an error), use the present tense
                    delta = fields.Datetime.now() - ticket.create_date
                    ticket.days_open = delta.days
            else:
                # Open ticket: Calculate from the present time
                delta = fields.Datetime.now() - ticket.create_date
                ticket.days_open = delta.days

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ticket_number'] = self.env['ir.sequence'].next_by_code('help.desk.ticket') or _('New')
        return super().create(vals_list)


    @api.model
    def _group_expand_state(self, stages, domain):
        desired_order = ['new', 'in_progress', 'done', 'closed']
        all_states = dict(self._fields['state'].selection).keys()
        
        result = []
        for state in desired_order:
            if state in all_states:
                result.append(state)
        return result
    
