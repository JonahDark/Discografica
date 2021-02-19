# -*- coding: utf-8 -*-

import random
from datetime import datetime
from time import time
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class entrada_model(models.Model):
    _name = 'discografica.entrada_model'
    _description = 'Modelo de entrada'
    _sql_constraints = [("sql_cons_check_id_entrada",
                         "UNIQUE(id_entrada)", "Error en la entrada, el id ya existe")]

    name = fields.Char(string="ID entrada", readonly=True,index=True, default=lambda self: str(int(time())))
    precio = fields.Float(string="Precio", required=True,default=25.0, readonly=True)
    iva = fields.Selection([('21', '21%'), ('15', '15%'),('7', '7%'), ('0', '0%')], string="IVA", default='21')
    cantidad = fields.Integer(string="Cantidad", required=True, default=1)
    total = fields.Float(string="Total:", readonly=True,compute="calculaTotal", store=True)
    active = fields.Boolean(readonly=True, default=True)

    # RELACIONES
    concierto_id = fields.Many2one(
        "discografica.concierto_model", string="Concierto")

    cliente_id = fields.Many2one(
        "discografica.cliente_model", string="Cliente")

    @api.depends('iva', 'precio', 'cantidad')
    def calculaTotal(self):
        self.ensure_one()
        _total = 0
        _total = (self.precio * int(self.iva) /
                  100 + self.precio) * self.cantidad
        self.total = _total

    @api.depends('entrada_ids')
    def limpiaEntradasVendidas(self):
        entradasVendidas = self.search([("active", "=", "True")])
        for rec in entradasVendidas:
            rec.active = False

    def eliminaHistorial(self):
        historialEntradasVendidas = self.search([("active", "=", "False")])
        for rec in historialEntradasVendidas:
            rec.unlink()
