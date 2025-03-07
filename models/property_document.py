# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyDocument(models.Model):
    _name = 'property.document'
    _description = 'Property Document'

    property_id = fields.Many2one('property.property', string="Property Name", help='The related property')
    list_name_id = fields.Many2one(
        "property.list.name",
        string="Document Type",
        required=True,
        domain="[('list_type_id', '=', 3), ('active', '=', True)]"
    )
    list_value_id = fields.Many2one('property.list.value', string='Document', required=True,
                                    domain="[('list_name_id', '=', list_name_id), ('active', '=', True)]")

    document_file = fields.Binary(string="Upload", required=True)
    document_filename = fields.Char(string="File", help="Automatically filled when file is uploaded")
    document_description = fields.Text(string='Notes', help='A brief description of the document')
