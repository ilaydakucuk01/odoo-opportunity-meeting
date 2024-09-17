from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # One-to-many relationship for opportunity meetings
    opportunity_meeting_ids = fields.One2many('opportunity.meeting', 'opportunity_id', string='Opportunity Meetings')
