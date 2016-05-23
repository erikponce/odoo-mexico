# -*- encoding: utf-8 -*-
# Author=Moises Lopez moylop260@vauxoo.com
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import time
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import pooler, tools
from openerp import netsvc


class account_invoice_line(osv.Model):
    _inherit = "account.invoice.line"

    _columns = {
        'import_ids': fields.many2many('import.info', 'account_invoice_line_import_info_rel', 'invoice_line_id', 'import_id',
                                        string='Pedimentos'),
        #tracking_id
        #'move_id': fields.many2one('stock.move', 'Stock Move'),
    }


class import_info(osv.Model):
    _inherit = "import.info"    
    
    _columns = {
        'invoice_line_ids': fields.many2many('account.invoice.line', 'account_invoice_line_import_info_rel', 'import_id', 'invoice_line_id',
                                             string='Líneas de Factura'),
    }

