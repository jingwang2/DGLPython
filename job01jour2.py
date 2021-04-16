class Personne:
    def __init__(self,fname,fprenom):
        self.name=fname
        self.prenom=fprenom
    def se_presenter(self):
        print("My name is",self.name,self.prenom)
a=str(input("name"))
b=str(input("prenome"))
P1=Personne(a,b)
P1.se_presenter()