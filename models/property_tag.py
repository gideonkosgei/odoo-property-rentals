# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyTag(models.Model):
    """A class for the model property tags to represent
    the related tags for a property"""
    _name = 'property.tag'
    _description = 'Property Tag'
    _rec_name = 'tag'

    tag = fields.Char(string='Tag', required=True, help='Name of the tag')
