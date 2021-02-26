from odoo import models, fields, api

class Ciclo(models.Model):

	_name = 'practica.ciclo'
	nombre = fields.Char('Nombre', required=True)
	descripcion = fields.Text('Descripcion del ciclo', required=True)
	modulos_id = fields.Many2many('practica.modulo')