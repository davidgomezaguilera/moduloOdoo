from odoo import models, fields, api

class Convalidacion(models.Model):
	_name = 'practica.convalidacion'
	nombre = fields.Char('Nombre', required=True)
	fecha_convalidacion = fields.Date('Fecha de convalidación',required=True)
	modulo_id = fields.Many2one('practica.modulo','Módulo')
	alumno_id = fields.Many2one('practica.alumno','Alumno')

