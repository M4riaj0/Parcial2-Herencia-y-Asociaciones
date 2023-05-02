import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import pytest
import cliente

def test_no_ingresar_datos():
    with pytest.raises(TypeError, match="No se ingresaron los datos"): 
        ingreso_cliente = cliente.Cliente(None, None) 

def test_ingresar_datos():
    with pytest.raises(TypeError, match='Debes ingresar todos los campos'): 
        datos_ingresados = cliente.Cliente(nombreCliente='', cedulaCliente='') 
        pass
    
def test_ingresar_solo_nombre():
    with pytest.raises(TypeError, match="Solo se ingreso un dato"):
        dato_ingresado = cliente.Cliente(nombreCliente='Majo', cedulaCliente = None)

def test_ingresar_solo_cedula():
    with pytest.raises(TypeError, match="Solo se ingreso un dato"):
        dato_ingresado = cliente.Cliente(cedulaCliente='123', nombreCliente= None) 
        
def test_cedula_numerica():
    with pytest.raises(ValueError, match='La cédula debe contener solo números'):
        datos_ingresados = cliente.Cliente(nombreCliente='Juan', cedulaCliente='yqweur43') 

def test_solo_texto_nombre():
    with pytest.raises(ValueError, match='El nombre debe contener solo letras'):
        cliente_in = cliente.Cliente('Ca#mi%', '123')