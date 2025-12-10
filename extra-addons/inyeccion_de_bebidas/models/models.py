# -*- coding: utf-8 -*-
from operator import truediv

#importamos los modelos, campos y la api
from odoo import models, fields, api

#Todas nuestras clases heredaran de la clase models.Model
class inyeccion_de_bebidas(models.Model):
    # De aquí es donde cogerá el oddoo el nombres para la tabla en la  BBDD
    # Comprueba los nombres de otros modulos y sus tablas
    # Sgue la estructura modulo.modelo

     _name = 'inyeccion_de_bebidas.inyeccion_de_bebidas'
     _description = 'bebida recomendada basada en el nivel de sueño de los alumnos de Daniel Castelao'

     alumno = fields.Char(string="Nombre del alumno")
     nivel_de_sueno = fields.Integer(string="Nivel de sueño")


     bebida_recomendada = fields.Char(string="Bebida recomendada", compute="_compute_bebida_recomendada")
     store=True #El valor se guarda en la BBDD, permitiendo búsquedas y filtros
     @api.depends('nivel_de_sueno')
     def _compute_bebida_recomendada(self):
         for record in self:
             if record.nivel_de_sueno<=3:
                 record.bebida_recomendada = "Café con leche"
             elif 4 <= record.nivel_de_sueno <= 6:
                 record.bebida_recomendada = "Café solo largo"
             elif 7 <= record.nivel_de_sueno <= 9:
                 record.bebida_recomendada = "Café solo larguísimo"
             elif record.nivel_de_sueno == 10:
                 record.bebida_recomendada = "Inyección de adrenalina"
             else:
                 record.bebida_recomendada = "Tirarse del halo de Vialia"




#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

