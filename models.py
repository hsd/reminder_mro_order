from openerp import models, fields


class mro_order(models.Model):
    _name = 'mro.order'
    _inherit = ['mro.order', 'reminder']

    # Reminders based on the planned date
    _reminder_date_field = 'date_planned'
    _reminder_description_field = 'description'

    # The user_id of the linked asset is the agenda we need to fill
    # This needs to have store=True so an actual column is made, because
    # reminder_base refers to this
    user_id = fields.Many2one(
        related='asset_id.user_id',
        readonly=True,
        store=True)
