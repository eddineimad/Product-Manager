class composition:


    def _init_(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def get_produit(self): 
        return self.__produit
    
    def set_produit(self, newreference) :
        self.__reference = newreference

    @property
    def get_quantite(self):
        return self.__quantite
    
    def set_quantite(self, newprix):
        self.__prix_achat = newprix
    
    
    def _str_(self):
        return f"""produit: {self.__produit},quantite: {self.__quantite}"""

    def _eq_(self, other):
        if (self.get_produit == other.get_produit)and(self.get_quantite == other.get_quantite):
            return True
        else:
            return False