# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2010 OpenERP Italian Community (<http://www.openerp-italia.org>). 
#    All Rights Reserved
#    $Id$
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

import netsvc
import pooler, tools

from osv import fields, osv

class stock_picking_carriage_condition(osv.osv):
    """
    Carriage condition
    """
    _name = "stock.picking.carriage_condition"
    _description = "Carriage Condition"
    _columns = {
	'name':fields.char('Carriage Condition', size=64, required=True, readonly=False),
	'note': fields.text('Note'),
    }
stock_picking_carriage_condition()

class stock_picking_goods_description(osv.osv):
    """
    Description of Goods
    """
    _name = 'stock.picking.goods_description'
    _description = "Description of Goods"

    _columns = {
	'name':fields.char('Description of Goods', size=64, required=True, readonly=False),
	'note': fields.text('Note'),
    }
stock_picking_goods_description()


class stock_picking_reason(osv.osv):
    """
    Reason for Transportation
    """
    _name = 'stock.picking.transportation_reason'
    _description = 'Reason for transportation'

    _columns = {
	'name':fields.char('Reason For Transportation', size=64, required=True, readonly=False),
	'note': fields.text('Note'),
    }
stock_picking_reason()

class stock_picking(osv.osv):
    _inherit = "stock.picking"
    _columns =  {
        'company_id': fields.many2one('res.company', 'Company', required=True),
        'carriage_condition_id': fields.many2one('stock.picking.carriage_condition', 'Carriage condition'),
        'goods_description_id': fields.many2one('stock.picking.goods_description', 'Description of goods'),
        'transportation_reason_id': fields.many2one('stock.picking.transportation_reason', 'Reason for transportation'),
	'packages_no' : fields.integer('Number of Packages'),
    }
    _defaults = {
        'company_id': lambda self, cr, uid, context: self.pool.get('res.users').browse(cr, uid, uid,context=context).company_id.id,
    }


    def create(self, cr, user, vals, context=None):
        if ('name' not in vals) or (vals.get('name')=='/'):
	    if 'type' in vals.keys() and vals['type']=='out':
            	vals['name'] = self.pool.get('ir.sequence').get(cr, user, 'stock.picking_out')
	    elif 'type' in vals.keys() and vals['type']=='internal':
            	vals['name'] = self.pool.get('ir.sequence').get(cr, user, 'stock.picking_internal')
	    else:
		vals['name'] = self.pool.get('ir.sequence').get(cr, user, 'stock.picking_in')		

        return super(stock_picking, self).create(cr, user, vals, context)


stock_picking()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:



