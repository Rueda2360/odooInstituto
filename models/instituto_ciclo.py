# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoCiclo(models.Model):
    
    _name = 'instituto.ciclo'
    _description = 'Ciclo del instituto'
    _rec_name = 'nombreCiclo'

    nombreCiclo = fields.Char('Nombre del Ciclo Formativo', required=True)
    descripcionCiclo = fields.Text('Descripción', required=True)
    
    #Esto puede dar problemas
    #idModulo = fields.One2many('instituto.modulo', 'idCiclo', 'Módulos')

    @api.depends('nombreCiclo')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombreCiclo = f"{record.nombreCiclo}"

