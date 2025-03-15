# -*- coding: utf-8 -*-
from odoo import fields, models,api
from odoo.exceptions import ValidationError

class PropertyUnitFurnish(models.Model):
    _name = "property.unit.furnish"
    _description = "Furniture & Appliance"

    unit_id = fields.Many2one("property.unit", string="Unit", required=True)

    section_id = fields.Many2one(
        "property.list.name",
        string="Section",
        required=True,
        domain="[('list_type_id', '=', 10), ('active', '=', True)]"
    )
    item_id = fields.Many2one(
        'property.list.value',
        string='Item',
        required=True,
        domain="[('list_name_id', '=', section_id), ('active', '=', True)]"
    )
    quantity = fields.Integer(string='Quantity', required=True)
    cost = fields.Float(string='Cost')
    details = fields.Text(string='Details')
    image = fields.Binary(string='Image', help='The properties image')
    image_filename = fields.Char(string="File")

    @api.onchange("section_id")
    def _onchange_section_id(self):
        self.item_id = False

    @api.constrains('quantity', 'cost')
    def _check_positive_values(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError("Quantity must be 0 or greater.")
            if record.cost < 0:
                raise ValidationError("Cost must be 0 or greater.")




