import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import pytest
import productos_control
import control_plagas


def test_no_ingresar_datos():
    with pytest.raises(TypeError, match='No se ingresaron los atributos'): 
        ingreso_pcontrol = control_plagas.ControlPlagas(None, None, None, None, None)

def test_ingresar_datos_vacios():
    with pytest.raises(TypeError, match='Debes ingresar todos los campos'): 
        datos = control_plagas.ControlPlagas(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, periodoCarencia = '' ) 
    
def test_ingresar_solo_ICA():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = control_plagas.ControlPlagas(registroICA = 12345, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, periodoCarencia = '' )
        pass
def test_ingresar_solo_nombre():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = control_plagas.ControlPlagas(registroICA = None, nombreProducto = 'Nombre', frecuenciaAplicacion = '', valorProducto = None, periodoCarencia = '' )

def test_ingresar_solo_frecuencia():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = control_plagas.ControlPlagas(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '3 dias', valorProducto = None, periodoCarencia = '' ) 

def test_ingresar_solo_valor():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = control_plagas.ControlPlagas(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = 15000, periodoCarencia = '' ) 
  
def test_ingresar_solo_periodo_carencia():
    with pytest.raises(TypeError, match="Debes ingresar todos los campos"):
        datos = control_plagas.ControlPlagas(registroICA = None, nombreProducto = '', frecuenciaAplicacion = '', valorProducto = None, periodoCarencia = '30 dias' ) 
  
def test_registro_no_numerico():
    with pytest.raises(ValueError, match='El registro ICA debe contener solo números'): 
        datos = control_plagas.ControlPlagas(registroICA = '123m%45', nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = 15000, periodoCarencia = '30 dias' ) 

def test_valor_no_numerico():
    with pytest.raises(ValueError, match='El valor del producto debe contener solo números'): 
        datos = control_plagas.ControlPlagas(registroICA = 12334, nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = '15%yy000', periodoCarencia = '30 dias' ) 

def test_solo_texto():
    datos = control_plagas.ControlPlagas(registroICA = '12334' , nombreProducto = 'Nombre', frecuenciaAplicacion = '3 dias', valorProducto = '15000', periodoCarencia = '30 dias' ) 