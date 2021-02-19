# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class concierto_model(models.Model):
    _name = 'discografica.concierto_model'
    _description = 'Modelo de concierto'

    foto=fields.Binary(string="Foto")
    name = fields.Char(string="Nombre", required=True, index=True)
    fecha_hora = fields.Datetime(string="Fecha", required=True, default=datetime.now())
    lugar = fields.Char(string="Lugar", required=True)
    numEntradas = fields.Integer(string="Entradas disponibles", store=True, compute="decrementaEntrada")
    recaudado = fields.Float(string="Recaudado", readonly=True, store=True, compute="acumulaRecaudado")


    # RELACIONES
    artista_ids = fields.Many2many("discografica.artista_model", string="Artista/s")
    gira_id = fields.Many2one("discografica.gira_model", string="Giras")
    entrada_ids = fields.One2many("discografica.entrada_model", "concierto_id", "Entradas Vendidas")

    @api.depends("entrada_ids")
    def acumulaRecaudado(self):
        self.ensure_one()
        _recaudado = 0
        for i in self.entrada_ids:
            _recaudado += i.total
        self.recaudado = _recaudado

    @api.depends('entrada_ids')
    def decrementaEntrada(self):
        self.numEntradas = 2
        self.ensure_one()
        for i in self.entrada_ids:
            self.numEntradas -= i.cantidad
            if self.numEntradas < 0:
                raise ValidationError("No hay suficientes entradas disponibles o las entradas estan agotadas")

    @api.constrains('fecha_hora')
    def fechaLimite(self):
        if datetime.now() >= self.fecha_hora:
            raise ValidationError("Esta fuera de la fecha limite de compra")

    