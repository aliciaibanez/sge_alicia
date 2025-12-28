from odoo.exceptions import ValidationError
from odoo import models, fields, api


class stock_product(models.Model):
    _name = 'stock_management.stock_product'
    _description = 'stock_management.stock_product'
    _sql_constraints = [('unique_name', 'unique(nombre)', 'El nombre debe ser único'),
                        ('check_quantity', 'CHECK(quantity >= 0)', 'La cantidad en stock debe ser mayor o igual a 0'),
                        ('unique_full_name', 'unique(nombre, category)', 'El full_name debe ser único'),
                        ('check_length_nombre', 'CHECK(LENGTH(nombre) >= 3', 'El nombre debe tener, al menos, 3 caracteres')]
    
    nombre = fields.Char(string='Nombre')
    category = fields.Selection(
        string='Categoría',
        selection=[('ordenador', 'Ordenador'), ('nevera', 'Nevera')], 
        required=True
        
    )
    price = fields.Monetary(
        string='Precio de venta',
        currency_field='currency_id')
    
    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        default=lambda self: self.env.ref('base.EUR').id)
    
    quantity = fields.Integer(string='Cantidad en stock')
    total_value = fields.Float(
        compute='_compute_total_value' )
    
    minimum_quantity = fields.Integer(string='Cantidad mínima')
    
    stock_status = fields.Selection(compute='_compute_stock_status',
        string='Estado del stock',
        selection=[('normal', 'Normal'), ('low_stock', 'Low Stock')]
    )
    
    full_name = fields.Char(string='Nombre completo', compute='_compute_full_name')
    
    @api.depends('price', 'quantity')
    def _compute_total_value(self):
        for record in self:
            record.total_value = record.price * record.quantity
            
    @api.depends('quantity', 'minimum_quantity')
    def _compute_stock_status(self):
        for record in self:
            if (record.quantity > record.minimum_quantity):
                record.stock_status = 'normal'
            else:
                record.stock_status = 'low_stock'
    
    @api.depends('nombre', 'category')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.nombre} ({record.category})"
                           
    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError('El precio debe ser mayor a 0')
    
    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError('La cantidad debe ser mayor o igual a 0')
    
    @api.constrains('total_value')
    def _check_total_value(self):
        for record in self:
            if record.total_value > 100000 :
                raise ValidationError('El valor total no debe exceder 100000 unidades monetarias')
            
    @api.constrains('category')
    def _check_category(self):
        for record in self:
            if not record.category :
                raise ValidationError('Debe seleccionar la categoría del producto')