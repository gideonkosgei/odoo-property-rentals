# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PropertyAreaMeasure(models.Model):
    _name = 'property.area.measure'
    _description = 'Unit Area Measurement'

    name = fields.Char(string='Section', required=True,
                       help='Name of the room or section')
    length = fields.Float(string='Length(ft)', help='The length of the room')
    width = fields.Float(string='Width(ft)', help='The width of the room')
    height = fields.Float(string='Height(ft)', help='The height of the room')
    area = fields.Float(string='Area(ft²)', compute='_compute_area',
                        help='The total area of the room')
    unit_id = fields.Many2one('property.unit', string='Unit')

    @api.depends('length', 'width', 'height')
    def _compute_area(self):
        """ The total area of the room for each record is calculated """
        for rec in self:
            rec.area = rec.length * rec.width
