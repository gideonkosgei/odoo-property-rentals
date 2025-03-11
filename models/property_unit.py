# -*- coding: utf-8 -*-
from odoo import fields, models,api

class PropertyUnit(models.Model):
    _name = "property.unit"
    _description = "Property Unit"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Unit Name", required=True, help="The name or number of the unit (e.g., A101, Office 3B)")
    property_id = fields.Many2one("property.property", string="Property", required=True,
                                  help="The property this unit belongs to")
    # unit_type_category_id = fields.Many2one("property.list.name", string="Unit Category",
    #                                         required=True, domain="[('list_type_id', '=', 2), ('active', '=', True)]")
    # unit_type_id = fields.Many2one("property.list.value", string="Unit Type", required=True,
    #                                domain="[('list_name_id', '=', unit_type_category_id), ('active', '=', True)]")

    floor_number = fields.Integer(string="Floor Number", help="The floor where the unit is located")
    area_size = fields.Float(string="Size (sqm)", help="Total area of the unit in square meters")

    bedrooms = fields.Integer(string="Bedrooms", help="Number of bedrooms (if residential)")
    bathrooms = fields.Integer(string="Bathrooms", help="Number of bathrooms")

    # tenant_id = fields.Many2one("res.partner", string="Tenant", help="The tenant currently occupying this unit")
    is_occupied = fields.Boolean(string="Occupied?", compute="_compute_occupancy_status", store=True)

    rent_price = fields.Float(string="Rent Price", help="Rental price per month or lease term")
    # lease_id = fields.Many2one("property.lease", string="Lease Contract",
    #                            help="The lease contract associated with this unit")

    status = fields.Selection(
        [("available", "Available"), ("occupied", "Occupied"), ("under_maintenance", "Under Maintenance")],
        string="Status",
        default="available",
    )

    image_ids = fields.One2many(
        "property.unit.image", "unit_id", string="Unit Images"
    )

    utility_meter_ids = fields.One2many("property.unit.utility.meter", "unit_id", string="People")

    # Parking
    # parking_space_id = fields.Many2one("property.parking", string="Assigned Parking Space",
    #                                    help="Assigned parking spot for this unit")

    # @api.depends("tenant_id")
    # def _compute_occupancy_status(self):
    #     for record in self:
    #         record.is_occupied = bool(record.tenant_id)
