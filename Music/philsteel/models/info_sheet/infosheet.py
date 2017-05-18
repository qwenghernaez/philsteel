# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Infosheet(models.Model):
	_name = 'philsteel.infosheet'

	client = fields.Char(string='Client')
	other = fields.Char(string='Others')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	contact_person = fields.Many2many('philsteel.contacts', string='Work Scope',  ondelete='cascade')
	designation_contact = fields.Char(string='Designation Contact Person')
	location = fields.Char(string='Location')
	ic_number = fields.Char(string='I.C Number')
	sc_number = fields.Char(string='S.C Number')
	tel_number = fields.Char(string='Telephone Number')
	fax_number = fields.Char(string='Fax Number')
	work_scopes = fields.Many2many('philsteel.workscope', string='Work Scope',  ondelete='cascade')
	#----------------STRUCTURE -------------#
	crazy = fields.Char(string='Crazy')
	semi_crazy = fields.Char(string='Semi Crazy')
	wood = fields.Char(string='Wood')
	steel = fields.Char(string='Steel')
	Others = fields.Char(string='Others')
	#---------------MGA IDINAGDAG(Please check if correct.)------------------------------#
	building_height = fields.Char(string='Building Height')
	storeys_no = fields.Char(string='No. of Storeys')
	safe_access = fields.Selection([('available', 'Available'), ('not_available', 'Not Available')], string='Safe Access')
	#----------------ROOFING PROFILE-------------#
	types_a = fields.Char(string='Type')
	total_area_a = fields.Char(string='Total Area')
	color_a = fields.Char(string='Color')
	thickness_a = fields.Char(string='Thickness')
	max_length = fields.Char(string='Max. length site can accomodate.')
	#----------------SIDING PROFILE-------------#
	types_b = fields.Char(string='Type')
	total_area_b = fields.Char(string='Total Area')
	color_b = fields.Char(string='Color')
	thickness_b = fields.Char(string='Thickness')
	#----------------CEILING PROFILE-------------#
	types_c = fields.Char(string='Type')
	total_area_c = fields.Char(string='Total Area')
	color_c = fields.Char(string='Color')
	thickness_c = fields.Char(string='Thickness')
	ceiling_framing = fields.Char(string='Ceiling Framing Included')
	not_included = fields.Char(string='Not Included')
	hat_section = fields.Char(string='Hat Section')
	tee_runner = fields.Char(string='Tee Runner')
	metal_furring = fields.Char(string='Metal Furring')
	otherss = fields.Char(string='Others')
	#----------------PENETRATING FLASHING-------------#
	with_penetration = fields.Char(string='With Penetration')
	without_penetration = fields.Char(string='Without Penetration')
	#----------------FASTENING-------------#
	teks_screw = fields.Char(string='Teks screw')
	strap_rivet = fields.Char(string='Straps and Rivets')
	conceal = fields.Char(string='Concealed')
	anchor_bolts = fields.Char(string='Wanchor Bolts')
	#----------------BENDED ACCESSORIES-------------#
	#------TYPES------#
	end_flashing = fields.Boolean(string='- End Flashing')
	end_wall_flashing = fields.Boolean(string='- End Wall Flashing')
	wall_flashing = fields.Boolean(string='- Wall Flashing')
	ridge_flashing = fields.Boolean(string='- Ridge Flashing')
	ridge_wall_flashing = fields.Boolean(string='- Ridge Wall Flashing')
	crapping = fields.Boolean(string='- Crapping')
	#------DONE OF TYPES------#
	color_d = fields.Char(string='Color')
	thickness_d = fields.Char(string='Thickness')
	standard = fields.Char(string='Standard')
	per_actual = fields.Char(string='Per Actual')
	pmpi = fields.Char(string='PMPI for clients approval')
	regret_wall_other = fields.Char(string='Regrets on Wall by Others')
	regret_wall_pmpi = fields.Char(string='Regrets on Wall by PMPI')
	masonry_work_other = fields.Char(string='Masonry Works by Others')
	masonry_work_pmpi = fields.Char(string='Masonry Works by PMPI')
	#----------------NAILER-------------#
	#------ROOF PURLINS------#
	roofpurlins = fields.Selection([('steels', 'Steels'), ('woods', 'Woods')], string='Roof Purlins')
	#------SIDE GIRTS ------#
	sidegirts = fields.Selection([('steels', 'Steels'), ('woods', 'Woods')], string='Side Girts')
	#----------------NAILER-------------#
	roof_purlins = fields.Boolean(string='Roof Purlins Spacing')
	side_girts = fields.Boolean(string='Side Girts Spacing')
	#----------------ROOF SPAN-------------#
	max_lengths = fields.Char(string='Maximun Length')
	roof_pitch = fields.Char(string='Roof Pitch')
	curve_roof = fields.Char(string='Curve Roof Radius')
	#----------------SKYLIGHTS-------------#
	require = fields.Char(string='Required')
	not_require = fields.Char(string='Not Required')
	thickness_e = fields.Char(string='Thickness')
	max_lengthsa = fields.Char(string='CMax Length')
	#----------------ROLLFORMING-------------#
	on_site = fields.Char(string='Required')
	off_site = fields.Char(string='Not Required')
	#------JOBSITE OR OFFSITE ------#
	powers = fields.Char(string='A. Power')
	space = fields.Char(string='B.Space')
	access = fields.Char(string='C. Access')
	#----------------INSULATION-------------#
	#------REQUIRED ------#
	requires = fields.Char(string='Required')
	types_d = fields.Char(string='     Type')
	thickness_f = fields.Char(string='     Thickness')
	#-----END-REQUIRED ------#
	not_require = fields.Char(string='Not Required')
	#-----WITH WIRE MESH ------#
	with_wiremesh = fields.Char(string='With Wiremesh')
	types_e = fields.Char(string='    Type')
	without_wiremesh = fields.Char(string='With-out Wiremesh')
	gi_wire = fields.Char(string='G.I. Wire')
	spacing = fields.Char(string='Spacing')
	#----------------GUTTER HANGERS-------------#
	by_pmpi = fields.Char(string='By PMPI')
	by_others = fields.Char(string='By Others')
	color_finish = fields.Char(string='Color and Finish')
	bolted_structure = fields.Char(string='Bolted to Structure')
	welded_structure = fields.Char(string='Welde to Structure')
	size = fields.Char(string='Size t x w x l')
	#----------------DECKING PROFILE-------------#
	monolithic = fields.Char(string='Monolithic')
	steel_beams = fields.Char(string='Steel Beams')
	shear = fields.Char(string='Shear studs req')
	closure_requirement = fields.Char(string='Closure Requirement')
	metal = fields.Char(string='     Metal')
	#----------------GUTTER-------------------------#
	colored = fields.Char(string='By PMPI')
	stainless_steel = fields.Char(string='By Others')
	concrete = fields.Char(string='Color and Finish')
	spanish_type = fields.Char(string='Bolted to Structure')
	box_type = fields.Char(string='Welde to Structure')
	#--------CONNECTION-------------#
	revited = fields.Char(string='     Revited')
	welded = fields.Char(string='     Welded')
	gas = fields.Char(string='    Gas')
	tig = fields.Char(string='    Tig')
	seam = fields.Char(string='     Seam')
	glutter_flashing = fields.Char(string='Glutter Flushing')
	requireds = fields.Char(string='Required')
	not_requireds = fields.Char(string='Not Required')
	#--------LOUVERS-------------#
	single_pass = fields.Char(string='Single Pass')
	double_pass = fields.Char(string='Double Pass')
	triple_pass = fields.Char(string='Triple Pass')
	#--------PURLINS--------------------#
	lc = fields.Boolean(string='LC')
	lz = fields.Boolean(string='LZ')
	hat_sections = fields.Boolean(string='Hat Sections')
	#--------FASCIA------------------------#
	fiber_cement = fields.Char(string='Fiber Cement Board')
	metal_fascia = fields.Char(string='Metal Fascia')
	woodss = fields.Char(string='Wood')
	#--------STRAINERS-------------------------#
	stainless = fields.Boolean(string='Stainless')
	ordinary = fields.Boolean(string='Ordinary')
	#--------SLEEVES-------------------------#
	stainless_a = fields.Boolean(string='Stainless')
	ordinary_a = fields.Boolean(string='Ordinary')
	#--------OTHERS--------------------------#
	#--------SPECIFY PREFERED------#
	sealant = fields.Char(string='Specify Preffered Sealant')
	recommended = fields.Char(string='Recommended')
	#--------TYPES OF PROJECT-------------------------#
	residential = fields.Boolean(string='Residential')
	commercial = fields.Boolean(string='Commercial')
	industrial = fields.Boolean(string='Industrial')
	government = fields.Boolean(string='Government')
	institutional = fields.Boolean(string='Institutional')
	mass_housing = fields.Boolean(string='Mass Housing')
	#--------LOCATION-------------------------#
	industrial_park = fields.Boolean(string='Industrial Park')
	populated_areas = fields.Boolean(string='Populated Areas')
	exclusive_subdivision = fields.Boolean(string='Exclusive Subdivision')
	#--------TYPES OF CONTRACT-------------------------#
	lump_sum = fields.Char(string='Lump Sum')
	itemized = fields.Char(string='Itemized')
	#--------BID CONTRACT DOCUMENTS-------------------------#
	avail = fields.Char(string='Available')
	not_avail = fields.Char(string='Not Available')
	#--------WORKINGHOURS-------------------------#
	daytime = fields.Boolean(string='Day Time')
	nighttime = fields.Boolean(string='Night time')
	#--------PRE CONTRACT ARRANGEMENTS-------------------------#
	implementation_date = fields.Date(string='Implementation Date')
	materials_delivery_date = fields.Date(string='Materials Delivery Date')
	structure_turnover_date = fields.Date(string='Structure Turnover Date')
	length_max = fields.Char(string='Max. Length')
	manpower_max = fields.Char(string='Max Manpower')
	#--------LIFTING EQUIPMENT-------------------------#
	manual = fields.Boolean(string='Manual')
	mechanical = fields.Boolean(string='Mechanical or by Crane with Qualified Rigger')
	#--------SITE REQUIREMENTS-------------------------#
	site_id = fields.Boolean(string='ID')
	medical_exam = fields.Boolean(string='Medical Exam')
	hard_hat = fields.Boolean(string='Hard Hat')
	safety_belt = fields.Boolean(string='Safety Belt')
	body_harness = fields.Boolean(string='Body Harness')
	safety_shoes = fields.Boolean(string='Safety Shoes')
	uniforms = fields.Boolean(string='Uniforms')
	servce_vehicle = fields.Boolean(string='Full Time Service Vehicle')
	#-------CLEARANCE-----------#    
	barangay = fields.Boolean(string='     Barangay')
	police = fields.Boolean(string='     Police')
	nbi = fields.Boolean(string='     NBI')
	#--------TEMPORARY FACILITIES-------------------------#
	by_client = fields.Boolean(string='Manual')
	by_pmpi = fields.Boolean(string='Mechanical or by Crane with Qualified Rigger')
	field_office = fields.Boolean(string='Manual')
	#-----BUNK HOUSE-------------#
	onsite = fields.Boolean(string='     Onsite')
	offsite = fields.Boolean(string='     Offsite')
	#====================================================#
	portable_water = fields.Boolean(string='Portable Water')
	electricity = fields.Boolean(string='Electricity')
	others_con = fields.Boolean(string='Other Safety Concerns')
	#--------SIGNATORY-------------------------#
	accomplish_by = fields.Many2one(
		'philsteel.projectmanpower', 'Accomplished By',  ondelete='cascade'
	)
	accomplish_date = fields.Date(string='Accomplished Date')

	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.client = record.name.customer_name
			record.ic_number = record.name.ic_no
			record.sc_number = record.name.sc_no
			record.location = record.name.location


	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'approved'

		return True