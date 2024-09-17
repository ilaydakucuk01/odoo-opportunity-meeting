from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # One-to-many relationship for supplier meetings
    supplier_meeting_ids = fields.One2many('opportunity.meeting.note', 'supplier_id', string='Supplier Meetings')
