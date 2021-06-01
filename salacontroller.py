from datetime import datetime
from sala import sala
class salacontroller:
    def __init__(self):
        self.listasala={}  
            
    def addsala(self,sala):
        if sala.getNombre() not in self.listasala:
                self.listasala[sala.getNombre()] = sala
                return True
        return False
    def registrarevento(self,nombre,dni,fecha):
        if nombre in self.listasala:
            if self.listasala[nombre].setRegistro(dni,fecha):
                return True
        return False     

    def listar(self):
        return self.listasala                  
    def Comprobardni(self,dni):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
        letra = dni[-1].upper()
        num = dni[:-1]

        if (letra.isalpha() == False):
            return False
        if len(dni) != 9:
            return False
        else:
            letr = letras[int(num)%23]
            if (letra != letr):
                return False
        return True    
    def registrarfinalizado(self,nombre,dni,fecha):
        if nombre in self.listasala:
            if self.listasala[nombre].setFinalizado(dni,fecha):
                return True
        return False    

    def comprobarfecha(self,nombre,fecha):
        if nombre in self.listasala:
            self.listasala[nombre].comprobar(fecha)               