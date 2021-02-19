# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class album_model(models.Model):
    _name = 'discografica.album_model'
    _description = 'Modelo de artista'
    _sql_constraints = [("sql_cons_check_name_album", "UNIQUE(name)","Error en el nombre, este album ya existe!")]

    name = fields.Char(string="Nombre", required=True, index=True)
    fecha_creacion_album = fields.Date(string="Fecha creación album", required=True, default=date.today())
    foto = fields.Binary(string="Foto")
    descripcion = fields.Html(string="Descripcion")

    #RELACIONES     
    artista_ids=fields.Many2many("discografica.artista_model",string="Artistas")    
    cancion_ids= fields.One2many("discografica.cancion_model","album_id","Canciones")
