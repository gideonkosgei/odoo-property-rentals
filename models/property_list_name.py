# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyListName(models.Model):

    _name = 'property.list.name'
    _description = 'List'

    list_type_id = fields.Many2one(comodel_name='property.list.type', string='list Type', required=True)
    name = fields.Text(string='List', required=True)
    active = fields.Boolean(string="Active", default=True)
