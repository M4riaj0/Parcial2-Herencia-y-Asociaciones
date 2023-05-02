import sys
import os

path = os.path.abspath('modulos/')
sys.path.append(path)

import pytest
import facturas

def test_ingresar_datos_vacios():
    with pytest.raises(TypeError, match='El campo está vacío'): 
        datos = facturas.Facturas(fechaFactura = '' ) 
        pass
