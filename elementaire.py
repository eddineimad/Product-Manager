from produit import*

class Elementaire (Produit):
    def _init_(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    @property

    def prixAchat(self):
        return self.__prixAchat
    
    def getPrixHT(self):
        return self.__prixAchat