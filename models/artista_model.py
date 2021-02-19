# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class artista_model(models.Model):
    _name = 'discografica.artista_model'
    _description = 'Modelo de artista'
    _sql_constraints = [("sql_cons_check_name_artista", "UNIQUE(name)","Error en el nombre, este artista ya existe!")]

    name = fields.Char(string="Nombre", required=True, index=True)
    fecha_creacion_grupo = fields.Date(string="Fecha creación grupo", required=True, default=date.today())
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True, default=date.today())
    pais = fields.Char(string="Pais", required=True)
    foto = fields.Binary(string="Foto")
    tipo = fields.Selection([('Grupo', 'Grupo'), ('Cantante', 'Cantante')], string="Tipo", default='Cantante')
    numAlbumes = fields.Integer(string="Numero albumes",readonly=True)

    #RELACIONES     
    album_ids = fields.Many2many("discografica.album_model",string="Albumes")
    discografica_id = fields.Many2one("discografica.discografica_model",string="Discografica")    
    gira_ids = fields.Many2many("discografica.gira_model",string="Giras")
    

    @api.depends('albumes_ids')
    def num_Albumes(self):
        self.ensure_one()
        self.num_Albumes=len(self.albumes_ids)