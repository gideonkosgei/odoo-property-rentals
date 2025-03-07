# -*- coding: utf-8 -*-

{
    'name': "Property Management",
    'version': '18.0.1.0.0',
    'category': 'Industries',
    'summary': 'Streamline rental property management, including tenant tracking, lease management, and rent collection.',
    'description': """
        This Property Management System enables landlords, property managers, and real estate agencies to efficiently oversee rental units. 

        Key Features:
        - Property Management: Track property details, availability, and locations.
        - Tenant Management: Store tenant profiles, lease agreements, and contact details.
        - Lease Management: Automate lease tracking, renewals, and expiration alerts.
        - Rent Collection: Online rent payments, invoices, and payment tracking.
        - Maintenance Requests: Tenant issue reporting, assignment, and tracking.
        - Financial Reporting: Income and expense reports, tax statements.
        - Communication Tools: Landlord-tenant messaging for streamlined communication.
    """,

    'author': "Gideon Kosgei",
    'company': 'Gideon Kosgei',
    'maintainer': 'Gideon Kosgei',
    'website': 'https://github.com/gideonkosgei',
    # 'depends': ['base', 'mail', 'sale_management', 'website','base_geolocalize'],
    'depends': ['base', 'mail', 'sale_management','base_geolocalize'],
    'data': [
        'security/user_groups.xml',
        'security/property_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/advanced_property_management_data.xml',
        'data/ir_cron_data.xml',
        'data/property.list.type.csv',
        'data/property.list.name.csv',
        'data/property.list.value.csv',
        'data/property.public.service.csv',
        'data/property.type.csv',
        'data/property.document.category.csv',
        'data/property.document.csv',
        'data/property.structure.csv',
        'views/property_property_views.xml',
        'views/property_list_type_views.xml',
        'views/property_list_value_views.xml',
        'views/property_list_name_views.xml',
        'views/property_facility_views.xml',
        'views/property_nearby_amenity_views.xml',
        'views/property_type_views.xml',
        'views/property_structure_views.xml',
        'views/property_public_service_views.xml',
        'views/property_tag_views.xml',
        'views/property_document_category_views.xml',
        'views/property_document_views.xml',
        'views/property_search_pannel_views.xml',
        'views/property_templates.xml',
        'views/property_commision_views.xml',
        'views/property_sale_views.xml',
        'views/property_rental_views.xml',
        'views/res_partner_views.xml',
        'views/rental_bill_views.xml',
        'views/property_auction_views.xml',

        'reports/property_sale_report.xml',
        'reports/property_report.xml',
        'wizards/property_sale_report_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'advanced_property_management/static/src/js/property_website.js',
            # 'advanced_property_management/static/src/js/property_item.js',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
