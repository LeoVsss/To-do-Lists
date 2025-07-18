import mariadb
rodando=True

conexao = mariadb.connect(
  user="root",
  password="root",
  database="Banco1",
  port=3307 

)

class tarefas:
  def __init__(self,conexao):
    self.connecting = conexao
    self.sql= conexao.cursor() 

  def Adicionar(self,add):
      try: 
        self.sql.execute("insert into afazeres(tarefas) values (?)",[add])                
        self.connecting.commit()
        print("Enviada com sucesso \n")
      except:
        print("Erro na InserçãO \n")  

  def Remover(self,remove):
    try:
      self.sql.execute("Delete from afazeres where tarefas = (?) ",[remove]) 
      self.connecting.commit()
      print("Removido com sucesso \n")
    except:
      print("Erro ao remover, você deve ter digitado o nome errado \n")  

  def Listar(self):
    try:
     self.sql.execute("Select * from afazeres")
     resultados = self.sql.fetchall()
     for registros in resultados:
       if registros[1]:
         print(registros)
     self.connecting.commit()
     
    except:
     print("Erro ao listar")


  def Concluidas(self,done):
     try:
        
      self.sql.execute("SELECT situacao FROM afazeres WHERE tarefas = ?", (done,))
      resultado = self.sql.fetchone()
      
      if resultado is None:
    
       print(f"ERRO: A tarefa '{done}' não existe na sua lista.\n")
       return

      status_atual=resultado[0]

      if (status_atual=='Concluída'):
        print(f"AVISO: A tarefa '{done}' já está marcada como 'Concluída'.\n")

      else:  
       self.sql.execute("Update afazeres set situacao = 'Concluída' where tarefas = (?)",[done])
       self.connecting.commit()
       print(f"tarefa {done} marcada como 'Concluída' \n")
     except:
       print("Erro ao atualizar situação \n")  

  def Sair(self):
    print("Finalizando o programa \n")
    self.connecting.close()   



Meus_Afazeres=tarefas(conexao)

while rodando==True:

  entrada = (input("Digite o que gostaria de fazer: 1-Inserir, 2-Remover, 3-Listar, 4-Feita, 5-Sair \n"))

  try:
        comando = int(entrada)
  except ValueError:
        print("\n[ERRO] Entrada inválida. Por favor, digite apenas um número.\n")
        continue 

  if (comando==1):
    Afazer = input("Digite a tarefa que vai ser inserida: \n")
    Meus_Afazeres.Adicionar(Afazer)

  if (comando==2):
    Remove = input("Digite qual tarefa gostaria de remover: \n")
    Meus_Afazeres.Remover(Remove)

  if (comando==3): 
   Meus_Afazeres.Listar()

  if (comando==4):
    Concluida=input("Digite qual tarefa foi concluída: \n")
    Meus_Afazeres.Concluidas(Concluida) 

  if (comando==5): 
    Meus_Afazeres.Sair()
    break   
  
 