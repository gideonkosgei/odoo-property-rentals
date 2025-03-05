# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyDocumentAttachment(models.Model):
    _name = 'property.document.attachment'
    _description = 'Property Document Attachment'

    property_id = fields.Many2one('property.property',string="Property Name",help='The related property')
    document_category_id = fields.Many2one("property.document.category", string="Category",
                                           domain=[("active", "=", True)], required=True)
    document_id = fields.Many2one('property.document', string='Document', required=True,
                                  domain="[('document_category_id', '=', document_category_id), ('active', '=', True)]")

    document_file = fields.Binary(string="Upload", required=True)

    document_filename = fields.Char(string="File", help="Automatically filled when file is uploaded")
    document_description = fields.Text(string='Notes',help='A brief description of the document')
