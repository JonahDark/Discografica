# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api


class cancion_model(models.Model):
    _name = 'discografica.cancion_model'
    _description = 'Modelo de cancion'    

    name = fields.Char(string="Nombre", required=True, index=True)
    duracion = fields.Char(string="Duracion", required = True, default="--:--")   
    
    #RELACIONES     
    artista_ids = fields.Many2many("discografica.artista_model",string="Artista/s")
    album_id = fields.Many2one("discografica.album_model",string="Album")
    
    
    
