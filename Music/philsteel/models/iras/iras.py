# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IRAS(models.Model):
	_name = 'philsteel.iras'
	
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:")
	sc_no = fields.Char(string="S.C. No:")
	noc_status = fields.Selection([('with_noc', 'With NOC'), ('without_noc', 'Without NOC')], string='NOC Status')
	noc_date = fields.Date(string="Date of NOC")
	date = fields.Date(string='Date')
	#--------particular_problem---------#
	particular_problems = fields.Text(string="Problems")
	jobsite_sketch = fields.Binary()
	#--------actual observation---------#
	observation = fields.Text(string="Actual Observation and Action Taken")
	#--------duration of rectification---------#
	from_date = fields.Date(string='From')
	to_date = fields.Date(string='To')
	#--------investigation perpormed by---------#
	personnel = fields.Many2many('philsteel.projectmanpower', string='Investigation / Rectification Performed By',  ondelete='cascade')

	positions = fields.Many2one(
		'philsteel.positions', 'Position',  ondelete='cascade'
	)
	remarkss = fields.Text(string="Remarks")
	prepare_by = fields.Many2one(
		'philsteel.contacts', 'Prepered By',  ondelete='cascade'
	)
	noted_by = fields.Many2one(
		'philsteel.contacts', 'Noted By',  ondelete='cascade'
	)

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