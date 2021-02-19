# -*- coding: utf-8 -*-

from datetime import datetime
from time import time
from odoo.exceptions import ValidationError
from odoo import models, fields, api
import random

class cliente_model(models.Model):
    _name = 'discografica.cliente_model'
    _description = 'Modelo de cliente'
    _sql_constraints=[("sql_cons_check_id","UNIQUE(id_cliente)","Error en cliente, el ID ya existe!"),
                        ("sql_cons_check_dni","UNIQUE(dni)","Error en cliente, el DNI ya existe!"),
                        ("sql_cons_check_telefono","UNIQUE(telefono)","Error en cliente, el telefono ya existe!"),
                        ("sql_cons_check_email","UNIQUE(email)","Error en cliente, el email ya existe!")]

    foto = fields.Binary(string="Foto")
    id_cliente = fields.Char(string="ID cliente", readonly=True,index=True,default=lambda self: str(int(time())))
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True, index=True, size=9)
    fecha_nacimiento = fields.Date(string="Fecha nacimiento",required=True)
    telefono = fields.Char(string="Telefono",required=True,index=True,size=9)
    email = fields.Char(string="Email",required=True,index=True)    

    #RELACIONES
    entrada_ids=fields.One2many("discografica.entrada_model","cliente_id","Comprador")
       
            
    @api.constrains("dni")
    def _validacionDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        for i in num:
            if not i.isnumeric():
                raise ValidationError("los 8 primeros digitos del DNI solo pueden ser numericos")
        posi = int(num) % 23
        if letra != letras[posi]:
            raise ValidationError("DNI no valido")
        if len(self.dni) != 9:
            raise ValidationError("El DNI debe contener 9 caracteres")
        if letra.isnumeric():
            raise ValidationError("El DNI debe terminar con una letra")
        

    @api.constrains('telefono')
    def _validarTelefono(self):
        if len(self.telefono)!=9:
            raise ValidationError("El telefono debe tener 9 digitos")

    @api.constrains('email')
    def _validarEmail(self):
        if '@' and '.' not in self.email:
            raise ValidationError("El email debe contener un '@' y un '.'")

    @api.constrains('fecha_nacimiento')
    def _mayorDeEdad(self):
        anyoHoy= datetime.today().year
        anyoNac = self.fecha_nacimiento.year
        if (anyoHoy - anyoNac) < 18:
            raise ValidationError("Debe de ser mayor de edad")
