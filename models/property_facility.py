# -*- coding: utf-8 -*-
from odoo import fields, models,api
from odoo.exceptions import ValidationError

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
    details = fields.Text(string='Details')

    @api.onchange("facility_type_id")
    def _onchange_facility_type_id(self):
        # Clears the facility when facility type changes
        self.facility_id = False

    @api.constrains('property_id', 'facility_id')
    def _check_unique_property_facility(self):
        for record in self:
            existing = self.search([
                ('property_id', '=', record.property_id.id),
                ('facility_id', '=', record.facility_id.id),
                ('id', '!=', record.id)  # Exclude the current record in case of updates
            ])
            if existing:
                raise ValidationError(
                    f"Facilities: '{record.facility_id.name}' is already set for this property. "
                    "Please select a different Facility or remove the existing one before adding a new entry."
                )






