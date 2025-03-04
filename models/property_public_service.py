# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyPublicService(models.Model):
    _name = 'property.public.service'
    _description = 'Property Public Services & Infrastructure'

    category = fields.Char(string="Category", required=True)
    details = fields.Char(string="Details", required=True)
    state = fields.Boolean(string="Active", default=True)

