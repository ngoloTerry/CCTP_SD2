class GrapheNOPLS:
    # Le constructeur __init__ construit un graphe o`u tous les sommets sont isol´es (aucun arc)
    # le dictionnaire est donc vide
    def __init__ (self, sommets): 
        self.som = sommets
        self.dict = dict()
        for x in sommets:
            self.dict[x]={}

    # 1) retourne la liste des sommets du graphe
    def sommets(self):
        return list(self.som)
    
    # 2) ajoute des éléments aux clés du dico du graphe
    def ajouteArc(self, x, y, w=1):
        # il faut vérifier que x et y sont dans le graphe:
        assert x in self.som, "ajouteArc: sommet "+x+" inexistant"
        assert y in self.som, "ajouteArc: sommet "+y+" inexistant"
        # on s'assure qu'il n'y ait pas de dupliqué
        if not y in self.dict[x]:
            self.dict[x].update({y:w})

    # 3) prend une liste de tuple (x,y) afin de les ajouter au graphe
    def ajouteLesArcs(self, larcs):
        for arc in larcs:
            self.ajouteArc(arc[0], arc[1], arc[2]) # en considérant que la liste de tuple accepte en 3ème argument le poids
    
    # 5) retourne une liste de successeurs
    def successeurs(self,x):
        return self.dict[x].keys()
    
    # 6) retourne une liste de prédecesseurs
    def predecesseurs(self,x):
        res = []
        for som in self.dict:
            if x in som:
                res.append(som.key) # va ptet causer une erreur
        return res
    
    # supplémentaire)  retourne le poids d’une arˆete dont les extr´emit´es sont donn´ees en param`etres
    def poids(self, x, y):
        # tout va dépendre de comment se forme la représentation du graphe
        return self.dict[x][y]
    
    # 7) retourne une liste de sucesseurs ET prédecesseurs
    def voisins(self, x):
        # gestion des doublons: manquante

        res = self.predecesseurs(x) + self.successeurs(x)
        return res
    
    # 8)
    def degreSortant(self, x):
        return len(self.successeurs(x))
    
    # 9)
    def degreEntrant(self, x):
        return len(self.predecesseurs(x))
    
    # 10) 
    def degre(self, x):
        return len(self.voisins(x))

    # 11) affiche
    def affiche(self):
        print("Enesemble des sommets: "+self.sommets())
        for elm in self.dict:
            print("Le sommet "+elm+" a pour voisins: "+ self.voisins(elm))
    # Exo2
    # Fonction lesAretes
    def lesAretes(self): # les aretes sont toutes les paires "clé-élément" du dico
        res = []
        for cle in self.sommets():
            for elm in self.sommets():
                if elm in self.dict[cle]: # pas la peine de gérer les doublons: ce sont des aretes pas des arcs.
                    res.append((cle,elm, self.poids(cle,elm)))


    # Fonction SupprArc
    def supprimeArete(self,x,y): # supprimer une arete = enlever l'element de la clé, des deux côtés.
        assert y in x, "supprimeArete: l'arete ("+str(x)+","+str(y)+") n'existe pas."
        assert x in y, "supprimeArete: l'arete ("+str(y)+","+str(x)+") n'existe pas."

        del self.dict[x][y]
        del self.dict[y][x]

