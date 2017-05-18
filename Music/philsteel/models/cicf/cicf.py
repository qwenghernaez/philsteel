# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CICF(models.Model):
	_name = 'philsteel.cicf'

	jobsite_image = fields.Binary()
	cicf_no = fields.Char(string="CICF. No:")
	concern_dept = fields.Char(string='Concerned Department')
	complain_date = fields.Date(string='Date')
	name = fields.Many2one(
		'philsteel.customer_inquiry', 'Project Name',  ondelete='cascade', required='True'
	)
	dept = fields.Many2one(
		'philsteel.departmentx', 'Concerned Departments',  ondelete='cascade', required='True'
	)

	client = fields.Char(string='Customer')
	client_code = fields.Char(string='Customer Code')
	location = fields.Text(string="Jobsite Location")
	
	#--------REFERENCES---------#
	ic_no = fields.Char(string="I.C. No:")
	sc_no = fields.Char(string="S.C. No:")
	nica_signed_date = fields.Date(string="NICA Date")
	jobsite_contacts = fields.Many2one(
		'philsteel.sitecontacts', 'Site Contact',  ondelete='cascade'
	)
	designation = fields.Many2one('philsteel.positions', string='Designation', ondelete='cascade')
	tel_no = fields.Char(string='Contact Person Tele.No')
	date_action_required = fields.Char(string='Date Action Required')
	
	jobsite_sketch = fields.Binary()
	#--------particulars---------#
	particularss = fields.Text(string="Particular")
	#--------signatory---------#
	prep_by = fields.Many2one(
		'philsteel.contacts', 'Prepared By',  ondelete='cascade'
	)
	prep_date = fields.Date(string='Prepared Date')
	endorsed_by = fields.Many2one(
		'philsteel.contacts', 'Endorsed By',  ondelete='cascade'
	)
	endorsed_date = fields.Date(string='Endorsed Date')
	approved_by = fields.Many2one(
		'philsteel.contacts', 'Approved By',  ondelete='cascade'
	)
	approved_date = fields.Date(string='Approved Date')
	acknowledge_by = fields.Many2one(
		'philsteel.contacts', 'Acknowledged By',  ondelete='cascade'
	)
	acknowledge_date = fields.Date(string='Acknowledged Date')

	statuss = fields.Selection([
		('draft', 'Draft'), 
		('solved', 'Solved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
	

	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'solved'

		return True

	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.location = record.name.location
			record.ic_no = record.name.ic_no
			record.sc_no = record.name.sc_no
			record.client = record.name.client
			record.nica_signed_date = record.name.nica_signed_date

	@api.onchange('jobsite_contacts')
	def get_proj_details(self):
		for recorda in self:
			recorda.tel_no = recorda.jobsite_contacts.phone
