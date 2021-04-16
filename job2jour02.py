class Personne:
    def __init__(self,fname,fprenom):
        self.name=fname
        self.prenom=fprenom
    def se_presenter(self):
        print("My name is",self.name,self.prenom)

class Livre:
    def __init__(self,titre,auteur):
        self.titre=titre
        self.auteur=auteur
    def showtitre(self):
        print("Book name",self.titre)

class auteur(Personne,Livre):
    def __init__(self,fname,fprenom,oeuvre):
        super().__init__(self,fname,fprenom)
        self.oeuvre=oeuvre

    def listeroeuvre(self):
        print("List of books",self.oeuvre)

    def ecrireunlivre(self):
        super().titre=str(input("new book:"))
        self.oeuvre=self.oeuvre + super().titre
        
