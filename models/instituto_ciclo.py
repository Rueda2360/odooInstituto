# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoCiclo(models.Model):
    
    _name = 'instituto.ciclo'
    _description = 'Ciclo del instituto'
    rec_name = 'nombreCiclo'

    nombreCiclo = fields.Char('Nombre del Ciclo Formativo', required=True)
    descripcionCiclo = fields.Char('Descripción', required=True)
    
    #Esto puede dar problemas
    #idModulo = fields.One2many('instituto.modulo', 'idCiclo', 'Módulos')

