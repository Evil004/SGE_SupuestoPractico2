# -*- coding: utf-8 -*-

from odoo import models, fields


class Escuela(models.Model):
    _name = 'escuela_vela.escuela'
    _description = 'escuela_vela.escuela'

    name = fields.Char(string="Denominacion")
    logo = fields.Binary(string="Logo")
    phoneNumber = fields.Char(string="Telefono")
    email = fields.Char(string="Email")

    monitores = fields.Many2many('escuela_vela.monitor', string="Monitores")
    courses = fields.One2many('escuela_vela.curso', 'escuela', string="Cursos")
    alumnos = fields.One2many('escuela_vela.alumno', 'escuela', string="Alumnos")


class Curso(models.Model):
    _name = 'escuela_vela.curso'
    _description = 'escuela_vela.curso'

    title = fields.Char(string="Titulo")
    durationInDays = fields.Integer(string="Duracion en dias")
    durationInHours = fields.Integer(string="Duracion en horas")
    price = fields.Float(string="Precio")

    escuela = fields.Many2one('escuela_vela.escuela', string="Escuela")


class Monitor(models.Model):
    _name = 'escuela_vela.monitor'
    _description = 'escuela_vela.monitor'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellidos")
    phoneNumber = fields.Char(string="Telefono")
    email = fields.Char(string="Email")
    code = fields.Char(string="Codigo")

    escuelas = fields.Many2many('escuela_vela.escuela', string="Escuelas")
    
class Alumno(models.Model):
    _name = 'escuela_vela.alumno'
    _description = 'escuela_vela.alumno'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellidos")
    phoneNumber = fields.Char(string="Telefono")
    email = fields.Char(string="Email")
    numMatricula = fields.Char(string="Numero de matricula")

    escuela = fields.Many2one('escuela_vela.escuela', string="Escuela")



#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
