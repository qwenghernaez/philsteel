# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectActivities(models.Model):
	_name = 'philsteel.projectactivities'

	name = fields.Char(string="Activity", required=True)
	status = fields.Selection([('new', 'New'), ('ongoing', 'Ongoing'),('done', 'Done'), ('onhold', 'On-hold'), ('cancelled', 'cancelled')], string='Activity Status')


class Departments(models.Model):
	_name = 'philsteel.departmentx'

	department_name = fields.Char(string="Department", required=True)
	description = fields.Text(string="Description")

