from odoo import api, fields, models, _

class Property(models.Model):
    """A class for the model property to represent the property"""

    _name = "property.property"
    _description = "Property"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name", required=True, copy=False, help="Name of the Property",tracking=True
    )
    code = fields.Char(
        string="Reference",
        readonly=True,
        copy=False,
        default=lambda self: _("New"),
        help="Sequence/code for the property",
    )

    property_type_id = fields.Many2one(
        "property.list.name",
        string="Property Type",
        required=True,
        domain="[('list_type_id', '=', 4), ('active', '=', True)]",
        tracking=True
    )
    property_structure_id = fields.Many2one(
        'property.list.value',
        string='Building Structure',
        required=True,
        domain="[('list_name_id', '=', property_type_id), ('active', '=', True)]",
        tracking=True
    )

    is_multi_story = fields.Boolean(
        string="Multi-Story",
        store=True
    )
    total_stories = fields.Integer(
        string="Total Stories",
        store=True
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("available", "Available"),
            ("rented", "Rented"),
            ("sold", "Sold"),
            ("maintenance", "Maintenance"),
        ],
        required=True,
        string="Status",
        tracking = True,
        default="draft",
        help="* The 'Draft' status is used when the property is in draft.\n"
        "* The 'Available' status is used when the property is "
        "available or confirmed\n"
        "* The 'Rented' status is used when the property is rented.\n"
        "* The 'sold' status is used when the property is sold.\n",
    )

    location = fields.Char(string="Location", help="The location of the property", tracking=True)
    street = fields.Char(string="Street", required=True, help="The street name", tracking=True)
    street2 = fields.Char(string="Street2", help="The street2 name", tracking=True)
    zip = fields.Char(string="Zip", change_default=True, help="Zip code for the place", tracking=True)
    city = fields.Char(string="City", help="The name of the city", tracking=True)
    country_id = fields.Many2one(
        "res.country",
        string="Country",
        ondelete="restrict",
        required=True,
        help="The name of the country", tracking=True,
        readonly=True,
        default = lambda self: self.env.company.country_id,
    )

    state_id = fields.Many2one(
        "res.country.state",
        string="State",
        ondelete="restrict",
        tracking=True,
        domain="[('country_id', '=?', country_id)]",
        help="The name of the state"
    )

    image = fields.Binary(string="Image", help="Image of the property")
    neighbourhood = fields.Char(string="Neighbourhood", tracking=True)
    location_url = fields.Char(string="Location Link", help="Enter a Google Maps or OpenStreetMap link", tracking=True)
    landmark = fields.Text(
        string="Nearby Landmarks",
        help="Add notable feature of the landscape or a structure that stands out and is easily recognizable",
        tracking=True
    )

    main_road = fields.Char(string="Main Road",  help="Main road to the property", tracking=True)

    # Insurance Details
    insurance_policy_number = fields.Char(string="Policy Number", help="Insurance policy Number", tracking=True)
    insurance_provider = fields.Char(string="Insurance Provider", help="Name of the company providing the insurance",
                                     tracking=True)
    insurance_coverage = fields.Text(string="Coverage Details", help="Description of what the insurance policy covers",
                                     tracking=True)

    owner_id = fields.Many2one(
        "res.partner", string="Owner", required=True, help="The owner of the property", tracking=True
    )
    ownership_type = fields.Selection(
        [
            ("sole", "Sole Ownership"),
            ("joint", "Joint Ownership"),
            ("corporate", "Corporate Ownership"),
        ],
        string="Ownership Type",
        required=True,
        tracking=True,
        help="Type of ownership: Sole, Joint, or Corporate"
    )

    legal_representative = fields.Many2one(
        "res.partner", string="Representative", help="Name of the legal representative or property manager",
        tracking=True
    )
    disclosure = fields.Text(
        string="Ownership Disclosure",
        help="Examples of Disclosures.\n"
             "- Financial Obligations': Who is responsible for property taxes, maintenance, and mortgage payments? \n"
             "- Sale Conditions':  Can one owner sell their share without the other’s consent? \n"
             "- Legal Restrictions': legal agreements or restrictions affecting the property? \n"
             "- Dispute Resolution': Handling of conflicts between owners? \n"
             "- Encumbrances': loans or liens against the property? \n",
        tracking=True
    )
    local_condition_ids = fields.One2many("property.local.condition", "property_id", string="Local Condition")
    document_ids = fields.One2many("property.document", "property_id", string="Document Attachments")
    facility_ids = fields.One2many("property.facility", "property_id", string="Facilities")
    nearby_amenity_ids = fields.One2many("property.nearby.amenity", "property_id", string="Nearby Amenities")
    dynamic_attribute_ids = fields.One2many("property.dynamic.attribute", "property_id", string="Dynamic Attributes")
    people_ids = fields.One2many("property.people", "property_id", string="People")
    unit_ids = fields.One2many("property.unit", "property_id", string="unit")
    property_image_ids = fields.One2many(
        "property.image", "property_id", string="Property Images", tracking=True
    )
    description = fields.Text(
        string="Description", help="A brief description about the property", tracking=True
    )

    #orphans
    company_id = fields.Many2one(
        "res.company",
        string="Property Management Company",
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        "res.currency", string="Currency", related="company_id.currency_id", tracking=True
    )

    total_floor = fields.Integer(
        string="Total Floor",
        default=1,
        help="The total number of floor in " "the property",
    )

    sale_rent = fields.Selection(
        [
            ("for_sale", "For Sale"),
            ("for_tenancy", "For Tenancy"),
            ("for_auction", "For Auction"),
        ],
        string="Sale | Rent",
        # required=True,
    )
    unit_price = fields.Monetary(
        string="Sales Price", help="Selling price of the Property."
    )
    sale_id = fields.Many2one(
        "property.sale",
        string="Sale Order",
        help="The corresponding property sale",
        tracking=True,
    )
    rent_month = fields.Monetary(
        string="Rent/Month", help="Rent price per month", tracking=True
    )

    #total_floors_in_building (Integer) – Total floors in the building

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("code", "New") == "New":
                vals["code"] = (
                        self.env["ir.sequence"].next_by_code("property.property") or "New"
                )
            res = super(Property, self).create(vals)
            return res

    def _compute_total_sq_feet(self):
        """Calculates the total square feet of the property"""
        for rec in self:
            rec.total_sq_feet = sum(rec.mapped("area_measurement_ids").mapped("area"))

    def action_get_map(self):
        """Redirects to Google Maps using the provided location URL"""
        for record in self:
            if record.location_url:
                return {
                    "type": "ir.actions.act_url",
                    "name": "View Map",
                    "target": "new",  # Opens in a new tab
                    "url": record.location_url,
                }
            else:
                return {
                    "warning": {
                        "title": "Missing Location",
                        "message": "No Google Maps URL provided for this property.",
                    }
                }

    def action_available(self):
        """Set the state to available"""
        self.state = "available"

    def action_property_sale_view(self):
        """View Sale order Of the Property"""
        return {
            "name": "Property Sale: " + self.code,
            "view_mode": "list,form",
            "res_model": "property.sale",
            "type": "ir.actions.act_window",
            "res_id": self.sale_id.id,
        }

    def action_property_rental_view(self):
        """View rental order Of the Property"""
        return {
            "name": "Property Rental: " + self.code,
            "view_mode": "list,form",
            "res_model": "property.rental",
            "type": "ir.actions.act_window",
            "domain": [("property_id", "=", self.id)],
        }

    @api.onchange("property_type_id")
    def _onchange_property_type_id(self):
        #Clears the building structure when property type changes
        self.property_structure_id = False

    def action_add_unit(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Units",
            "res_model": "property.unit",
            "view_mode": "form",
            "domain": [("property_id", "=", self.id)],
            "context": {"default_property_id": self.id},
        }

    def action_view_units(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Units",
            "res_model": "property.unit",
            "view_mode": "list,form",
            "domain": [("property_id", "=", self.id)],
            "context": {"default_property_id": self.id},
        }

    unit_count = fields.Integer(string="Units", compute="_compute_unit_count", store=True)

    @api.depends("unit_ids")
    def _compute_unit_count(self):
        for record in self:
            record.unit_count = len(record.unit_ids)