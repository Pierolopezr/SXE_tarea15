# -*- coding: utf-8 -*-

from odoo import models, fields, api


class leed_malditos(models.Model):
     _name = 'leed_malditos.leed_malditos'
     _description = 'Registro de veces que un profesor manda a leer'

     profesor = fields.Char(string ="Nombre del docente")
     veces_mando_leer = fields.Integer(string="Veces que mandó a leer")
     description = fields.Text()
