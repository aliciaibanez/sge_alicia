from odoo import http
from odoo.http import request


class MyController(http.Controller):

    # Página estática
    @http.route('/taller/bienvenida', auth='public', website=True)
    def bienvenida(self, **kw):
        return request.render('taller.bienvenida')


class MyController2(http.Controller):

    # Página dinámica
    @http.route('/taller/lista', type='http', auth='public', website=True)
    def lista(self, **kwargs):
        vehiculos = request.env['taller.vehiculo'].search([])

        return request.render('taller.lista', {
            'vehiculos': vehiculos
        })
