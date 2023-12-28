from composition import composition
from produit import Produit
from elementaire import Elementaire
from composee import Compose
from collections import namedtuple, defaultdict,deque


p1 = Elementaire("i5", "jyjtu", 65)
p2 = Elementaire("ram", "fyghujbdt33", 35)
co1 = composition(p1, 20)
co2 = composition(p2, 100)

c1 = Compose("HP", "4f3tfy", 56, )

listeproduit = [p1, p2, c1]
def afficheprix (listeproduit):
    for i in  listeproduit :
        if type(i) == Elementaire :
            print("prix de ", i.Getnom, "est", i.getPrixHT)
    
        else :
            prix = 0
            for e in i.Getliste:
                prix += e.Getproduit.GetprixAchat
            print("prix de ", i.Getnom ,"est", prix)

afficheprix(listeproduit)
Description = namedtuple('Description', ['Produit','Detail'])

D1 = Description(p1.Getnom, p1._str_())
D2 = Description(p2.Getnom, p2._str_())
D3 = Description(c1.Getnom, c1._str_())

print("The details of product are :", D1.Detail)

des1 = {}
des1 = D1

des2 = {}
des2 = D2

des3 = {}
des3 = D3

listeDescription = defaultdict()

listeDescription[1] = des1
listeDescription[2] = des2
listeDescription[3] = des3  

DeqDescription = {}
DeqDescription = deque()

DeqDescription.append(des1)  
DeqDescription.append(des2)  
DeqDescription.append(des3)