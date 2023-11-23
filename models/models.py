from odoo import models, fields

class Reserva(models.Model):
	_name = "reservas.reserva"
	name= fields.Char('Nombre', required=True)
	entrada=fields.Date('Fecha de entrada')
	salida=fields.Date('Fecha de salida')
	cliente_id=fields.Many2one('reservas.cliente', string='Cliente')
	habitacion_id=fields.Many2one('reservas.habitacion', string='Habitacion')

class Cliente(models.Model):
	_name = "reservas.cliente"
	name= fields.Char('Nombre', required=True)
	dni= fields.Char('DNI', required=True)
	email= fields.Char('Email')
	nacimineto= fields.Char('Fecha_de_Nacimiento')
	telefono = fields.Char('Telefono')

class Habitacion(models.Model):
	_name = "reservas.habitacion"
	name=fields.Char('Cod_Habitacion', required=True)
	num_camas= fields.Integer('Camas')
	precio= fields.Float('Precio')
	suite= fields.Boolean('Suite')
	descripcion = fields.Char('Descripcion')

