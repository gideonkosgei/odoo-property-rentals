# -*- coding: utf-8 -*-
from odoo import fields, models,api

class PropertyUnitUtilityMeter(models.Model):
    _name = "property.unit.utility.meter"
    _description = "Utility Meter"

    unit_id = fields.Many2one("property.unit", string="Unit", required=True)

    category_id = fields.Many2one(
        "property.list.name",
        string="Category",
        required=True,
        domain="[('list_type_id', '=', 7), ('active', '=', True)]"
    )
    utility_id = fields.Many2one(
        'property.list.value',
        string='Utility',
        required=True,
        domain="[('list_name_id', '=', category_id), ('active', '=', True)]"
    )
    meter_number = fields.Char(string='Meter Number')

    provider_id = fields.Many2one(
        'property.list.value',
        string='Provider',
        required=True,
        domain="[('list_name_id', 'in', [50, 51, 52, 53]), ('active', '=', True)]"
    )

    details = fields.Text(string='Details')

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self.utility_id = False






