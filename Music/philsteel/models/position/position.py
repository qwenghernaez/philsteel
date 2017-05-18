# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Positions(models.Model):
	_name = 'philsteel.positions'

	name = fields.Char(string="Position", required=True)
	description = fields.Text(string="Description")