from produit import*

class Compose (Produit) :
    def _init_(self, nom, code, frais, tva, liste):
        super()._init_(nom, code)
        self.__frais = frais
        self.__tva = tva
        self.__liste = liste

    @property
    def Getfrais(self) :
        return self.__frais
    
    @property
    def Gettva(self) :
        return self.__tva
    
    @property
    def Getliste(self) :
        return self.__liste
    
    def Setfrais(self, frais) :
        self.__frais = frais

    def Settva(self, tva) :
        self.__tva = tva
    
    def Setliste(self, liste) :
        self.__liste = liste

    def _str_(self):
        return super()._str_(), "Frais de Fabrication: ", str(self.__frais), "TVA: " , str(self.__tva), "Liste des contitiants: ", self.__liste
    
    def GetprixHT(self):
        return self.__frais + (self.__frais / 100) * self.__tva