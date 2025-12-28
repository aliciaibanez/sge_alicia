# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryAie(http.Controller):
#     @http.route('/library_aie/library_aie', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_aie/library_aie/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_aie.listing', {
#             'root': '/library_aie/library_aie',
#             'objects': http.request.env['library_aie.library_aie'].search([]),
#         })

#     @http.route('/library_aie/library_aie/objects/<model("library_aie.library_aie"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_aie.object', {
#             'object': obj
#         })
