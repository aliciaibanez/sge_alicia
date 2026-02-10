from odoo import models, fields, api


class Reparacion(models.Model):
    _name = "taller.reparacion"
    _description = "Reparación"
    _sql_constraints = [
        ("coste_total_positivo", "CHECK(coste_total >= 0)", "El coste total debe ser positivo"),
    ]

    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de finalización")
    descripcion = fields.Char(string="Descripción")

    estado = fields.Selection(
        string="Estado",
        selection=[
            ("borrador", "Borrador"),
            ("en_curso", "En curso"),
            ("finalizada", "Finalizada"),
        ],
        default="borrador",
    )

    coste_total = fields.Float(
        string="Coste total",
        compute="_compute_coste_total",
        store=True,
    )

    vehiculo_id = fields.Many2one(
        comodel_name="taller.vehiculo",
        string="Vehículo",
        ondelete="restrict",
    )

    pieza_ids = fields.Many2many(
        comodel_name="taller.pieza",
        string="Piezas",
        relation="taller_pieza_taller_reparacion_rel",
        column1="taller_reparacion_id",
        column2="taller_pieza_id",
    )

    tecnico_id = fields.Many2one(
        comodel_name="res.users",
        string="Técnico",
        ondelete="restrict",
    )

    @api.depends("pieza_ids")
    def _compute_coste_total(self):
        for record in self:
            record.coste_total = sum(
                pieza.precio_unitario for pieza in record.pieza_ids
            )

    def abrir_reparacion(self):
        for record in self:
            record.estado = "en_curso"

    def cerrar_reparacion(self):
        for record in self:
            record.estado = "finalizada"

    def reabrir_reparacion(self):
        for record in self:
            record.estado = "en_curso"
