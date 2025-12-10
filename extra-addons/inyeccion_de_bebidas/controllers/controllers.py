# -*- coding: utf-8 -*-
# from odoo import http


# class InyeccionDeBebidas(http.Controller):
#     @http.route('/inyeccion_de_bebidas/inyeccion_de_bebidas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inyeccion_de_bebidas/inyeccion_de_bebidas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inyeccion_de_bebidas.listing', {
#             'root': '/inyeccion_de_bebidas/inyeccion_de_bebidas',
#             'objects': http.request.env['inyeccion_de_bebidas.inyeccion_de_bebidas'].search([]),
#         })

#     @http.route('/inyeccion_de_bebidas/inyeccion_de_bebidas/objects/<model("inyeccion_de_bebidas.inyeccion_de_bebidas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inyeccion_de_bebidas.object', {
#             'object': obj
#         })

