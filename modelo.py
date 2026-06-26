#filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir
class Filmes:
    def __init__(self, nome, ano, duracao):
      self.__nome = nome.title()
      self.ano = ano 
      self.duracao = duracao 
      self.__curtir = 0
      @property
      def valor_curtir(self):
         return self.__curtir
      
    def valor_nome(self):
         return self.__nome
      
    def curtida (self): 
         self.curtir += 1 

class Series: 
     def __init__(self, nome, ano, temporadas):
      self.__nome = nome.title()
      self.ano = ano 
      self.temporadas = temporadas 
      self.__curtir = 0

     def curtida (self): 
         self.curtir += 1 


peaky_blinders = Series("peaky blinders", 2013,6)
print(peaky_blinders.nome)

avatar = Filmes("Avatar", 2009, 177)
print(avatar.nome)