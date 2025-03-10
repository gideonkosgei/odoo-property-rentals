# -*- coding: utf-8 -*-
from odoo import fields, models,api
from odoo.exceptions import ValidationError

class PropertyLocalCondition(models.Model):
    _name = "property.local.condition"
    _description = "Local Condition"

    property_id = fields.Many2one("property.property", string="Property", required=True)

    category_id = fields.Many2one(
        "property.list.name",
        string="Condition",
        required=True,
        domain="[('list_type_id', '=', 5), ('active', '=', True)]"
    )
    local_condition_id = fields.Many2one(
        'property.list.value',
        string='Status',
        required=True,
        domain="[('list_name_id', '=', category_id), ('active', '=', True)]"
    )
    details = fields.Text(string='Details')

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self.local_condition_id = False

    @api.constrains('property_id', 'category_id')
    def _check_unique_property_category(self):
        for record in self:
            existing = self.search([
                ('property_id', '=', record.property_id.id),
                ('category_id', '=', record.category_id.id),
                ('id', '!=', record.id)  # Exclude the current record in case of updates
            ])
            if existing:
                raise ValidationError(
                    f"Local Conditions: '{record.category_id.name}' is already set for this property. "
                    "Please select a different condition or remove the existing one before adding a new entry."
                )






