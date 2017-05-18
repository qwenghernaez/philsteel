# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PISReports(models.Model):
	_name = 'philsteel.pisreports'


	client = fields.Char(string='Client')

	inspection_date = fields.Date(string='Date of Inspection')
	accomplishment_date = fields.Date(string='Accomplishment Date')
	roofing = fields.Boolean(string='Roofing')
	deckings = fields.Boolean(string='Decking')
	cladding = fields.Boolean(string='Cladding')
	other = fields.Char(string='Others')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	contact_person = fields.Char(string='Contact Person')
	site_representative = fields.Many2one('philsteel.contacts', string='Representative at Site during Inspection',  ondelete='cascade')
	designation_contact = fields.Char(string='Designation Contact ')
	location = fields.Char(string='Location')
	ic_number = fields.Char(string='I.C Number')
	sc_number = fields.Char(string='S.C Number')
	arrival_time = fields.Char(string='Time of Arrival')
	departure_time = fields.Char(string='Time of Departure')
	
	work_scope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')
	activity = fields.Many2many('philsteel.projectactivities', string='Activities',  ondelete='cascade')
	material = fields.Many2many('philsteel.materiales', string='Materials Installed',  ondelete='cascade')
	wheather = fields.Selection([('rainy', 'Rainy'), ('cloudy', 'Cloudy'), ('fair', 'Fair')], string='Wheather')

	other_concerns = fields.Text(string="Other concerns:")

	prepared_by = fields.Many2one(
		'philsteel.contacts', 'Prepared By',  ondelete='cascade'
	)
	approved_by = fields.Many2one(
		'philsteel.contacts', 'Approved By',  ondelete='cascade'
	)
	man_power = fields.Many2many('philsteel.contacts', string='Man Power',  ondelete='cascade')
	tool_equipment = fields.Many2many('philsteel.materials', string='Tools and Equipments',  ondelete='cascade')
	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.client = record.name.customer_name
			record.ic_number = record.name.ic_no
			record.sc_number = record.name.sc_no
			record.location = record.name.location
			

	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'approved'

		return True