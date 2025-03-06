# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyListType(models.Model):

    _name = 'property.list.type'
    _description = 'List Type'

    name = fields.Text(string='List Type', required=True)
    active = fields.Boolean(string="Active", default=True)
