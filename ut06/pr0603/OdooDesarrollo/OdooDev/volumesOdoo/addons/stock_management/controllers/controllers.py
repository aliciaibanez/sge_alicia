# -*- coding: utf-8 -*-
# from odoo import http


# class StockManagement(http.Controller):
#     @http.route('/stock_management/stock_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_management/stock_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_management.listing', {
#             'root': '/stock_management/stock_management',
#             'objects': http.request.env['stock_management.stock_management'].search([]),
#         })

#     @http.route('/stock_management/stock_management/objects/<model("stock_management.stock_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_management.object', {
#             'object': obj
#         })
