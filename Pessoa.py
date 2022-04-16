import mysql.connector as mysql

class Pessoa:
    def __init__(self, nome:str, telefone:int, endereco:object)->None:
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco
    
    def listar(self):
        pass

    def editar(self):
        pass

    def deletar(self):
        pass

    def _conectar_mysql(self, comando:str):
        conexao = mysql.connect(host="localhost", user="root", password="", database="restaurante")
        cursor = conexao.cursor()
        cursor.execute(comando)

        if "SELECT" in comando:
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()
            return resultado
        else:
            conexao.commit()
        cursor.close()
        conexao.close()