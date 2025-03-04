# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyAmenity(models.Model):
    _name = 'property.amenity'
    _description = 'Property Amenity'

    name = fields.Char(string="Category", required=True)
    amenities = fields.Char(string="Category", required=True)

