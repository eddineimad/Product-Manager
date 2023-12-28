from abc import ABC, abstractmethod
class Produit(ABC) :
    def _init_(self, nom, code) :
        self.__nom = nom
        self.__code = code

    @property
    def Getnom(self) :
        return self.__nom
    
    @property
    def Getcode(self) :
        return self.__code
    
    def Setnom(self, nom) :
        self.__nom = nom

    def Setcode(self, code) :
        self.__code = code

    def _str_(self):
        return  "; Nom: " + self.__nom + "; Code: " + self.__code
        

    def _eq_(self, other):
        return self.__code == other.__code
    
    @abstractmethod
    def GetprixHT(self) :
        pass