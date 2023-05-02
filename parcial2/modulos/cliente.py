class Cliente:
    def __init__(self, nombreCliente, cedulaCliente):

        if nombreCliente is None and cedulaCliente is None:
            raise TypeError('No se ingresaron los datos')

        if nombreCliente == '' or cedulaCliente == '':
            raise(TypeError('Debes ingresar todos los campos'))

        if (nombreCliente is None and cedulaCliente != None) or (cedulaCliente is None and nombreCliente != None):
            raise(TypeError('Solo se ingreso un dato'))
        
        if not nombreCliente.isalpha():
            raise ValueError('El nombre debe contener solo letras')
        try:
            cedulaInt = int(cedulaCliente)
        except ValueError:
            raise(ValueError('La cédula debe contener solo números')) 

        self.__nombreCliente = nombreCliente
        self.__cedulaCliente = cedulaCliente
        self.__facturas = []

    @property 
    def nombreCliente(self):
        return self.__nombreCliente
     
    @nombreCliente.setter
    def nombreCliente(self, nuevoNombre):
        self.__nombreCliente = nuevoNombre

    @property 
    def cedulaCliente(self):
        return self.__cedulaCliente
    
    @cedulaCliente.setter
    def cedulaCliente(self, nuevaCedula):
        self.__cedulaCliente = nuevaCedula
    
    @property
    def facturas(self):
        return self.__facturas
    
    @facturas.setter
    def facturas(self, nuevaFactura):
        self.__facturas.append(nuevaFactura)