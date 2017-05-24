# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CCAA(models.Model):
	_name = 'philsteel.ccaa'
	
	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	sc_no = fields.Char(string="S.C. No:")
	sub_contractor = fields.Char(string="Sub Contractor")
	workscope = fields.Many2many('philsteel.workscope', string='Work Scope',  ondelete='cascade')
	date = fields.Date(string='Date: ')
	prices = fields.Float(string='Amount')
	personnel = fields.Many2one(
		'philsteel.contacts', 'Personnel',  ondelete='cascade'
	)

	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
	

	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'approved'

		return True


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.sc_no = record.name.sc_no