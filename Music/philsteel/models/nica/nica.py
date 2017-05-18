# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NICA(models.Model):
	_name = 'philsteel.nica'
	
	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)

	client = fields.Char(string='Client')
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:" )
	sc_no = fields.Char(string="S.C. No:")
	workscope = fields.Many2many('philsteel.workscope', string='Work Scope',  ondelete='cascade')
	date_complete = fields.Date(string='Date of Completion')
	#==================long tex================#
	message = fields.Text(string="Type Message")
	#==================signatory================#
	personnel = fields.Many2one(
		'philsteel.contacts', 'Personnel',  ondelete='cascade'
	)

	positions = fields.Many2one(
		'philsteel.positions', 'Designation',  ondelete='cascade'
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


	@api.onchange('personnel')
	def get_proj_details(self):
		for record in self:
			record.positions = record.name.designation


	# @api.onchange('name')
	# def get_proj_details(self):
	# 	for record in self:
	# 		record.location = record.name.location
	# 		record.ic_no = record.name.ic_number
	# 		record.sc_no = record.name.sc_number
	# 		record.client = record.name.client


	@api.onchange('name')
	def get_proj_details(self):
		for recorda in self:
			recorda.client = recorda.name.customer_name
			recorda.ic_no = recorda.name.ic_no
			recorda.sc_no = recorda.name.sc_no
			recorda.location = recorda.name.location