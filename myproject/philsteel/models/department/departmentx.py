# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Departments(models.Model):
	_name = 'philsteel.departmentx'

	name = fields.Char(string="Department", required=True)
	description = fields.Text(string="Description")