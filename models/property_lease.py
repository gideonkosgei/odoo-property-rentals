# -*- coding: utf-8 -*-
from odoo import fields, models

class PropertyLease(models.Model):
    _name = "property.lease"
    _description = "Lease Contract"

    name = fields.Char(string="Lease Reference", required=True, copy=False, default=lambda self: _('New'))
    unit_id = fields.Many2one("property.unit", string="Unit", required=True, help="The property unit under this lease")
    tenant_id = fields.Many2one("res.partner", string="Tenant", required=True, help="Tenant leasing the unit")
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    rent_amount = fields.Float(string="Rent Amount", required=True)
    payment_frequency = fields.Selection(
        [("monthly", "Monthly"), ("quarterly", "Quarterly"), ("annually", "Annually")],
        string="Payment Frequency",
        default="monthly",
        required=True,
    )
    security_deposit = fields.Float(string="Security Deposit", help="Security deposit amount")
    status = fields.Selection(
        [("active", "Active"), ("terminated", "Terminated"), ("expired", "Expired")],
        string="Lease Status",
        default="active",
    )

    @api.model
    def create(self, vals):
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code("property.lease") or _("New")
        return super(PropertyLease, self).create(vals)
