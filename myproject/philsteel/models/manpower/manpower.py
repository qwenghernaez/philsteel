# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectManpower(models.Model):
	_name = 'philsteel.projectmanpower'
	_inherits = {'res.partner': 'partner_id', }

	id = fields.Integer('ID', readonly=True)
	partner_id = fields.Many2one(
		'res.partner', 'Related Partner', required=True, ondelete='cascade',
		help='User ID'
	)
	image = fields.Binary()
	positions = fields.Char(string="Position", required=True)
	code = fields.Char(size=256, string='ID')

	info = fields.Text(string='Extra info')
	active = fields.Boolean(
		'Active', default=True,
		help='If unchecked, it will allow you to hide contact without '
			 'removing it.'
	)

	@api.model
	def create(self, vals,):
		groups_proxy = self.env['res.groups']
		group_ids = groups_proxy.search([('name', '=', 'ProjectManpower')])
		vals['groups_id'] = [(6, 0, group_ids)]
		return super(ProjectManpower, self).create(vals)

