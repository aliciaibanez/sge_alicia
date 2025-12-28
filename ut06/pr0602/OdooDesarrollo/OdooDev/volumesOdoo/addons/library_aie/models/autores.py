from odoo import models, fields, api

class autores(models.Model):
    _name = 'library_aie.autores'
    _description = 'library_aie.autores'

    nombre = fields.Char(string='Nombre del autor')
    pais_id = fields.Many2one(
        comodel_name='res.country',
        string='País')
    
    libros_ids= fields.One2many(
        string='Libros',
        comodel_name='library_aie.libros',
        inverse_name='autor_ids',
    )