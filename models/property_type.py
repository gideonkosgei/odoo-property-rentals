# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Property Type'

    name = fields.Text(string='Property Type', required=True)
    active = fields.Boolean(string="Active", default=True)

