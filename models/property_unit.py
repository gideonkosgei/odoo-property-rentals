# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PropertyUnit(models.Model):
    _name = "property.unit"
    _description = "Property Unit"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Unit Name", required=True, help="The name or number of the unit (e.g., A101, Office 3B)",tracking=True)
    property_id = fields.Many2one("property.property", string="Property", required=True,tracking=True,
                                  help="The property this unit belongs to")
    mixed_unit_type = fields.Selection([("residential", "Residential"), ("retail", "Retail"),("office", "Office"),("warehouse", "Warehouse")],
                                       string="Unit Type",tracking=True)

    image_ids = fields.One2many(
        "property.unit.image", "unit_id", string="Unit Images"
    )

    utility_meter_ids = fields.One2many("property.unit.utility.meter", "unit_id", string="People")
    furnish_ids = fields.One2many("property.unit.furnish", "unit_id", string="Furniture & Appliance")

    wall_material = fields.Many2one(
        "property.list.value",
        string="Wall Material",
        domain="[('list_name_id', '=', 54), ('active', '=', True)]",
        tracking=True
    )
    flooring_type = fields.Many2one(
        "property.list.value",
        string="Flooring Type",
        domain="[('list_name_id', '=', 55), ('active', '=', True)]",
        tracking=True
    )
    kitchen_type = fields.Many2one(
        "property.list.value",
        string="Kitchen Type",
        domain="[('list_name_id', '=', 56), ('active', '=', True)]",
        tracking=True
    )
    kitchen_appliance = fields.Boolean(string="Kitchen Appliances", default=False)

    cabinets_material = fields.Many2one(
        "property.list.value",
        string="Cabinet Material",
        domain="[('list_name_id', '=', 58), ('active', '=', True)]",
        tracking=True
    )
    lighting_type = fields.Many2one(
        "property.list.value",
        string="Lighting Type",
        domain="[('list_name_id', '=', 59), ('active', '=', True)]",
        tracking=True
    )
    air_conditioning = fields.Many2one(
        "property.list.value",
        string="Air Conditioning",
        domain="[('list_name_id', '=', 60), ('active', '=', True)]",
        tracking=True
    )
    heating_system = fields.Many2one(
        "property.list.value",
        string="Heating System",
        domain="[('list_name_id', '=', 61), ('active', '=', True)]",
        tracking=True
    )
    furnishing = fields.Many2one(
        "property.list.value",
        string="Furnishing",
        domain="[('list_name_id', '=', 62), ('active', '=', True)]",
        tracking=True
    )
    fireplace = fields.Boolean(string="Fireplace", default=False,tracking=True)
    wifi_ready = fields.Boolean(string="Wifi Ready?", default=False,tracking=True)
    fiber_optic_available = fields.Boolean(string="Fiber Optics Availability?", default=False,tracking=True)
    smart_home_features = fields.Boolean(string="Smart Home Features?", default=False,tracking=True)
    cable_tv = fields.Boolean(string="Cable TV Connection?", default=False,tracking=True)

    has_solar_panels = fields.Boolean(string="Solar Panels?", default=False,tracking=True)
    energy_rating = fields.Selection([("A+", "A+"), ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")],
                                     string="Energy Rating",tracking=True)
    insulation = fields.Selection([("Foam", "Foam"), ("Fiber_glass", "Fiber Glass"), ("Wool", "Wool"), ("None", "None")],
                                  string="Insulation",tracking=True)
    green_certification = fields.Selection([("LEED", "LEED"), ("BREEAM", "BREEAM"), ("None", "None")],
                                           string="Green Certification",tracking=True)
    water_recycling_system = fields.Boolean(string="Water Recycling?", default=False,tracking=True)

    garden = fields.Boolean(string="Garden?", default=False,tracking=True)
    terrace = fields.Boolean(string="Terrace?", default=False,tracking=True)
    outdoor_seating_area = fields.Boolean(string="Outdoor Seating Area?", default=False,tracking=True)

    # orphans
    built_in_closets = fields.Boolean(string="Built-in Closets?", default=False,tracking=True)
    basement_storage = fields.Boolean(string="Basement Storage?", default=False,tracking=True)
    attic = fields.Boolean(string="Attic?", default=False,tracking=True)

    # parking
    covered_parking = fields.Boolean(string="Covered Parking?", default=False,tracking=True)
    parking = fields.Integer(string="Parking Slots", default=False, help="Number of allocated parking spaces",tracking=True)
    visitor_parking = fields.Boolean(string="Visitor Parking?", default=False,tracking=True)
    loading_zone = fields.Boolean(string="Loading Zone?", default=False,tracking=True,
                                  help="Whether there’s a dedicated loading/unloading area")
    handicap_accessible = fields.Boolean(string="Handicap Accessible?", default=False,tracking=True,
                                         help="Whether the unit has accessibility features")
    # security & safety
    cctv = fields.Boolean(string="CCTV?", default=False,tracking=True)
    fire_alarm = fields.Boolean(string="Fire Alarm?", default=False,tracking=True)
    emergency_exits = fields.Boolean(string="Emergency Exits?", default=False,tracking=True)
    fire_suppression_system = fields.Boolean(string="Has Fire Suppression Systems?",tracking=True,
                                             help="sprinklers/fire-resistant walls are installed?")
    bathrooms = fields.Integer(string="Bathrooms", help="Number of bathrooms",tracking=True)
    bathroom_features = fields.Selection(
        [("Bathtub", "Bathtub"), ("Walk-in Shower", "Walk-in Shower"), ("Jacuzzi", "Jacuzzi"), ("Bidet", "Bidet")],
        string="Bathroom Features",tracking=True)
    water_supply = fields.Selection(
        [("Municipal", "Municipal"), ("Borehole", "Borehole"), ("Well", "Well"), ("Tank", "Tank")],
        string="Water Supply",tracking=True)

    plumbing_status = fields.Selection(
        [("Modern", "Modern"), ("Old", "Old"), ("Needs Repairs", "Needs Repairs")], string="Plumbing Status",tracking=True)

    area_measurement_ids = fields.One2many(
        "property.area.measure", "unit_id", string="Area Measurement",tracking=True
    )
    total_sq_feet = fields.Float(
        string="Total Square Feet",
        compute="_compute_total_sq_feet",
        help="The total area square feet of the " "property",
    )

    floor_number = fields.Integer(string="Floor Number", help="The floor where the unit is located",tracking=True)

    bedrooms = fields.Integer(string="Bedrooms", help="Number of bedrooms (if residential)",tracking=True)
    bathrooms = fields.Integer(string="Bathrooms", help="Number of bathrooms",tracking=True)

    rent_price = fields.Float(string="Rent Price", help="Rental price per month or lease term", tracking=True)

    property_layout = fields.Selection(
        [("open_plan", "Open - plan"), ("traditional", "Traditional"), ("multi_level", "Multi - level")],
        string="Property Layout", tracking=True)

    status = fields.Selection(
        [("available", "Available"), ("occupied", "Occupied"), ("under_maintenance", "Under Maintenance")],
        string="Status",
        default="available",
        tracking=True
    )

    lease_status = fields.Many2one(
        "property.list.value",
        string="Lease Status",
        domain="[('list_name_id', '=', 71), ('active', '=', True)]",
        default="Available",
        tracking=True,
        required=True
    )
    financial_legal_status = fields.Many2one(
        "property.list.value",
        string="Financial & Legal Status",
        domain="[('list_name_id', '=', 70), ('active', '=', True)]",
        tracking=True
    )
    special_use_case = fields.Many2one(
        "property.list.value",
        string="Special Use Cases",
        domain="[('list_name_id', '=', 72), ('active', '=', True)]",
        tracking=True
    )
    occupancy_status = fields.Many2one(
        "property.list.value",
        string="Occupancy Status",
        domain="[('list_name_id', '=', 69), ('active', '=', True)]",
        tracking=True,
        required=True
    )

    finish_living_bedroom = fields.Selection(
        [("Tiles", "Tiles"), ("marble", "marble"), ("wood", "wood"), ("carpet", "carpet"), ("carpet", "carpet")],
        string="Living & Bedrooms",tracking=True)

    finish_Kitchen = fields.Selection([("ceramic", "Ceramic or Porcelain Tiles"), ("anti_slip", "Anti-slip Flooring")],
                                      string="Kitchen",tracking=True)

    finish_bathroom = fields.Selection([("ceramic", "Waterproof Tiles"), ("anti_skid", "Anti-skid Flooring")],
                                       string="Bathroom",tracking=True)
    finish_corridor = fields.Selection(
        [("Granite", "Granite"), ("terrazzo", "Terrazzo"), ("vitrified", "Vitrified Tiles")],
        string="Corridors & Common Areas",tracking=True)

    # commercial
    number_of_rooms = fields.Integer(string="Number of Rooms", help="Number of office spaces/meeting rooms/sections",
                                     tracking=True)
    partitioning = fields.Selection(
        [("open-plan", "Open Plan"), ("cubicles", "Cubicles"), ("individual-offices", "Individual Offices")],
        string="Partitioning",tracking=True
    )
    mezzanine_floor = fields.Boolean(string="Mezzanine Floor?", help="Unit has a mezzanine level?",tracking=True)
    private_entrance = fields.Boolean(string="Private Entrance?", help="Unit has an exclusive entrance?",tracking=True)
    has_balcony = fields.Boolean(string="Has Balcony?", help="the unit has a balcony?",tracking=True)
    number_of_balconies = fields.Integer(string="Number of Balconies", help="Number of balconies",
                                         tracking=True)



    # Office Space & Layout
    workstation_capacity = fields.Integer(string="Workstation Capacity", help="Maximum workstation count",
                                          tracking=True)
    conference_rooms = fields.Integer(string="Conference Rooms", help="Number of meeting rooms",
                                      tracking=True)
    executive_offices = fields.Integer(string="Executive Offices", help="Number of private executive offices",
                                       tracking=True)
    has_kitchen_pantry = fields.Boolean(string="Has Pantry/Kitchen?",
                                        help="Whether a pantry/kitchen area is available?",tracking=True)
    has_lounge_area = fields.Boolean(string="Has Lounge Area?",
                                     help="Whether a common lounge/break area is available?",tracking=True)
    reception_area = fields.Boolean(string="Has Reception Area?",
                                    help="Whether a reception area is available?",tracking=True)
    soundproofing = fields.Boolean(string="Soundproofed?",
                                   help="Whether soundproofing is installed?",tracking=True)
    hvac_system = fields.Selection(
        [("central_air", "Central Air"), ("split_ac", "Split AC"), ("fan_ventilation", "Fan Ventilation")],
        string="HVAC System",tracking=True
    )
    # Warehouse & Industrial Space Specifications
    storage_capacity = fields.Float(string="Storage Capacity(m³)", help="Maximum storage capacity in cubic meters",
                                    tracking=True)
    loading_docks = fields.Integer(string="Loading Docks", help="Number of loading docks for trucks",
                                   tracking=True)
    has_truck_parking = fields.Boolean(string="Truck Parking?",
                                       help="Whether the unit has dedicated truck parking?")
    ceiling_clearance = fields.Float(string="Ceiling Clearance(m)",
                                     help="Minimum ceiling height in meters (for stacking goods)",
                                     tracking=True)
    floor_loading_capacity = fields.Float(string="Floor Loading Capacity(kg/m²)",
                                          help="Load-bearing capacity of the floor (in kg/m²)",
                                          tracking=True)
    temperature_control = fields.Selection(
        [("cold_storage", "Cold Storage"), ("climate_controlled", "Climate-Controlled"), ("standard", "Standard")],
        string="Temperature Control",tracking=True
    )

    pallet_racking = fields.Boolean(string="Pallet Racking?",
                                    help="Whether pre-installed racking is available",tracking=True)

    # Connectivity & Technology
    backup_power_supply = fields.Boolean(string="Backup Power Supply?",
                                         help="Whether pre-installed racking is available",tracking=True)
    biometric_access = fields.Boolean(string="Biometric Access?",
                                      help="Is access is controlled via biometrics?",tracking=True)

    #Retail Space Specifications (For shops, malls, showrooms etc.)
    display_windows = fields.Boolean(string="Display Windows?",
                                      help="Whether large display windows are available",tracking=True)
    shelving_racks = fields.Boolean(string="Shelving Racks",
                                     help="Whether shelving racks are included",tracking=True)
    customer_seating_area = fields.Boolean(string="Has Customer Seating Area?",
                                    help="Whether there’s a seating area",tracking=True)
    billing_counter_space = fields.Boolean(string="Billing Counter Space?",tracking=True,
                                           help="Whether dedicated counter space is available")
    foot_traffic_rating = fields.Selection(
        [("high", "High"), ("medium", "Medium"), ("low", "Low")],
        string="Temperature Control",tracking=True
    )
    unit_dynamic_attribute_ids = fields.One2many("property.unit.dynamic.attribute", "unit_id", string="Dynamic Attributes")
    # _sql_constraints = [
    #     ('unique_unit_property', 'UNIQUE(name, property_id)',
    #      'The unit name must be unique within the same property.')
    # ]

    def _compute_total_sq_feet(self):
        """Calculates the total square feet of the property"""
        for rec in self:
            rec.total_sq_feet = sum(rec.mapped("area_measurement_ids").mapped("area"))

    is_residential = fields.Boolean(compute="_compute_property_type_flags")
    is_commercial = fields.Boolean(compute="_compute_property_type_flags")
    is_multi_story = fields.Boolean(compute="_compute_property_type_flags")
    is_office = fields.Boolean(compute="_compute_property_type_flags")
    is_shop = fields.Boolean(compute="_compute_property_type_flags")
    is_warehouse = fields.Boolean(compute="_compute_property_type_flags")
    is_mixed_use = fields.Boolean(compute="_compute_property_type_flags")

    @api.depends("property_id.property_structure_id","property_id.property_structure_id")
    def _compute_property_type_flags(self):
        for record in self:
            property_type_id = record.property_id.property_type_id.id
            property_structure_id = record.property_id.property_structure_id.id
            record.is_mixed_use = property_structure_id == 157
            record.is_multi_story = record.property_id.is_multi_story == True
            record.is_residential = property_type_id == 26
            record.is_commercial = property_type_id == 27
            record.is_office = property_structure_id == 154
            record.is_warehouse = property_structure_id == 156
            record.is_shop = property_structure_id == 155

