# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyFacility(models.Model):
    _name = "property.facility"
    _description = "Property Facility"

    property_id = fields.Many2one("property.property", string="Property", required=True)
    list_name_id = fields.Many2one("property.list.name", string="Facility type", required=True,domain=[("active", "=", True)])
    list_value_id = fields.Many2one('property.list.value', string='Facility', required=True,
                                  domain="[('list_name_id', '=', list_name_id), ('active', '=', True)]")

    is_available = fields.Boolean(string="Available?", default=False)


