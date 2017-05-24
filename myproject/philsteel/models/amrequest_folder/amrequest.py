

from odoo import models, fields, api, _


class AMRequests(models.Model):
     _name = 'philsteel.amrequests'

     customer = fields.Char(string='Customer')

     status = fields.Selection([('new', 'New'), ('visited', 'Visited')], default='new', string='Request Status')

     illustrations = fields.One2many('philsteel.amrimages', 'rfam', string="Illustrations")


     request_number = fields.Char(string='Request Number', readonly='True', required='True', default=lambda self: _('New'))
     location = fields.Text(string='Address')

     name = fields.Many2one(
         'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
     )

     project_type = fields.Selection([('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'), ('government', 'Government'), ('institutional', 'Institutional'), ('mass_housing', 'Mass Housing')], string='Type of Project')
     project_site_address = fields.Text(string='Complete Project Site Address', required='True')
     general_contractor = fields.Many2one(
         'philsteel.projectmanpower', 'Name of contractor',  ondelete='cascade'
     )


     contact_person_at_site = fields.Many2many('philsteel.sitecontacts', string='Site Contact Person',  ondelete='cascade')
     jobsite_contact_number = fields.Char(string='Job Site Telephone or Mobile Number')
     product_profile = fields.Char(string='Product Profile')

     sc_number = fields.Char(string='SC NO')
     ic_number = fields.Char(string='IC NO')
     sq_number = fields.Char(string='SQ NO')
     iq_number = fields.Char(string='IQ NO')

     work_scope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')

     frames_trusses_installed = fields.Char(string='% Frames / Trusses Installed')
     purlins_installed = fields.Char(string='% Purlins Installed')
     sogrod_installed = fields.Char(string='% Sagrod Installed')
     beam_installed = fields.Char(string='% Beam Installed')
     floors_available_for_measurement = fields.Char(string='% No. of Floors Available for Measurement')

     rfm_quotation = fields.Boolean(string='Quotation')
     rfm_contract = fields.Boolean(string='Contact')
     rfm_fabrication = fields.Boolean(string='Fabrication')
     rfm_tech1assistance = fields.Boolean(string='Tech 1 Assistance')
     rfm_others = fields.Text(string='Others')

     ready_for_measurement_date = fields.Date(string='Date when structure ready for measurement')

     accomplished_by = fields.Many2one(
         'philsteel.projectmanpower', 'Accomplished By',  ondelete='cascade'
     )

     date_filed = fields.Date(string='Date Filed')

     approved_by = fields.Many2one(
         'philsteel.contacts', 'Approve By',  ondelete='cascade'
     )
     assigned_by = fields.Many2one(
         'philsteel.android', 'Assigned By',  ondelete='cascade', required='True'
     )

     #image = fields.Binary()
     statuss = fields.Selection([
         ('draft', 'Draft'),
         ('approved', 'Approved'),
         ('ongoing', 'Ongoing'),
         ('done', 'Done'),
         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

     @api.onchange('name')
     def get_proj_details(self):
         for record in self:
             record.customer = record.name.customer_name
             record.ic_number = record.name.ic_no
             record.sc_number = record.name.sc_no
             record.location = record.name.location
             record.project_type = record.name.types_of_project

     @api.multi
     def action_approved(self):
         for visit in self:
             visit.statuss = 'approved'

         return True


     @api.multi
     def action_ongoing(self):
         for visit in self:
             visit.statuss = 'ongoing'

         return True


     @api.multi
     def action_done(self):
         for visit in self:
             visit.statuss = 'done'

         return True

     @api.model
     def create(self, values):
         
         if values.get('request_number', 'New') == 'New':
             values['request_number'] = self.env['ir.sequence'].next_by_code('philsteel.amrequests') or 'New'

         result = super(AMRequests, self).create(values)

         return result





class AMRImages(models.Model):
	_name = 'philsteel.amrimages'

	name = fields.Binary(string='Image')
	description = fields.Text(string='Description')

	rfam = fields.Many2one('philsteel.amrequests',
		ondelete='cascade', string="RFAM", required=True)

	new_field = fields.Binary()
