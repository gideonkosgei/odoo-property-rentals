# -*- coding: utf-8 -*-
from odoo import fields, models


class RentalBill(models.Model):
    """A class for the model rental bills to represent
    the related bills for a property rental"""
    _name = 'rental.bill'
    _description = 'Rental Bill'

    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)
    bill_no = fields.Char(string='Bill Number', required=True,
                          help='The bill number of the bill')
    name = fields.Char(string='Name', required=True,
                       help='The name of the bill')
    amount = fields.Float(string='Amount',
                          help='The amount listed in the bill')
    rental_id = fields.Many2one('property.rental', string='Property Rental',
                                help='The corresponding Property Rental')
