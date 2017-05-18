# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
	_name = 'philsteel.materials'


	image = fields.Binary()
	name = fields.Char(string="Material Name", required='True')
	code = fields.Char(string="Code", required='True')
	description = fields.Text(string="Description")
	prices = fields.Float(string='Material Price', required='True')

	# def create(self, cr, uid, vals, context=None):
 #        sequence = self.pool.get('ir.sequence').get(cr, uid, 'test.base.code')
 #        vals['code'] = sequence
 #        res = super(Materials, self).create(cr, uid, vals, context=context)
 #        return res


class Materiales(models.Model):
	_name = 'philsteel.materiales'

	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.materials', 'Material Name',  ondelete='cascade', required='True'
	)
	prices = fields.Float(string='Material Price')
	pieces_installed = fields.Integer(string='Material Price')
	total_price_installed = fields.Float(string='Total Price', compute='_compute_total_price', store='True')

	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.prices = record.name.prices

	# @api.onchange('prices', 'pieces_installed')
 #    def onchange_field(self):
 #        if self.prices or self.pieces_installed:
 #            self.total_price_installed = self.prices * self.pieces_installed

 	@api.depends('prices','pieces_installed')
 	def _compute_total_price(self):
 		for r in self:
 			if not r.pieces_installed:
 				r.total_price_installed = 0.00
 			else:
 				r.total_price_installed = r.prices * r.pieces_installed
