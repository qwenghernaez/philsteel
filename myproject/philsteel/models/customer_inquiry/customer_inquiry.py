# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Inquiry(models.Model):
	_name = 'philsteel.customer_inquiry'
	
	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)

	client = fields.Char(string='Client')
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:")
	sc_no = fields.Char(string="S.C. No:")
	workscope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')
	manager_south = fields.Char(string="Inst. Mngr. - South 1")
	date_complete = fields.Date(string='Date of Completed')
	date_mobilization = fields.Date(string='Date of Mobilization')
	proj_incharge = fields.Many2one(
		'philsteel.projectmanpower', 'Project In-charge',  ondelete='cascade'
	)
	overall_remarks = fields.Text(string="Overall Remarks")
	sub_contractor = fields.Char(string="Subcontractor")
	#==================Quality================#
	duration_of_works = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Duration of Works')
	tools_and_equipments = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Tools and Equipments used')
	workmanship = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Workmanship')
	finished_appearance = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Finished Appearance(Total)')
	quality_remarks = fields.Char(string="Remarks")
	#==================safety================#
	safety_initiative = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Safety initiative / awareness of workers')
	work_attitude = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Work Attitude of Workers')
	safety_rules_regulation = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Compliance to Safety Rules and Regulation')
	use_of_ppe = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Availability and Use of PPE')
	safety_remarks = fields.Char(string="Remarks")
	#==================Supervision================#
	communicating_client = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Communicating with Client')
	expertise = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Expertise')
	control_over_workers = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Control over workers')
	reactions_to_problems = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Reactions to problems encountered')
	effectiveness_of_supervision = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Effectivenessof Supervision')
	personality = fields.Selection([('excellent', 'Excellent'), ('acceptable', 'Acceptable'), ('poor', 'Poor')], string='Personality')
	supervision_remarks = fields.Char(string="Remarks")

	nica_status = fields.Selection([('signed', 'Signed Already'), ('not_yet_signed', 'Not Yet Signed')], string='NICA Status')
	nica_signed_date = fields.Date(string="Date")
	nica_reason = fields.Text(string="Please state reason why: ")
	#==================signatory================#
	personnel = fields.Many2one(
		'philsteel.contacts', 'Personnel',  ondelete='cascade'
	)
	accomplish_date = fields.Date(string="Date")
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
	# 		record.ic_no = record.name.ic_no
	# 		record.sc_no = record.name.sc_no
	# 		record.client = record.name.client
	# 		record.workscope = record.name.workscope
	# 		record.date_complete = record.name.date_complete

	@api.onchange('name')
	def get_proj_details(self):
		for recorda in self:
			recorda.client = recorda.name.customer_name
			recorda.ic_no = recorda.name.ic_no
			recorda.sc_no = recorda.name.sc_no
			recorda.location = recorda.name.location