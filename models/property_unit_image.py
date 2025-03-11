# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyUnitImages(models.Model):
    _name = 'property.unit.image'
    _description = 'Unit Images'

    name = fields.Char(string='Name', required=True,
                       help='Name for the given image')
    description = fields.Text(string='Description',
                              help='A brief description of the image given')
    image = fields.Binary(string='Image', required=True,
                          help='The properties image')

    unit_id = fields.Many2one('property.unit',
                                  string='Unit',
                                  help='Related property')



