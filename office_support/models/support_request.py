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
    urgent = fields.Boolean(default=False, string="Urgent")
