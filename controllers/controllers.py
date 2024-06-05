# -*- coding: utf-8 -*-
# from odoo import http


# class TripleDiscountPricelist(http.Controller):
#     @http.route('/triple_discount_pricelist/triple_discount_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/triple_discount_pricelist/triple_discount_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('triple_discount_pricelist.listing', {
#             'root': '/triple_discount_pricelist/triple_discount_pricelist',
#             'objects': http.request.env['triple_discount_pricelist.triple_discount_pricelist'].search([]),
#         })

#     @http.route('/triple_discount_pricelist/triple_discount_pricelist/objects/<model("triple_discount_pricelist.triple_discount_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('triple_discount_pricelist.object', {
#             'object': obj
#         })
