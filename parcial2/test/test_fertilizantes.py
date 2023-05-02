import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import pytest
import fertilizantes


def test_no_ingresar_datos():
    with pytest.raises(TypeError, match='No se ingresaron los atributos'): 
        ingreso_fertilizante = fertilizantes.Fertilizantes(None, None, None, None, None)

def test_ingresar_datos_vacios():
    with pytest.raises(TypeError, match='Debes ingresar todos los campos'): 
        datos = fertilizantes.Fertilizantes(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, fechaUltimaAplicacion = '' ) 
    
def test_ingresar_solo_ICA():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = fertilizantes.Fertilizantes(registroICA = 12345, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, fechaUltimaAplicacion = '' )

def test_ingresar_solo_nombre():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = fertilizantes.Fertilizantes(registroICA = None, nombreProducto = 'Nombre', frecuenciaAplicacion = '', valorProducto = None, fechaUltimaAplicacion = '' )
        pass
def test_ingresar_solo_frecuencia():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = fertilizantes.Fertilizantes(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '3 dias', valorProducto = None, fechaUltimaAplicacion = '' ) 

def test_ingresar_solo_valor():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = fertilizantes.Fertilizantes(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = 15000, fechaUltimaAplicacion = '' ) 
  
def test_ingresar_solo_periodo_carencia():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = fertilizantes.Fertilizantes(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, fechaUltimaAplicacion = '1/05/2023' ) 
  
def test_registro_no_numerico():
    with pytest.raises(ValueError, match='El registro ICA debe contener solo números'): 
        datos = fertilizantes.Fertilizantes(registroICA = '123m%45', nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = 15000, fechaUltimaAplicacion = '1/05/2023' ) 

def test_valor_no_numerico():
    with pytest.raises(ValueError, match='El valor del producto debe contener solo números'): 
        datos = fertilizantes.Fertilizantes(registroICA = 12334, nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = '15%yy000', fechaUltimaAplicacion = '1/05/2023' ) 

def test_solo_texto():
    datos = fertilizantes.Fertilizantes(registroICA = '12334' , nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = '15000', fechaUltimaAplicacion = '1/05/2023' ) 