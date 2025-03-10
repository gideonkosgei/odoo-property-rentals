# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyImages(models.Model):
    """A class for the model property image to represent
    the related images for a property"""
    _name = 'property.image'
    _description = 'Property Images'

    name = fields.Char(string='Name', required=True,
                       help='Name for the given image')
    description = fields.Text(string='Description',
                              help='A brief description of the image given')
    image = fields.Binary(string='Image', required=True,
                          help='The properties image')

    property_id = fields.Many2one('property.property',
                                  string='Property',
                                  help='Related property')
