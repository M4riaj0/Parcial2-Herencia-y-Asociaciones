import productos_control

class ControlPlagas(productos_control.ProductosControl):
    def __init__(self, registroICA, nombreProducto, frecuenciaAplicacion, valorProducto, periodoCarencia):
        super().__init__(registroICA, nombreProducto, frecuenciaAplicacion, valorProducto)
        self.__periodoCarencia = periodoCarencia

        if registroICA is None and nombreProducto is None and  frecuenciaAplicacion is None and  valorProducto is None and  periodoCarencia is None:
            raise(TypeError('No se ingresaron los atributos'))
        
        if registroICA == '' or nombreProducto == '' or  frecuenciaAplicacion == ''or  valorProducto == '' or  periodoCarencia == '':
            raise(TypeError('Debes ingresar todos los campos'))
        
        if not nombreProducto.isalpha():
            raise ValueError('El nombre del producto debe contener solo letras')
        try:
            registroICA = int(registroICA)
        except ValueError:
            raise(ValueError('El registro ICA debe contener solo números')) 
        try:
            valorProducto = int(valorProducto)
        except:
            raise(ValueError('El valor del producto debe contener solo números')) 
    
    @property 
    def periodoCarencia(self):
        return self.__periodoCarencia
    
    @periodoCarencia.setter
    def periodoCarencia(self, nuevoPeriodo):
        self.__periodoCarencia = nuevoPeriodo

    @property 
    def valorProducto(self):
        return int(super().valorProducto)
    
    @valorProducto.setter
    def valorProducto(self, nuevoValor):
        super().valorProducto = nuevoValor