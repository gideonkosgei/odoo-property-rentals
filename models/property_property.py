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
        help="The name of the country", tracking=True
    )
    state_id = fields.Many2one(
        "res.country.state",
        string="State",
        ondelete="restrict",
        tracking=True,
        domain="[('country_id', '=?', country_id)]",
        help="The name of the state"
    )

    neighbourhood = fields.Char(string="Neighbourhood", tracking=True)
    location_url = fields.Char(string="Location Link", help="Enter a Google Maps or OpenStreetMap link", tracking=True)
    landmark = fields.Text(
        string="Nearby Landmarks",
        help="Add notable feature of the landscape or a structure that stands out and is easily recognizable",
        tracking=True
    )

    main_road = fields.Char(string="Main Road",  help="Main road to the property", tracking=True)

    company_id = fields.Many2one(
        "res.company",
        string="Property Management Company",
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        "res.currency", string="Currency", related="company_id.currency_id", tracking=True
    )
    image = fields.Binary(string="Image", help="Image of the property")


    description = fields.Text(
        string="Description", help="A brief description about the property", tracking=True
    )
    # responsible_id = fields.Many2one(
    #     "res.users",
    #     string="Responsible Person",
    #     help="The responsible person for " "this property",
    #     default=lambda self: self.env.user,
    # )
    type_residence = fields.Char(
        string="Type of Residence", help="The type of the residence"
    )
    total_floor = fields.Integer(
        string="Total Floor",
        default=1,
        help="The total number of floor in " "the property",
    )
    bedroom = fields.Integer(
        string="Bedrooms", help="Number of bedrooms in the property"
    )
    bathroom = fields.Integer(
        string="Bathrooms", help="Number of bathrooms in the property"
    )
    parking = fields.Integer(
        string="Parking",
        help="Number of cars or bikes that can be parked " "in the property",
    )
    furnishing = fields.Selection(
        [
            ("no_furnished", "Not Furnished"),
            ("half_furnished", "Partially Furnished"),
            ("furnished", "Fully Furnished"),
        ],
        string="Furnishing",
        help="Whether the residence is fully furnished or partially/half "
        "furnished or not at all furnished",
    )
    land_name = fields.Char(string="Land Name", help="The name of the land")
    land_area = fields.Char(
        string="Area In Hector", help="The area of the land in hector"
    )
    shop_name = fields.Char(string="Shop Name", help="The name of the shop")
    industry_name = fields.Char(string="Industry Name", help="The name of the industry")
    usage = fields.Char(
        string="Used For", help="For what purpose is this property used for"
    )

    property_image_ids = fields.One2many(
        "property.image", "property_id", string="Property Images", tracking=True
    )
    area_measurement_ids = fields.One2many(
        "property.area.measure", "property_id", string="Area Measurement"
    )
    total_sq_feet = fields.Float(
        string="Total Square Feet",
        compute="_compute_total_sq_feet",
        help="The total area square feet of the " "property",
    )
    property_tags = fields.Many2many(
        "property.tag", string="Property Tags", help="Tags for the property"
    )
    attachment_id = fields.Many2one("ir.attachment", string="Attachment")
    sale_rent = fields.Selection(
        [
            ("for_sale", "For Sale"),
            ("for_tenancy", "For Tenancy"),
            ("for_auction", "For Auction"),
        ],
        string="Sale | Rent",
        required=True,
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

    #Insurance Details
    insurance_policy_number = fields.Char(string="Policy Number", help="Insurance policy Number" , tracking=True)
    insurance_provider = fields.Char(string="Insurance Provider", help="Name of the company providing the insurance" , tracking=True)
    insurance_coverage = fields.Text(string="Coverage Details", help="Description of what the insurance policy covers" , tracking=True)

    owner_id = fields.Many2one(
        "res.partner", string="Owner",required=True, help="The owner of the property",tracking=True
    )
    ownership_type = fields.Selection(
        [
            ("sole", "Sole Ownership"),
            ("joint", "Joint Ownership"),
            ("corporate", "Corporate Ownership"),
        ],
        string="Ownership Type",
        required=True,
        tracking = True,
        help="Type of ownership: Sole, Joint, or Corporate"
    )

    legal_representative = fields.Many2one(
        "res.partner", string="Representative", help="Name of the legal representative or property manager", tracking=True
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

    security_level = fields.Selection([
        ('poor', 'Poor'),
        ('average', 'Average'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    ], string="Security Level",tracking=True)

    noise_level = fields.Selection([
        ('quiet', 'Quiet'),
        ('moderate', 'Moderate'),
        ('noisy', 'Noisy'),

    ], string="Noise Level",tracking=True)
    public_transport = fields.Selection([
        ('none', 'None'),
        ('limited', 'Limited'),
        ('moderate', 'Moderate'),
        ('good', 'Good'),
    ], string="Public Transport ", tracking=True)

    traffic_conditions = fields.Selection([
        ('light', 'Light'),
        ('moderate', 'Moderate'),
        ('heavy', 'Heavy')
    ], string="Traffic Conditions", tracking=True)

    air_quality = fields.Selection([
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('poor', 'Poor')
    ], string="Air Quality", tracking=True)

    road_conditions = fields.Selection([
        ('paved', 'Paved'),
        ('gravel', 'Gravel'),
        ('dirt', 'Dirt')
    ], string="Road Conditions", tracking=True)

    street_lighting = fields.Selection([
        ('well_lit', 'Well lit'),
        ('dim', 'Dim'),
        ('poor', 'Poor')
    ], string="Street Lighting", tracking=True)

    water_supply = fields.Selection([
        ('stable', 'Stable'),
        ('occasional_shortages', 'Occasional Shortages'),
        ('frequent_issues', 'Frequent Issues')
    ], string="Water Supply", tracking=True)

    network_coverage = fields.Selection([
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor')
    ], string="Network Coverage", tracking=True)

    power_outage = fields.Selection([
        ('rare', 'Rare'),
        ('occasional', 'Occasional'),
        ('frequent', 'Frequent')
    ], string="Power Outage", tracking=True)

    document_ids = fields.One2many("property.document", "property_id", string="Document Attachments")
    facility_ids = fields.One2many("property.facility","property_id", string="Facilities")
    nearby_amenity_ids = fields.One2many("property.nearby.amenity", "property_id", string="Nearby Amenities")
    dynamic_attribute_ids = fields.One2many("property.dynamic.attribute", "property_id", string="Dynamic Attributes")

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
