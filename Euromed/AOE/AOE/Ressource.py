

#from Euromed.AOE.AOE.definitions import LES_RESSOURCES as ress

class Ressource:

    def __init__(self):
        self.nbRessources = 0
        self.typeRessource = ""

    def __init__(self, nbRess, laRess):
        self.nbRessources = nbRess
        self.typeRessource = laRess

    def getTypeRessource(self):
        return self.typeRessource

    def getNbRessources(self):
        return self.nbRessources

    def setTypeRessource(self, typeRess):
        self.typeRessource = typeRess

    def setNbRessources(self, nbRess):
        self.nbRessources = nbRess