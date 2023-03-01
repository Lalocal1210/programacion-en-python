class Personaje:
    
    # Constructor
    def __init__(self,esp,name,alt):
        self.__especie = esp
        self.__nombre = name
        self.__altura = alt
    
    #definir metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo")
    
    def lanzarGranadas(self):
        print("El personaje "+self.nombre+"lanzo la granada")
    
    def recargarArma(self,municiones):
        cargador = 10
        cargador += municiones
        print(f"El arma recargada tiene {cargador} balas")
    
    # Gets y sets
        
    def getEspecie(self):
         return self.__especie
    def setEspecie(self,esp):
         self.__especie= esp
         
    def getNombre(self):
         return self.__nombre
    def setNombre(self,nom):
         self.__nombre= nom
 
    def getAltura(self):
         return self.__altura
    def setAltura(self,alt):
         self.__altura= alt