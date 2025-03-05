# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyDynamicAttribute(models.Model):
    _name = 'property.dynamic.attribute'
    _description = 'Property Dynamic Attributes'

    property_id = fields.Many2one("property.property", string="Property", required=True, ondelete="cascade")
    attribute_key = fields.Char(string="Attribute Key", required=True, help="The name of the attribute")
    attribute_value = fields.Char(string="Attribute Value", required=True, help="The value of the attribute")
    notes = fields.Text(string='Notes', help='A brief description attribute')



