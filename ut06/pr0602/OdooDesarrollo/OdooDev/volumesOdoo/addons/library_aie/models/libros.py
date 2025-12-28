
from odoo import models, fields, api

class libros(models.Model):
    _name = 'library_aie.libros'
    _description = 'library_aie.libros'

    titulo = fields.Char(string='Título')
    autor_ids= fields.Many2one(
        string='Autor del Libro',
        comodel_name='library_aie.autores',
    )
    genero_id = fields.Many2one(
        string='Género',
        comodel_name='library_aie.generos',
        ondelete='restrict',
    )
    
    socios_ids = fields.Many2many(
        string='Socios',
        comodel_name='library_aie.socios',
    )