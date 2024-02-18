# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InstitutoAlumno(models.Model):
    
    _name = 'instituto.alumno'
    _description = 'Alumno del instituto'
    _rec_name = 'nombreCompleto'

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellido', required=True)

    #Esto puede dar problemas
#    idModulo = fields.Many2many('instituto.modulo', string='Módulos Matriculados')



    nombreCompleto = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombreCompleto = f"{record.nombre} {record.apellidos}"
