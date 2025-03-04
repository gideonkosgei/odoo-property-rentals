# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyFacility(models.Model):

    _name = 'property.facility'
    _description = 'Property Facility'
    _rec_name = 'facility'

    facility = fields.Text(string='Facility', required=True,
                           help='Facilities of the property')
    state = fields.Boolean(string="Active", default=True)
    category = fields.Selection(selection=[
        ('Basic Infrastructure', 'Basic Infrastructure'),
        ('Security & Safety', 'Security & Safety'),
        ('Transportation & Parking', 'Transportation & Parking'),
        ('Building & Accessibility', 'Building & Accessibility'),
        ('Utility & Maintenance', 'Utility & Maintenance'),
        ('Shared/Common Areas', 'Shared/Common Areas')
    ], string='Category'
    )
