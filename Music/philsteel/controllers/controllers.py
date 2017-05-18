
from odoo import http

class WebsiteMaterials(http.Controller):
    @http.route('/page/inventory', auth='public', website=True)
    def index(self, **kw):
        inventory = http.request.env['philsteel.materials']
        return http.request.render('philsteel.website_materials', {
            'materials': inventory.search([])
        })