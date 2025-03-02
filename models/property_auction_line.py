# -*- coding: utf-8 -*-
from odoo import fields, models


class PropertyAuctionLine(models.Model):
    """A class for the model property.auction.line to represent
    the participants of the auction"""
    _name = 'property.auction.line'
    _description = 'Auction Line'

    partner_id = fields.Many2one('res.partner', string='Bidder',
                                 help='The person who is bidding for the '
                                      'property')
    bid_time = fields.Datetime(string='Bid Time',
                               help='The date and time when the bid was placed')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id,
                                  required=True)
    bid_amount = fields.Monetary(string='bid amount',
                                 help='The amount which is bid')
    auction_id = fields.Many2one('property.auction',
                                 string='Property Auction',
                                 help='The corresponding property auction')
