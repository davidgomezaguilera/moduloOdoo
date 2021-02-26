from odoo import models, fields, api

class Alumno(models.Model):
	_name = 'practica.alumno'
	nombre = fields.Char('Nombre y apellidos', required=True)
	edad = fields.Integer('Edad',required=True)
	localidad = fields.Char('Localidad')
	provincia = fields.Char('Provincia')
	email = fields.Char('Email')
	convalidacion_id = fields.One2many('practica.convalidacion','alumno_id','Convalidaciones del alumno')

