# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class ventasmod(osv.osv):
	_name='ventas_ventasmod'
	_rec_name='nombre'
	
	_columns={
		'nombre':fields.char('Nombre', size= 80,required=True, help ='nombre aqui'),
		'precio':fields.float('Precio', size= 80,required=True, help ='precio aqui'),
		'stock':fields.integer('stock', size= 80,required=True, help ='cantidad aqui'),
		'fecha_vencimiento':fields.datetime('Fecha de vencimiento', help ='fecha aqui'),
		'active':fields.boolean('Activo'),
		
	}
