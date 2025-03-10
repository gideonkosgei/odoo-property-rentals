# -*- coding: utf-8 -*-
from odoo import fields, models,api

class PropertyNearbyAmenity(models.Model):
    _name = "property.nearby.amenity"
    _description = "Nearby Amenity"

    property_id = fields.Many2one("property.property", string="Property", required=True)
    nearby_amenity_type_id = fields.Many2one(
        "property.list.name",
        string="Type",
        required=True,
        domain="[('list_type_id', '=', 2), ('active', '=', True)]"
    )
    nearby_amenity_id = fields.Many2one(
        'property.list.value',
        string='Amenity',
        required=True,
        domain="[('list_name_id', '=', nearby_amenity_type_id), ('active', '=', True)]"
    )
    distance = fields.Float(
        string="Distance (KM)",
        required=True,
        help='The distance between the property and the amenity nearby in kilometers'
    )
    details = fields.Text(string='Details')

    @api.onchange("nearby_amenity_type_id")
    def _onchange_nearby_amenity_type_id(self):
        # Clears the amenity when amenity type changes
        self.nearby_amenity_id = False