from modulos.productos_control import ProductosControl
from modulos.control_plagas import ControlPlagas
from modulos.antibioticos import Antibioticos

class Facturas:
    def __init__(self, fechaFactura):

        if fechaFactura == '':
            raise TypeError('El campo está vacío')

        self.__fechaFactura = fechaFactura
        self.__ProductosControl = []
        self.__Antibioticos = []
    
    @property
    def fechaFactura(self):
        return self.__fechaFactura
    
    @fechaFactura.setter
    def fechaFactura(self, nuevaFecha):
        self.__fechaFactura = nuevaFecha

    @property
    def ProductosControl (self):
        return self.__ProductosControl
    
    @ProductosControl.setter
    def ProductosControl (self, nuevoProducto):
        self.__ProductosControl.append(nuevoProducto)

    @property
    def pcantibioticos (self):
        return self.__Antibioticos
    
    @pcantibioticos.setter
    def pcantibioticos (self, nuevoAntibiotico):
        self.__Antibioticos.append(nuevoAntibiotico)

    @property
    def valorTotal(self):
        valor = 0
        for producto in self.__ProductosControl:
            valor = valor + producto.valorProducto
        for antibiotico in self.__Antibioticos:
            valor = valor + antibiotico.precio
        return valor
    
    
