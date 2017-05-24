# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CICF(models.Model):
	_name = 'philsteel.cicf'

	jobsite_image = fields.Binary()
	cicf_no = fields.Char(string="CICF. No:", readonly='True', required='True', default=lambda self: _('New'))
	concern_dept = fields.Char(string='Concerned Department')
	complain_date = fields.Date(string='Date')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)

	client = fields.Char(string='Client')
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:" )
	sc_no = fields.Char(string="S.C. No:")
	dept = fields.Many2one(
		'philsteel.departmentx', 'Concerned Departments',  ondelete='cascade', required='True'
	)

	client_code = fields.Char(string='Customer Code')
	
	#--------REFERENCES---------#
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
		for recorda in self:
			recorda.client = recorda.name.customer_name
			recorda.ic_no = recorda.name.ic_no
			recorda.sc_no = recorda.name.sc_no
			recorda.location = recorda.name.location


	@api.model
	def create(self, values):

		if values.get('cicf_no', 'New') == 'New':
			values['cicf_no'] = self.env['ir.sequence'].next_by_code('philsteel.cicf') or 'New'

		result = super(CICF, self).create(values)

		return result
