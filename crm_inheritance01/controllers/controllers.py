# -*- coding: utf-8 -*-
# from odoo import http


# class CrmInheritance01(http.Controller):
#     @http.route('/crm_inheritance01/crm_inheritance01/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_inheritance01/crm_inheritance01/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_inheritance01.listing', {
#             'root': '/crm_inheritance01/crm_inheritance01',
#             'objects': http.request.env['crm_inheritance01.crm_inheritance01'].search([]),
#         })

#     @http.route('/crm_inheritance01/crm_inheritance01/objects/<model("crm_inheritance01.crm_inheritance01"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_inheritance01.object', {
#             'object': obj
#         })
