# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoModulo(models.Model):
    
    _name = 'instituto.modulo'
    _description = 'Módulo del instituto'
    _rec_name = 'nombreModulo'

    nombreModulo = fields.Char('Nombre del Módulo')

    #Relaciones
    idCiclo = fields.Many2one('mi_modulo.ciclo_formativo', string='Ciclo Formativo')
    idAlumno = fields.Many2many('mi_modulo.alumno', string='Alumnos Matriculados')
    idProfesor = fields.Many2one('mi_modulo.profesor', string='Profesor que Imparte')


