# -*- coding: utf-8 -*-
from odoo import fields, models
class PropertyParking(models.Model):
    _name = "property.parking"
    _description = "Parking Space"

    name = fields.Char(string="Parking Spot", required=True, help="Parking space identifier (e.g., P1, P2, Basement 3-45)")
    property_id = fields.Many2one("property.property", string="Property", required=True, help="The property this parking spot belongs to")
    is_reserved = fields.Boolean(string="Reserved?", default=False, help="Indicates if the parking space is reserved")
    assigned_unit_id = fields.Many2one("property.unit", string="Assigned Unit", help="The unit assigned to this parking spot")
