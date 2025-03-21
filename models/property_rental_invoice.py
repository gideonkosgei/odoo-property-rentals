from odoo import models, fields, api

class PropertyRentalInvoice(models.Model):
    _name = "property.rental.invoice"
    _description = "Rental Invoice"

    contract_id = fields.Many2one("property.rental.contract", string="Rental Contract", required=True)
    invoice_id = fields.Many2one("account.move", string="Invoice", readonly=True)
    due_date = fields.Date(string="Due Date", required=True)
    name = fields.Char(string="Invoice Number", required=True, copy=False, readonly=True, default="New")
    tenant_id = fields.Many2one("res.partner", string="Tenant", related="contract_id.tenant_id", store=True)
    invoice_date = fields.Date(string="Invoice Date", required=True, default=fields.Date.today)
    amount_due = fields.Float(string="Amount Due", required=True)


    state = fields.Selection(
        [("draft", "Draft"), ("sent", "Sent"), ("paid", "Paid"), ("cancelled", "Cancelled")],
        string="Status",
        default="draft",
    )

    def action_generate_invoice(self):
        """Create an invoice from the rental contract"""
        invoice_vals = {
            "partner_id": self.contract_id.tenant_id.id,
            "move_type": "out_invoice",
            "invoice_date_due": self.due_date,
            "invoice_line_ids": [
                (0, 0, {
                    "name": f"Rent for {self.contract_id.unit_id.name}",
                    "quantity": 1,
                    "price_unit": self.contract_id.rent_amount,
                    "account_id": self.env.company.property_account_receivable_id.id,
                })
            ],
        }
        invoice = self.env["account.move"].create(invoice_vals)
        self.write({"invoice_id": invoice.id, "state": "sent"})

    def action_mark_paid(self):
        """Mark invoice as paid"""
        self.write({"state": "paid"})

    def action_cancel(self):
        """Cancel the invoice"""
        self.write({"state": "canceled"})
