# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 OpenERP Italian Community (<http://www.openerp-italia.org>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name" : "Minimal Italian Chart of Accounts",
    "version" : "0.1",
    "license": "AGPL-3",
    "category" : "Localisation/Account Charts",
    "depends" : ["l10n_it_account",],
    "author" : "OpenERP Italian Community",
    "description": """Piano dei conti italiano minimale, da usare come base di partenza per realizzare il proprio""",
    'website': 'http://www.openerp-italia.org/',
    'init_xml': [
        ],
    'update_xml': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'account_chart.xml',
        'account_tax.xml',
        'l10n_chart_it_minimal.xml',
        ],
    'demo_xml': [
        ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
