import Pessoa, PySimpleGUI as sg, Endereco as e

class Cliente(Pessoa.Pessoa):
    def __init__(self, nome:str, telefone:int, endereco:object) -> None:
        Pessoa.Pessoa.__init__(self, nome, telefone, endereco)

    def cadastrar(self):
        comando = f"INSERT INTO cliente VALUES ('{self._nome}', {self._telefone}, '{self._endereco.rua}', '{self._endereco.numero}', '{self._endereco.bairro}', '{self._endereco.cidade}', '{self._endereco.pais}', {self._endereco.cep}, '{self._endereco.estado}')"
        self._conectar_mysql(comando)

    def listar(self):
        comando = "SELECT * FROM cliente"
        return self._conectar_mysql(comando)

    def editar(self, valores:dict):
        comando = f"UPDATE cliente SET nome = '{valores['NOME']}', telefone = {valores['TELEFONE']}, rua = '{valores['RUA']}', numero = '{valores['NUMERO']}', bairro = '{valores['BAIRRO']}', cidade = '{valores['CIDADE']}', pais = '{valores['PAIS']}', cep = {valores['CEP']}, estado = '{valores['ESTADO']}' WHERE telefone = {valores['TELEFONE-ATUAL']} "
        self._conectar_mysql(comando)

    def deletar(self, telefone:int):
        comando = f"DELETE FROM cliente WHERE telefone = {telefone}"
        self._conectar_mysql(comando)

# JANELAS #
def janela_cliente():
    layout = [
        [sg.Button("Cadastrar Clientes", key="-CADASTRAR-CLI-", size=(18))],
        [sg.Button("Listar Clientes", key="-LISTAR-CLI-", size=(18))],
        [sg.Button("Voltar", key='-CLIENTE-VOLTAR-')]
    ]
    return sg.Window("Ludens", layout, finalize=True, element_justification='c')

def janela_cadastrarC():
    dados_cliente = [
        [sg.Text('DADOS DO CLIENTE')],
        [sg.Text('Nome', size=(8)), sg.InputText(key='NOME-CLIENTE')],
        [sg.Text('Telefone', size=(8)), sg.Input(key='TELEFONE-CLIENTE')]
    ]

    layout = [
        [sg.Column(dados_cliente,  vertical_alignment='t'), sg.Column(e.tela_dados_endereco())],
        [sg.Button("Cadastrar", key="-CADASTRARC-"), sg.Button("Cancelar", key='-CLIENTE-CADASTRO-CANCEL-', button_color="red")]
    ]
    return sg.Window("Ludens", layout, finalize=True,)

# LISTANDO CLIENTES #
def listar_clientes(clientes):
    linhas = []
    for i in clientes:
        linhas.append(i)
    
    if len(linhas) == 0:
        layout = [
            [sg.Text('Não existem clientes cadastrados.')],
            [sg.Button('Voltar', key='LISTAR-CLIENTES-VOLTAR')]
        ]
        return sg.Window('Listar clientes', layout, finalize=True, element_justification='c')
    else:
        layout = [
            [sg.Text('LISTA DE CLIENTES')],
            [sg.Table(linhas, ['NOME', 'TELEFONE'], key='TABELA-CLIENTES', justification='left')],
            [sg.Button('Editar dados', key='EDITAR-CLIENTE'), sg.Button('Excluir', button_color="red", key='EXCLUIR-CLIENTE')],
            [sg.Button('Voltar', key='LISTAR-CLIENTES-VOLTAR')]
        ] 
        return sg.Window('Listar clientes', layout, finalize=True)

# EDITAR CLIENTE #
def editar_cliente(cliente):
    dados_cliente = [
        [sg.Text('DADOS DO CLIENTE')],
        [sg.Text('Nome', size=(10)), sg.InputText(cliente[0], key='NOME')],
        [sg.Text('Telefone', size=(10)), sg.Input(cliente[1], key='TELEFONE')],
        [sg.Text('Telefone atual:', size=(10)), sg.Input(cliente[1], readonly=True, key='TELEFONE-ATUAL')]
    ]

    dados_endereco = [
        [sg.Text("DADOS DE ENDEREÇO")],
        [sg.Text("Rua:", size=(18)), sg.InputText(cliente[2], key="RUA")],
        [sg.Text("Número da residencia:", size=(18)), sg.InputText(cliente[3], key="NUMERO")],
        [sg.Text("Bairro:", size=(18)), sg.InputText(cliente[4], key="BAIRRO")],
        [sg.Text("Cidade:", size=(18)), sg.InputText(cliente[5], key="CIDADE")],
        [sg.Text("Estado:", size=(18)), sg.InputText(cliente[8], key="ESTADO")],
        [sg.Text("País", size=(18)), sg.InputText(cliente[6], key="PAIS")],
        [sg.Text("CEP:", size=(18)), sg.Input(cliente[7], key="CEP")]
        ]
    
    layout = [
        [sg.Text('EDITAR DADOS DO CLIENTE')],
        [sg.Column(dados_cliente,  vertical_alignment='t'), sg.Column(dados_endereco)],
        [sg.Button('Confirmar', button_color='green', key='CLIENTE-EDITAR-CONFIRM'), sg.Button('Voltar', key='CLIENTE-EDITAR-VOLTAR')]
    ]
    return sg.Window('Editar cliente', layout, finalize=True)

# EXCLUIR CLIENTE #
def excluir_cliente(cliente):
    dados_cliente = [
        [sg.Text('DADOS DO CLIENTE')],
        [sg.Text('Nome', size=(8)), sg.Input(cliente[0], key='NOME-CLIENTE', readonly=True)],
        [sg.Text('Telefone', size=(8)), sg.Input(cliente[1], key='TELEFONE', readonly=True)]
    ]

    dados_endereco = [
        [sg.Text("DADOS DE ENDEREÇO")],
        [sg.Text("Rua:", size=(18)), sg.Input(cliente[2], key="RUA", readonly=True)],
        [sg.Text("Número da residencia:", size=(18)), sg.Input(cliente[3], key="NUMERO", readonly=True)],
        [sg.Text("Bairro:", size=(18)), sg.Input(cliente[4], key="BAIRRO", readonly=True)],
        [sg.Text("Cidade:", size=(18)), sg.Input(cliente[5], key="CIDADE", readonly=True)],
        [sg.Text("Estado:", size=(18)), sg.Input(cliente[8], key="ESTADO", readonly=True)],
        [sg.Text("País", size=(18)), sg.Input(cliente[6], key="PAIS", readonly=True)],
        [sg.Text("CEP:", size=(18)), sg.Input(cliente[7], key="CEP", readonly=True)],
        ]
    
    layout = [
        [sg.Column(dados_cliente,  vertical_alignment='t'), sg.Column(dados_endereco)],
        [sg.Button('Excluir', button_color="red", key='EXCLUIR-CLIENTE-CONFIRM'), sg.Button('Voltar', key='EXCLUIR-CLIENTE-VOLTAR')]
    ]
    return sg.Window('Excluir cliente', layout, finalize=True)