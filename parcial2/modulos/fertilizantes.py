import productos_control

class Fertilizantes(productos_control.ProductosControl):
    def __init__(self, registroICA, nombreProducto, frecuenciaAplicacion, valorProducto , fechaUltimaAplicacion):
        super().__init__(registroICA, nombreProducto, frecuenciaAplicacion, valorProducto)

        if registroICA is None and nombreProducto is None and  frecuenciaAplicacion is None and  valorProducto is None and  fechaUltimaAplicacion is None:
            raise(TypeError('No se ingresaron los atributos'))
        
        if registroICA == '' or nombreProducto == '' or  frecuenciaAplicacion == ''or  valorProducto == '' or  fechaUltimaAplicacion == '':
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

        self.__fechaUltimaAplicacion = fechaUltimaAplicacion

    @property 
    def fechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion
    
    @fechaUltimaAplicacion.setter
    def fechaUltimaAplicacion(self, nuevaFecha):
        self.__fechaUltimaAplicacion = nuevaFecha