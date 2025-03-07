# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyListValue(models.Model):
    _name = 'property.list.value'
    _description = 'List Value'
    _rec_name = 'name'

    list_name_id = fields.Many2one(comodel_name='property.list.name', string='List',required=True)
    name = fields.Text(string='List Value', required=True)
    active = fields.Boolean(string="Active", default=True)
    list_type_id = fields.Many2one(
        'property.list.type', string="List Type", related='list_name_id.list_type_id', store=True
    )
