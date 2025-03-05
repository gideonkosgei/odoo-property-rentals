# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyDocument(models.Model):
    _name = 'property.document'
    _description = 'Property Document'

    document_category_id = fields.Many2one(comodel_name='property.document.category', string='Document Category', required=True)
    name = fields.Char(string="Document Name", help="", required=True)
    description = fields.Text(string='Description',help='A brief description of the document')
    active = fields.Boolean(string="Active", default=True)
