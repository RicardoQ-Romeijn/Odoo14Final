# -*- coding: utf-8 -*-
# from odoo import http


# class Modelos9(http.Controller):
#     @http.route('/modelos9/modelos9/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modelos9/modelos9/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modelos9.listing', {
#             'root': '/modelos9/modelos9',
#             'objects': http.request.env['modelos9.modelos9'].search([]),
#         })

#     @http.route('/modelos9/modelos9/objects/<model("modelos9.modelos9"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modelos9.object', {
#             'object': obj
#         })
