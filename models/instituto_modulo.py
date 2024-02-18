# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoModulo(models.Model):
    
    _name = 'instituto.modulo'
    _description = 'Módulo del instituto'
    _rec_name = 'nombreModulo'

    nombreModulo = fields.Char('Nombre del Módulo')

    #Relaciones
    idCiclo = fields.Many2one('instituto.ciclo', string='Ciclo Formativo', required=True)
    idAlumno = fields.Many2many('instituto.alumno', string='Alumnos Matriculados', required=True)
    idProfesor = fields.Many2one('instituto.profesor', string='Profesor que Imparte', required=True)


