# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        #
        return res

    @api.onchange("location_id")
    def onchange_location_id(self):
        res = super().onchange_location_id()
        if self.location_id:
        #self.create_geometry()
        return res
