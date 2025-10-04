{
    "name": "POS No Tax on Receipt",
    "version": "15.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Remove tax total line from POS receipt",
    "author": "TZ hosais CJL",
    "website": "https://github.com/hosais/no_tax_receipt",
    "depends": [
        "point_of_sale",
        "ba_dcp_pos_extension"
    ],
    "data": [
        "views/pos_receipt_no_tax_info.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}