from odoo import fields, models, api


class SupportRequest(models.Model):
    _name = 'office.support.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "office support request"

    name = fields.Many2one('hr.employee', string="Name")
    department_id = fields.Many2one(string="Department", related="name.department_id")
    mobile_phone = fields.Char(related="name.mobile_phone", string="Mobile")
    company_id = fields.Many2one(related="name.company_id", string="Company")
    support_description = fields.Text(string="Description")
    requested_date = fields.Datetime(default=fields.Datetime.now, string="Requested Date")
    urgent = fields.Boolean(default=False, string="Urgent")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'Requested'),
        ('progress', 'Progress'),
        ('done', 'Done'),
    ], default='draft', track_visibility='onchange')
