from openerp import models, fields

import logging
logger = logging.getLogger(__name__)

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

    def write(self, cr, uid ,ids, vals, context=None):
        logger.debug('Write mro_order: making sure date_planned is dirty if no event yet')

        # If there is no event yet, make sure vals contains date_planned
        for order in self.browse(cr, uid, ids):
            if not order.reminder_event_id:
                vals['date_planned'] = order.date_planned

        return super(mro_order, self).write(
            cr, uid, ids, vals, context=context)
