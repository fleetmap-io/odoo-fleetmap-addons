import logging
import os
import firebase_admin
from odoo import api, fields, models
from firebase_admin import firestore

default_app = firebase_admin.initialize_app()
db = firestore.client()

endpoint = os.environ.get('MIDDLEWARE_URL')

_logger = logging.getLogger(__name__)

class FSMOrder(models.Model):
    _inherit = "fsm.order"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        _logger.info("vals: %s", vals)
        doc_ref = db.collection(u'jobs').document(vals['name'])
        new_dict = {}
        for key, value in vals.items():
            if hasattr(value, '__len__'):
                new_dict[key] = str(value)
            else:
                new_dict[key] = value
        doc_ref.set(new_dict)
        _logger.info("res %s", res)
        return res

    def unlink(self):
        doc_ref = db.collection(u'jobs').document(self.name)
        doc_ref.delete()
        super().unlink()

    def write(self, vals):
        _logger.info('%s write %s', self, vals)
        res = super(FSMOrder, self).write(vals)
        return res

    @api.onchange("location_id")
    def onchange_location_id(self):
        res = super().onchange_location_id()
        return res
