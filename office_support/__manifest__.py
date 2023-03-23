# -*- coding: utf-8 -*-
#############################################################################
#
#    odoo customizers
#
#    Copyright (C) 2023-TODAY Odoo Customizers(<https://www.odoocustomizers.com/>)
#    Author: Arjun Baidya (odoocustomizers@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Office Support',
    'version': '16.0.1.0.0',
    'summary': """Manage your office support by smart app""",
    'author': "Odoo Customizers",
    'maintainer': 'Odoo Customizers',
    'company': "Odoo Customizers",
    'website': 'https://www.odoocustomizers.com/',
    'category': 'Human Resources',
    'description': """
    Helps You To manage office support.
    """,
    'depends': [
        'base',
        'hr',
        'contacts',
        'mail',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/support_request.xml',
        'views/support_service.xml',
        'views/menu.xml',

    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
