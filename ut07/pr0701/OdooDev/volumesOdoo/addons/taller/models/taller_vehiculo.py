from odoo import models, fields


class Vehiculo(models.Model):
    _name = "taller.vehiculo"
    _description = "Vehículo"
    _sql_constraints = [
        ('unique_matricula', 'unique(matricula)', 'La matrícula debe ser única'),
    ]

    matricula = fields.Char(string="Matrícula", required=True)

    marca = fields.Char(string="Marca")

    modelo = fields.Char(string="Modelo")

    anio = fields.Integer(string="Año")

    cliente_id = fields.Many2one(
        string="Cliente",
        comodel_name="taller.cliente",
        ondelete="restrict",
    )
    
    
    

    reparacion_ids = fields.One2many(
        string="Reparación",
        comodel_name="taller.reparacion",
        inverse_name="vehiculo_id",
    )
