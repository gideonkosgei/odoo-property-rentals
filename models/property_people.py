# -*- coding: utf-8 -*-
from odoo import fields, models,api

class PropertyPeople(models.Model):
    _name = "property.people"
    _description = "Property People"

    property_id = fields.Many2one("property.property", string="Property", required=True)

    category_id = fields.Many2one(
        "property.list.name",
        string="Category",
        required=True,
        domain="[('list_type_id', '=', 6), ('active', '=', True)]"
    )
    role_id = fields.Many2one(
        'property.list.value',
        string='Role',
        required=True,
        domain="[('list_name_id', '=', category_id), ('active', '=', True)]"
    )

    partner_id = fields.Many2one(
        "res.partner", string="Person/Company", required=True,
        help="The person or company associated with the property",
    )

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self.role_id = False






