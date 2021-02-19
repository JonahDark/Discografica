# -*- coding: utf-8 -*-

from datetime import date

from odoo import models, fields, api


class discografica_model(models.Model):
    _name = 'discografica.discografica_model'
    _description = 'Modelo de discografica'
    _sql_constraints = [("sql_cons_check_name_discografica", "UNIQUE(name)","Error en el nombre, esta discografica ya existe!")]

    name = fields.Char(string="Nombre", required=True, index=True)
    fecha_creacion = fields.Date(string="Fecha de Creacion", default=date.today(), required = True)
    foto = fields.Binary(string="Foto")
    pais = fields.Char(string="Pais", required=True)
    
    #RELACIONES     
    artista_ids = fields.One2many("discografica.artista_model", "discografica_id", string="Artistas")
