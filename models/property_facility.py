# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyFacility(models.Model):
    """A class for the model property facilities to represent
    the related facilities for a property"""
    _name = 'property.facility'
    _description = 'Property Facility'
    _rec_name = 'facility'

    facility = fields.Text(string='Facility', required=True,
                           help='Facilities of the property')
