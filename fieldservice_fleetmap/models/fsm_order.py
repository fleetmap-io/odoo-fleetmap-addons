# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import logging
import requests
import os

endpoint = os.environ.get('MIDDLEWARE_URL')

_logger = logging.getLogger(__name__)

class FSMOrder(models.Model):
    _inherit = "fsm.order"

    # Geometry Field
    shape = fields.GeoPoint("Coordinate")

    @api.model
    def create(self, vals):
        res = super().create(vals)
        _logger.info("vals: %s", vals)
        _logger.info("endpoint: %s", endpoint)
        _logger.info(requests.post(endpoint, vals))
        return res

    @api.onchange("location_id")
    def onchange_location_id(self):
        res = super().onchange_location_id()
        return res
