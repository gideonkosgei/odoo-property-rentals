# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyDocumentCategory(models.Model):
    _name = 'property.document.category'
    _description = 'Property Document Category'

    name = fields.Char(string="Category Name", help="Enter Document Category", required=True)
    active = fields.Boolean(string="Active", default=True)
