from odoo import models, fields, api

class socios(models.Model):
    _name = 'library_aie.socios'
    _description = 'library_aie.socios'

    nombre = fields.Char(string='Nombre del autor')
    telefono = fields.Integer(string='Teléfono de contacto')
    
    libros_ids= fields.Many2many(
        string='Libros',
        comodel_name='library_aie.libros',
    )
    