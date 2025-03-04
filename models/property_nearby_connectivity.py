# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyNearbyConnectivity(models.Model):
    """A class for the model property.nearby.connectivity to represent
    the nearby connectives for a property"""
    _name = 'property.nearby.connectivity'
    _description = 'Property Nearby Connectivity'

    name = fields.Char(string="Name", required=True,
                       help='Name of the nearby connectivity for the property')
    direction = fields.Selection(
        [
            ("city_center", "City Center"),
            ("day_care", "Day Care"),
            ("kindergarten", "Kindergarten"),
            ("primary_school", "Primary School"),
            ("high_school", "High School"),
            ("tertiary_institution", "College, University"),
            ("health_center", "Hospital, Pharmacy"),
            ("shopping_center", "Malls, Supermarket"),
            ("public_services", "Police Station, Fire Station, Government office"),
            ("recreational Areas", "Park, Gym, Bar, Sports Complex"),
        ],
        string="Furnishing",
        help="Whether the residence is fully furnished or partially/half "
             "furnished or not at all furnished",
    )
    # direction = fields.Selection([('north', 'North'), ('south', 'South'),
    #                               ('east', 'East'), ('west', 'West')],
    #                              string='Direction',
    #                              help='To which direction is the nearby '
    #                                   'connectivity')
    kilometer = fields.Float(string="Kilometer", required=True,
                             help='The distance between the property and '
                                  'nearby connectivity in kilometers')
    property_id = fields.Many2one('property.property',
                                  string="Property Name",
                                  help='The related property')
