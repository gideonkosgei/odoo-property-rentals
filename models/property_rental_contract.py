from odoo import models, fields, api

class PropertyRentalContract(models.Model):
    _name = "property.rental.contract"
    _description = "Rental Contract"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Contract Reference", required=True, copy=False, readonly=True, default="New")
    tenant_id = fields.Many2one("res.partner", string="Tenant", required=True)
    property_id = fields.Many2one("property.property", string="Property", required=True)
    unit_id = fields.Many2one("property.unit", string="Unit", required=True)
    contract_start_date = fields.Date(string="Start Date", required=True)
    contract_end_date = fields.Date(string="End Date", required=True)
    rent_amount = fields.Monetary(string="Rent Amount", required=True)
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("expired", "Expired"),
            ("terminated", "Terminated"),
        ],
        string="Status",
        default="draft",
        tracking=True,
    )

    def action_confirm(self):
        """Confirm the contract"""
        self.write({"state": "active"})

    def action_terminate(self):
        """Terminate the contract"""
        self.write({"state": "terminated"})

    def action_expire(self):
        """Mark the contract as expired"""
        self.write({"state": "expired"})

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                        self.env["ir.sequence"].next_by_code("property.rental.contract") or "New"
                )
            return super(PropertyRentalContract, self).create(vals)
