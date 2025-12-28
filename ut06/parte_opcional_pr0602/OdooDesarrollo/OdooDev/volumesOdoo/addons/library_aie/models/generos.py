
from odoo import models, fields, api

class generos(models.Model):
    _name = 'library_aie.generos'
    _description = 'library_aie.generos'

    nombre = fields.Selection([
        ('novela', 'Novela'),
        ('drama', 'Drama'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('misterio', 'Misterio'),
        ('terror', 'Terror'),
        ('historico', 'Histórico'),], string='Género', required=True)
    
    libro_id= fields.One2many(
        string='Libros',
        comodel_name='library_aie.libros',
        inverse_name='genero_id',
    )