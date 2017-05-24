# -*- coding: utf-8 -*-

from odoo import models, fields, api

                                                                                                            
class WorkScope(models.Model):
	_name = 'philsteel.workscope'

	name = fields.Char(string="Scope" , required=True)
	description = fields.Text(string="Description")
