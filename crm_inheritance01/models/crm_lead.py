# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Remove @api.multi as it's deprecated and removed in Odoo 13+
    def write(self, vals):
        # Check if 'stage_id' is one of the fields being updated
        if 'stage_id' in vals:
            new_stage_id = vals['stage_id'] # Get the ID of the new stage

            # 'self' here is already a recordset (can contain one or more records)
            for lead in self: # Iterate through each lead in the recordset
                old_stage = lead.stage_id # Get the current stage of the lead
                new_stage = self.env['crm.stage'].browse(new_stage_id) # Get the record for the new stage

                # Check if both old and new stages exist and if the new stage's sequence
                # is less than the old stage's sequence (indicating a backward move).
                if old_stage and new_stage and new_stage.sequence < old_stage.sequence:
                    raise UserError(_("You cannot drag a lead backward to a previous stage!"))

        # If no backward drag is detected, or if 'stage_id' was not updated,
        # call the original write method of the crm.lead model.
        return super(CrmLead, self).write(vals)