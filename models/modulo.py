from odoo import models, fields, api

class Modulo(models.Model):
	_name = 'practica.modulo'
	nombre = fields.Char('Nombre del módulo', required=True)
	descripcion = fields.Text('Descripcion del módulo',required=True)
	ciclo_id = fields.Many2many('practica.ciclo')
