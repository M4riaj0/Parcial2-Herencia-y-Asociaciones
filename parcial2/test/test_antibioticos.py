import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import pytest
import antibioticos

def test_no_ingresar_datos():
    with pytest.raises(TypeError, match= 'No se ingresaron los atributos'): 
        datos_antibiotico = antibioticos.Antibioticos(None, None, None, None)
        pass

def test_ingresar_datos_vacios():
    with pytest.raises(TypeError, match='Los campos están vacíos'): 
        datos_ingresados = antibioticos.Antibioticos(nombreProducto='', dosisKg='', tipoAnimal='', precio='')

def test_ingresar_mal_animal():
    with pytest.raises(ValueError, match='Recuerde que los tipos de animales son: Bovinos, Caprinos, Porcinos'): 
        datos_ingresado = antibioticos.Antibioticos(nombreProducto='penicilinas', dosisKg='500', tipoAnimal='Gatuno', precio='4000')

def test_ingresar_solo_texto_nombre():
    with pytest.raises(ValueError, match='El nombre del producto debe contener solo letras'): 
        datos_ingresado = antibioticos.Antibioticos(nombreProducto='penic%&ilinas', dosisKg='500', tipoAnimal='Bovino', precio='4000')

def test_ingresar_dosis_kg():
        with pytest.raises(ValueError, match='El dato debe contener solo números'): 
            dato_ingresado = antibioticos.Antibioticos(nombreProducto='penicilinas', dosisKg='80%0I', tipoAnimal='Bovino', precio='4000') 
        
def test_ingresar_precio():
    with pytest.raises(ValueError, match='El dato debe contener solo números'): 
        datos_ingresados = antibioticos.Antibioticos(nombreProducto='penicilinas', dosisKg='500', tipoAnimal='Bovino', precio='400&0') 