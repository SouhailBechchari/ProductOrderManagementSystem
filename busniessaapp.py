

class Produit:
    nbprd = 0

    def __init__(self, reference, designation, prixachat, prixvente):
        self.reference = reference
        self.designation = designation
        self.prixachat = prixachat
        self.prixvente = prixvente
        Produit.nbprd += 1

    @property
    def get_reference(self):
        return self.reference

    @property
    def get_designation(self):
        return self.designation

    @property
    def get_prixachat(self):
        return self.prixachat

    @property
    def get_prixvente(self):
        return self.prixvente

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value

    @property
    def prixachat(self):
        return self._prixachat

    @prixachat.setter
    def prixachat(self, value):
        self._prixachat = value

    @property
    def prixvente(self):
        return self._prixvente

    @prixvente.setter
    def prixvente(self, value):
        self._prixvente = value

    def modifier_prixachat(self, nouveau_prixachat):
        self.prixachat = nouveau_prixachat

    def ajouter_prixvente(self, ajout_prixvente):
        self.prixvente += ajout_prixvente

    def to_string(self):
        return self.__dict__

    def equals(self, other):
        return self.reference == other.reference

class Commande:
    def __init__(self, produit, date, quantite):
        self.produit = produit
        self.date = date
        self.quantite = quantite

    @property
    def get_date(self):
        return self.date

    @property
    def get_quantite(self):
        return self.quantite

    @property
    def set_date(self, value):
        self.date = value

    @property
    def set_quantite(self, value):
        self.quantite = value
    
    def to_string(self):
        return self.__dict__


prd1 = Produit("2222", "knkn", 100, 5001)
prd2 = Produit("4353", "uggj", 2000, 53476)
prd3 = Produit("5673", "jkhhk", 2001, 2789)
com1 = Commande(prd1, "8/9/2018", 777)
com2 = Commande(prd2, "9/3/1999", 455)

print(Produit.nbprd)
print(prd1.to_string())
print(prd2.to_string())
print(prd3.to_string())
print(prd1.equals(prd2))
print(prd2.equals(prd3))
print(com1.to_string())
print(com2.to_string())
