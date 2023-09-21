import mysql.connector

conexao = mysql.connector.connect(
    host='',  ##SEU HOST
    user='',  #SEU USER
    password='',  #SUA SENHA
    database='',  #NOME DO SEU BANCO DE DADOS
)
cursor = conexao.cursor()

'''PARA USAR CADA UMA DAS FUNÇÕes, RETIRE DE COMENTÁRIO O RESPECTIVO BLOCO'''
# #CREATE
# login = "pedro"
# senha = "12345"
# comando = f'INSERT INTO login(login, senha) VALUES ("{login}", "{senha}")'
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados


# READ
# comando = f'SELECT * FROM login'
# cursor.execute(comando)
# resultado = cursor.fetchall() #ler o banco de dados
# print(resultado)

# UPDATE
# login = "pedro"
# senha = "olamundo"
# comando = f'UPDATE login SET senha = "{senha}" WHERE login = "{login}"'
# cursor.execute(comando)
# conexao.commit()

# #DELETE
# login = 'pedro'
# comando = f'DELETE FROM login WHERE login = "{login}"'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()
