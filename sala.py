class sala:
    def __init__(self,nombre,capacidad,precio) :
        self.nombre=nombre
        self.capacidad=capacidad
        self.precio=precio
        self.acumulados=0
        self.numreserva=0
        self.reservas={}
        self.finalizado=[]

    def getNombre(self):
        return self.nombre
    def getCapacidad(self):
        return self.capacidad
    def getPrecio(self):
        return self.precio
    def getAcumulados(self):
        return self.acumulados
    def getNumreserva(self):
        return self.numreserva                              
    def setRegistro(self,dni,fecha):
        for dni in self.reservas:
            if fecha in self.reservas[dni]:
                return False
        for fecha in range (0,len(self.finalizado)):
            return False
        else:
            if dni not in self.reservas.keys():
                self.reservas = {dni:[fecha]}
                self.numreserva+= 1
                return True
            else:
                self.reservas[dni].append(fecha)
                self.numreserva+= 1
                return True
    def mostrarParticipantes(self):
        ordenados = sorted(self.finalizado, key=lambda fecha : fecha[1])
      

        return ordenados        
    def setFinalizado(self,dni,fecha):
        if dni in self.reservas:
            self.reservas[dni].remove(fecha)
            self.finalizado.append((dni,fecha))
            self.acumulados+= self.precio
            if len(self.reservas[dni])==0:
               del self.reservas[dni]
            return True
        else:
            return False
    def getReservas(self):
        return self.reservas    
    def comprobar(self,fecha):
        if fecha in self.reservas:
                return True
        return False
             
