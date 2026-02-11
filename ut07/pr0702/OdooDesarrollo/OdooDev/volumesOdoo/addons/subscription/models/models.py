import datetime
from odoo import models, fields, api


class subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'subscription.subscription'
    _sql_constraints = [ ('unique_name', 'unique(name)', 'El nombre debe ser único'),]

    name = fields.Char(string='Suscripción', required = True)
    customer_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required = True
    )
    
    subscription_code = fields.Char(string='Identificador', required = True)
    start_date = fields.Date(string='Fecha de inicio', required = True)
    end_date = fields.Date(string='Fecha de finalización', required = True)
    duration_months = fields.Integer(
        string='Meses de suscripción', compute='_compute_months'
    )
    renewal_date = fields.Date(string='Fecha de renovación automática')
    status = fields.Selection(
        string='Estado de la suscripción',
        selection=[('active', 'Activo'), ('expired', 'Expirado'), ('pending', 'Pendiente'), ('cancelled', 'Cancelada')]
    )
    is_renewable = fields.Boolean(
        string='Suscripción automática'
    )
    auto_renewal = fields.Boolean(
        string='Autorenovación'
    )
    
    price = fields.Integer(string = "Precio de la suscripción")
    usage_limit = fields.Integer(string = "Número máximo de usos")
    current_usage = fields.Integer(string = "Cantidad de usos utilizados")
    use_percent = fields.Float(string='	Porcentaje de servicios utilizados', compute='_compute_use')
    

    #Cálculos
    
    @api.depends('end_date', 'start_date')
    def _compute_months(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = record.start_date - record.end_date
                record.duration_months = delta.days // 30
            else:
                record.duration_months = 0
    
    @api.depends('usage_limit', 'current_usage')
    def _compute_use(self):
        for record in self:
            if record.usage_limit > 0:
                record.use_percent  = (record.current_usage * 100) / record.usage_limit
            else:
                record.use_percent  = 0

    def ampliar_dias(self):
        for record  in self:
            record.end_date = record.end_date + datetime.timedelta(days=15)
            
    
    