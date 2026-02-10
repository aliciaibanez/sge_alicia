from odoo import models, fields, api


class Pieza(models.Model):
    _name = "taller.pieza"
    _description = "Pieza"
    _sql_constraints = [
        ("unique_nombre", "unique(nombre)", "El nombre debe ser único"),
        (
            "precio_unitario",
            "CHECK(precio_unitario >= 0)",
            "El precio debe ser mayor que 0",
        ),
    ]

    nombre = fields.Char(string="Nombre de la pieza")

    codigo = fields.Char(
        string="Código de la pieza",
    )

    precio_unitario = fields.Float(string="Precio unitario")

    reparacion_ids = fields.Many2many(
        string="reparacion",
        comodel_name="taller.reparacion",
        relation="taller_reparacion_this_taller_pieza_rel",
        column1="taller_pieza_id",
        column2="taller_reparacion_id",
    )
