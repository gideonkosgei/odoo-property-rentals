# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyNearbyAmenity(models.Model):
    _name = "property.nearby.amenity"
    _description = "Nearby Amenity"

    property_id = fields.Many2one("property.property", string="Property", required=True)
    list_name_id = fields.Many2one("property.list.name", string="Amenity type", required=True,domain=[("active", "=", True)])
    list_value_id = fields.Many2one('property.list.value', string='Amenity', required=True,
                                  domain="[('list_name_id', '=', list_name_id), ('active', '=', True)]")
    distance = fields.Float(string="Property Distance (KM)", required=True,
                             help='The distance between the property and the amenity nearby in kilometers')




