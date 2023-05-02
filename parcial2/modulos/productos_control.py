class ProductosControl:
    def __init__(self , registroICA , nombreProducto , frecuenciaAplicacion , valorProducto):

        if registroICA is None and nombreProducto is None and  frecuenciaAplicacion is None and  valorProducto is None:
            raise TypeError('No se ingresaron los atributos')
        
        if registroICA == '' or nombreProducto == '' or  frecuenciaAplicacion == ''or  valorProducto == '':
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


        self.__registriICA = registroICA
        self.__nombreProducto = nombreProducto
        self.__frecuenciaAplicacion = frecuenciaAplicacion
        self.__valorProducto = valorProducto

    @property 
    def registroICA(self):
        return self.__registriICA
    
    @registroICA.setter
    def registroICA(self, nuevoRegistro):
        self.__registriICA = nuevoRegistro

    @property 
    def nombreProducto(self):
        return self.__nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(self, nuevoNombre):
        self.__nombreProducto = nuevoNombre
    
    @property 
    def frecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion
    
    @frecuenciaAplicacion.setter
    def frecuenciaAplicacion(self, frecuenciDias):
        self.__frecuenciaAplicacion = frecuenciDias

    @property 
    def valorProducto(self):
        return self.__valorProducto * 1
    
    @valorProducto.setter
    def valorProducto(self, nuevoValor):
        self.__valorProducto = nuevoValor
