# -*- coding: utf-8 -*-

from odoo import models, fields, api



class WEEKLYPAS(models.Model):
	_name = 'philsteel.weeklypas'

	updated_as_of = fields.Date(string='Updated as of')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	types_of_contract = fields.Selection([('lump_sum', 'Lump Sum'), ('itemized', 'Itemized')], string='Type of Contract')
	aic_no = fields.Char(string="A.I.C. No:")
	ic_amount = fields.Float(string='I.C. / A.I.C. Amount')
	ic_no = fields.Char(string="I.C. No:")
	#----------SC-------#
	sc_no = fields.Char(string="S.C. No:")
	is_group = fields.Char(string="Group")
	document_support = fields.Char(string="Document to Support this billing")
	
	#--------Previous---------#
	amount_prev = fields.Char(string="Amount")
	percent_prev = fields.Char(string="Percentage")
	#--------This Period---------#
	period_amount = fields.Char(string="Amount")
	percent_thisperiod = fields.Char(string="Percentage")
	#--------To Date---------#
	todate_amount = fields.Char(string="Amount")
	percent_todate = fields.Char(string="Percentage")
	#----------------------------------------------------#
	
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