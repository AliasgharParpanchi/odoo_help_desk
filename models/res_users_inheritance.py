from odoo import api, fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    subordinate_ids = fields.Many2many(
        'res.users',
        'helpdesk_user_supervisor_rel',
        'supervisor_id',
        'subordinate_id',
        string='Subordinates',
        help='Users that this supervisor can manage'
    )