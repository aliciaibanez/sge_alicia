from odoo import models, fields


class Cliente(models.Model):
    _name = "taller.cliente"
    _description = "Cliente"
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre debe ser único'),
    ]

    name = fields.Char(string="Nombre", required=True)

    telefono = fields.Integer(string="Teléfono")

    email = fields.Char(string="e-mail")

    direccion = fields.Char(string="Dirección")

    vehiculo_ids = fields.One2many(
        comodel_name="taller.vehiculo", inverse_name="cliente_id", string="Vehículos"
    )
