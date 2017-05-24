# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DAILYPAS(models.Model):
	_name = 'philsteel.dailypas'

	updated_as_of = fields.Date(string='Updated as of')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	accomplisment_image = fields.Binary(string="Accomplishment before start and after the end of the days work.")
	site_condition = fields.Binary(string="Site Conditions.")
	status_materials = fields.Binary(string="Status of Materials on site.")
	customer_name = fields.Text(string="")
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:")
	sc_no = fields.Char(string="S.C. No:")
	duration = fields.Char(string="Duration")
	subcon = fields.Char(string="Name of subcon")
	manpower_status = fields.Text(string="Man Power Status")
	material_status = fields.Text(string="Material Status")
	time_start_from = fields.Char(string="Time Start From")
	time_start_to = fields.Char(string="Time Start To")
	equipment_status = fields.Text(string="Equipment Status")
	date_start = fields.Date(string='Date of Started')
	date_complete = fields.Date(string='Date of Completion')
	sales_engineer = fields.Many2one(
		'philsteel.projectmanpower', 'Sales Engineer',  ondelete='cascade'
	)
	#---------------------------------------------------#
	wheather = fields.Selection([('fair', 'Fair'), ('cloudy', 'Cloudy'), ('rainy', 'Rainy')], string='Wheather')
	wheather_from_date = fields.Date(string="From Date")
	wheather_to_date = fields.Date(string="To Date")


	particular = fields.Char(string="Particular")
	unit = fields.Char(string="Unit")
	qty = fields.Char(string="Quantity")
	weight_factor = fields.Char(string="Weight Factor")
	#--------Previous---------#
	qty_prev = fields.Char(string="Quantity")
	percent_prev = fields.Char(string="Percentage")
	#--------This Period---------#
	qty_thisperiod = fields.Char(string="Quantity")
	percent_thisperiod = fields.Char(string="Percentage")
	#--------To Date---------#
	qty_todate = fields.Char(string="Quantity")
	percent_todate = fields.Char(string="%")
	weight = fields.Char(string="Weight Percent")
	#----------------------------------------------------#
	remarks = fields.Text(string="Remarks")
	day_work_program = fields.Char(string="Next Day Work Program")
	proj_incharge = fields.Many2one(
		'philsteel.projectmanpower', 'Project In Charge',  ondelete='cascade'
	)
	client_rep = fields.Many2one(
		'philsteel.contacts', 'Client Representative',  ondelete='cascade'
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
			record.location = record.name.location
			record.ic_no = record.name.ic_no
			record.sc_no = record.name.sc_no
			record.sc_no = record.name.sc_no