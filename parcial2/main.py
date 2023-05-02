from modulos.productos_control import ProductosControl
from modulos.control_plagas import ControlPlagas
from modulos.antibioticos import Antibioticos
from modulos.fertilizantes import Fertilizantes
from modulos.facturas import Facturas
from modulos.cliente import Cliente

productoControl = ControlPlagas(1244 , "hola" , "2 veces" , 6000 , 30)
# print(productoControl.__dict__)
print(ControlPlagas.__bases__) #muestra que esta clase es una subclace de (<class 'modulos.productos_control.productosControl'>,)
print(Fertilizantes.__bases__) #muestra que esta clase es una subclace de (<class 'modulos.productos_control.productosControl'>,)
print(Antibioticos.__bases__) #muestra que esta clase no es una subclace: (<class 'object'>,)
print(ProductosControl.__bases__) #muestra que esta clase no es una subclace: (<class 'object'>,)
producto2 = Fertilizantes(1244 , "hola" , "2 veces" , 20000 , "25/04/2023")
producto3 = Antibioticos("sulfadicina", 300, "Bovino" , 2500)
factura = Facturas("2/01/2024")
factura.ProductosControl = productoControl
factura.ProductosControl = producto2
factura.pcantibioticos = producto3
print(factura.valorTotal)



