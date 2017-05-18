# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SiteContacts(models.Model):
	_name = 'philsteel.sitecontacts'

	name = fields.Many2one('philsteel.contacts', string='Name',ondelete='cascade')
	designation = fields.Many2one('philsteel.positions', string='Designation', ondelete='cascade')
	phone = fields.Char(string="Mobile Phone Number:")

