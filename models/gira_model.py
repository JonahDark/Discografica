# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api


class gira_model(models.Model):
    _name = 'discografica.gira_model'
    _description = 'Modelo de gira'    

    name = fields.Char(string="Nombre", required=True, index=True)
    fecha_inicio = fields.Date(string="Fecha inicio", required=True, default=date.today())
    fecha_fin = fields.Date(string="Fecha fin", required=True, default=date.today())
    foto = fields.Binary(string="Foto")
    
    
    #RELACIONES     
    artista_ids = fields.Many2many("discografica.artista_model",string="Artista/s")
    concierto_ids=fields.One2many("discografica.concierto_model","gira_id","Conciertos")
    
    
    
