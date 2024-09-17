from odoo import models, fields, api


# inherits calendar event
class OpportunityMeeting(models.Model):
    _name = 'opportunity.meeting'
    _inherits = {'calendar.event': 'meeting_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Opportunity Meeting'

    opportunity_id = fields.Many2one('crm.lead', string='Opportunity')
    note_lines = fields.One2many('opportunity.meeting.note', 'opportunity_meeting_id', string='Meeting Notes')


class OpportunityMeetingNote(models.Model):
    _name = 'opportunity.meeting.note'
    _description = 'Opportunity Meeting Note'

    name = fields.Char(string='Note', required=True)
    # Many2one relation to opportunity.meeting model
    opportunity_meeting_id = fields.Many2one('opportunity.meeting', string='Opportunity Meeting', ondelete='cascade')
    # Many2one relation to res.partner model
    supplier_id = fields.Many2one('res.partner', string='Supplier')
