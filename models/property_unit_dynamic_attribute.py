# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyUnitDynamicAttribute(models.Model):
    _name = 'property.unit.dynamic.attribute'
    _description = 'Unit Dynamic Attributes'

    unit_id = fields.Many2one("property.unit", string="unit", required=True, ondelete="cascade")
    attribute_key = fields.Char(string="Attribute Key", required=True, help="The name of the attribute")
    attribute_value = fields.Char(string="Attribute Value", required=True, help="The value of the attribute")
    notes = fields.Text(string='Notes', help='A brief description attribute')



