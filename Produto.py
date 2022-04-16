import mysql.connector as mysql, PySimpleGUI as sg

class Produto:
    def __init__(self, nome:str, preco:float, codigo:int, estoque:int, porcent_lucro:float) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__codigo = codigo
        self.__estoque = estoque
        self.__porcent_lucro = porcent_lucro
    
    def cadastrar(self):
        comando = f"INSERT INTO produto VALUES ('{self.__nome}', {self.__preco}, {self.__codigo}, {self.__estoque}, {self.__porcent_lucro})"
        self.__conectar_mysql(comando)
    
    def listar(self):
        comando = f"SELECT * FROM produto"
        resultado = self.__conectar_mysql(comando)
        return resultado

    def busca_especifica(self, pesquisa:str):
        comando = f"SELECT * FROM produto WHERE nome LIKE '{pesquisa}%'"
        resultado = self.__conectar_mysql(comando)
        return resultado

    def editar(self, valores:dict):
        comando = f"UPDATE produto SET nome = '{valores['NOME']}', preco = {valores['PRECO']}, codigo = {valores['CODIGO']}, porcent_lucro = {valores['PORCENT_LUCRO']} WHERE codigo = {valores['CODIGO-ATUAL']}"
        self.__conectar_mysql(comando)

    def deletar(self, codigo:int):
        comando = f"DELETE FROM produto WHERE codigo = {codigo}"
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
        
# JANELA - PRODUTOS #
def janela_produtos():
    layout = [[sg.Button('Cadastrar produtos', key='-CADASTRARPRO-', size=(18))],
              [sg.Button('Listar Produtos', key='-LISTARPRO-', size=(18))],
              [sg.Button('Voltar', key='-PRODUTOS-VOLTAR-')]
    ]
    return sg.Window('Produtos', layout, finalize=True, element_justification='c')

# JANELA DE CADASTRO #
def tela_cadastrar_prod():
    layout = dados_produtos = [
        [sg.Text('DADOS DOS PRODUTOS')],
        [sg.Text("Nome:", size=(8)), sg.InputText(key = "NOME-PRODUTO")],
        [sg.Text("Preço:", size=(8)), sg.Input(key="PRECO-PRODUTO")],
        [sg.Text("Código:", size=(8)), sg.Input(key="CODIGO-PRODUTO")],
        [sg.Text("Estoque:", size=(8)), sg.InputText(key="ESTOQUE-PRODUTO")],
        [sg.Text("Lucro:", size=(8)), sg.Input(key="LUCRO-PRODUTO")]
    ]

    layout = [
        [sg.Column(dados_produtos)],
        [sg.Button("Cadastrar", key="-CADASTRARP-"), sg.Button("Cancelar", key='-PRODUTOS-CADASTRO-CANCEL-', button_color="red")]
    ]
    return sg.Window('Ludens', layout, finalize=True)

# JANELA DE LISTAGEM
def janela_listar_produto(produtos):
    linhas = []
    for i in produtos:
        linhas.append(i)

    if len(produtos) == 0:
        layout = [
            [sg.Text('Não existem produtos cadastrados')],
            [sg.Button('Voltar', key='-VOLTAR-LISTA-PRODUTOS-')]
        ]
        return sg.Window("LISTA DE PRODUTOS", layout, finalize=True, element_justification='c')
    else:
        layout = [
            [sg.Text("PRODUTOS CADASTRADOS")],
            [sg.Text('Pesquisa:'), sg.Input(enable_events=True, key='PESQUISA')],
            [sg.Table(linhas, ['NOME', 'PREÇO', 'CÓDIGO', 'ESTOQUE', 'PROCENTAGEM DE LUCRO'], justification='left', key='TABELA-PRODUTOS')],
            [sg.Button("Editar dados", key='-EDITAR-PRODUTO-'), sg.Button("Excluir", button_color='red', key='-EXCLUIR-PRODUTO-')],
            [sg.Button('Voltar', key='-VOLTAR-LISTA-PRODUTOS-')]
        ]
        return sg.Window("LISTA DE PRODUTOS", layout, finalize=True)

# JANELA EDITAR PRODUTO #
def editar_produto(produto):
    layout = [
        [sg.Text('DADOS DO PRODUTO')],
        [sg.Text("Nome:", size=(9)), sg.Input(produto[0], key='NOME')],
        [sg.Text("Preço:", size=(9)), sg.Input(produto[1], key='PRECO')],
        [sg.Text("Código:", size=(9)), sg.Input(produto[2], key='CODIGO')],
        [sg.Text("Estoque:", size=(9)), sg.Input(produto[3], key='ESTOQUE')],
        [sg.Text("Lucro:", size=(9)), sg.Input(produto[4], key='PORCENT_LUCRO')],
        [sg.Text("Código atual:", size=(9)), sg.Input(produto[2], key='CODIGO-ATUAL',readonly=True)],
        [sg.Button('Confirmar', button_color='green', key='-EDITAR-PRODUTO-CONFIRM-'), sg.Button('Voltar', key='EDITAR-PRODUTO-VOLTAR')]
    ]
    return sg.Window('Editar produto', layout, finalize=True)

# JANELA DELETAR PRODUTO #
def excluir_produto(produto):
    layout = [
        [sg.Text('DADOS DO PRODUTO')],
        [sg.Text("Nome:", size=(8)), sg.Input(produto[0], readonly=True)],
        [sg.Text("Preço:", size=(8)), sg.Input(produto[1], readonly=True)],
        [sg.Text("Código:", size=(8)), sg.Input(produto[2], key='-CODIGO-PROD-', readonly=True)],
        [sg.Text("Estoque:", size=(8)), sg.Input(produto[3], readonly=True)],
        [sg.Text("Lucro:", size=(8)), sg.Input(produto[4], readonly=True)],
        [sg.Button('Excluir', button_color='red', key='-EXCLUIR-PRODUTO-CONFIRM-'), sg.Button('Voltar', key='EXCLUIR-PRODUTO-VOLTAR')]
    ]
    return sg.Window('Excluir produto', layout, finalize=True)