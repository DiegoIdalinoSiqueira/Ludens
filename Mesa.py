import mysql.connector as mysql, PySimpleGUI as sg

class Mesa:
    def __init__(self, numero:int, lugar:str, capacidade:int) -> None:
        self.__numero = numero
        self.__lugar = lugar
        self.__reservada = 0
        self.__data_reserva = ''
        self.__capacidade = capacidade
        self.__reservada_para = None

    def cadastrar(self):
        comando = f"INSERT INTO mesa VALUES ({self.__numero}, '{self.__lugar}', {self.__reservada}, '{self.__data_reserva}', {self.__capacidade}, null)"
        self.__conectar_mysql(comando)
    
    def listar(self):
        comando = "SELECT * FROM mesa"
        resultado = self.__conectar_mysql(comando)
        return resultado

    def editar(self,valores:dict):
        comando = f"UPDATE mesa SET numero = {valores['NUMERO']}, lugar = '{valores['LUGAR']}', capacidade = {valores['CAPACIDADE']} WHERE numero = {valores['NUMERO-ATUAL']}"
        self.__conectar_mysql(comando)

    def deletar(self, numero:int):
        comando = f"DELETE FROM mesa WHERE numero = {numero}"
        self.__conectar_mysql(comando)
    
    def editar_reserva(self, valores:dict):
        comando = f"UPDATE mesa SET reservada = {valores['RESERVADA']}, data_reserva = '{valores['DATA_RESERVA']}', reservada_para = {valores['RESERVADA_PARA']} WHERE numero = {valores['NUMERO']}"
        self.__conectar_mysql(comando)
        
    def __conectar_mysql(self, comando:str):
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

#janela mesas#
def janela_mesas():
    layout = [
        [sg.Button('Cadastrar Mesa', key='-CADASTRAR-MESA-', size=(18))],
        [sg.Button('Listar Mesas', key='-LISTAR-MESA-', size=(18))],
        [sg.Button('Voltar', key='-MESA-VOLTAR-')]
    ]
    return sg.Window("Ludens", layout, finalize=True, element_justification='c')

# JANELA CADASTRO DE MESA #
def cadastro_mesas():
    mesas = [
        [sg.Text('CADASTRAR MESA', pad=(15))],
        [sg.Text("Número:", size=(13)), sg.InputText(key = "NUMERO-MESA")],
        [sg.Text("Lugar:", size=(13)), sg.Input(key="LUGAR-MESA")],
        [sg.Text("Capacidade:", size=(13)), sg.InputText(key="CAPACIDADE-MESA")]
    ]

    layout = [
        [sg.Column(mesas)],
        [sg.Button("Cadastrar", key="-CADASTRAR-MESA-CONFIRM-"), sg.Button("Cancelar", key='-MESA-CADASTRO-CANCEL-', button_color="red")]
    ]
    return sg.Window("Ludens", layout,finalize=True)

# JANELA LISTAR MESA #
def listar_mesa(mesas):
    linhas = []
    for i in mesas:
        linhas.append(i)
    
    if len(linhas) == 0:
        layout = [
            [sg.Text('Não existem mesas cadastradas')],
            [sg.Button('Voltar', key='LISTAR-MESA-VOLTAR')]
        ]
        return sg.Window('Lista de mesas', layout, finalize=True, element_justification='c')
    else:
        layout = [
            [sg.Text('Lista de mesas')],
            [sg.Table(linhas, ['NÚMERO', 'LUGAR', 'RESERVADA', 'DATA DA RESERVA','CAPACIDADE', 'RESERVADA PARA'], justification='left', key='-TABELA-MESAS-')],
            [sg.Button('Editar dados', key='EDITAR-MESA'), sg.Button('Excluir', button_color='red',key='EXCLUIR-MESA')],
            [sg.Button('Voltar', key='LISTAR-MESA-VOLTAR')]
        ]
        return sg.Window('Lista de mesas', layout, finalize=True)

# EDITAR MESA #
def editar_mesa(mesa):
    layout = [
        [sg.Text('EDITAR MESA', pad=(0,15))],
        [sg.Text("Número:", size=(10)), sg.Input(mesa[0], key = "NUMERO")],
        [sg.Text("Lugar:", size=(10)), sg.Input(mesa[1], key="LUGAR")],
        [sg.Text("Capacidade:", size=(10)), sg.Input(mesa[4], key="CAPACIDADE")],
        [sg.Text('Número atual:', size=(10)), sg.Input(mesa[0], key="NUMERO-ATUAL", readonly=True)],
        [sg.Button('Confirmar', button_color='green', key='EDITAR-MESA-CONFIRM'), sg.Button('Voltar', key='EDITAR-MESA-VOLTAR')]
    ]
    return sg.Window('Editar mesa', layout, finalize=True)

# DELETAR MESA #
def deletar_mesa(mesa):
    layout = [
        [sg.Text('DADOS DA MESA', size=(15), pad=(0,15))],
        [sg.Text("Número:", size=(13)), sg.Input(mesa[0], key = "NUMERO-MESA", readonly=True)],
        [sg.Text("Lugar:", size=(13)), sg.Input(mesa[1], key="LUGAR-MESA", readonly=True)],
        [sg.Text("Capacidade:", size=(13)), sg.Input(mesa[4], key="CAPACIDADE-MESA", readonly=True)],
        [sg.Button('Excluir', button_color='red', key='EXCLUIR-MESA-CONFIRM'), sg.Button('Voltar', key='EXCLUIR-MESA-VOLTAR')]
    ]
    return sg.Window('Deletar mesa', layout, finalize=True)