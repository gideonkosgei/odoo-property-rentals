# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyStructure(models.Model):

    _name = 'property.structure'
    _description = 'Property Structure'
    _rec_name = 'property_structure'
    _order = "id"

    property_type_id = fields.Many2one(comodel_name='property.type', string='Property Type', required=True)
    property_structure = fields.Text(string='Property Structure', required=True)
    active = fields.Boolean(string="Active", default=True)

