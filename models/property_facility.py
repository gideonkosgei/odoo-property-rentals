# -*- coding: utf-8 -*-
from odoo import fields, models,api

class PropertyFacility(models.Model):
    _name = "property.facility"
    _description = "Property Facility"

    property_id = fields.Many2one("property.property", string="Property", required=True)
    is_available = fields.Boolean(string="Available?", default=True)

    facility_type_id = fields.Many2one(
        "property.list.name",
        string="Facility Type",
        required=True,
        domain="[('list_type_id', '=', 1), ('active', '=', True)]"
    )
    facility_id = fields.Many2one('property.list.value', string='Facility', required=True,
                                  domain="[('list_name_id', '=', facility_type_id), ('active', '=', True)]")

    @api.onchange("facility_type_id")
    def _onchange_facility_type_id(self):
        # Clears the facility when facility type changes
        self.facility_id = False






