import PySimpleGUI as sg, Pessoa , Endereco as e

class Funcionario(Pessoa.Pessoa):
    def __init__(self, nome:str, telefone:int, endereco:object, cpf:int, cargo:str, salario:float)->None:
        Pessoa.Pessoa.__init__(self, nome, telefone, endereco)
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario

    def cadastrar(self):
        comando = f'INSERT INTO funcionario VALUES ("{self._nome}", {self._telefone}, {self.__cpf}, "{self.__cargo}", {self.__salario}, "{self._endereco.rua}", "{self._endereco.numero}", "{self._endereco.bairro}", "{self._endereco.cidade}", "{self._endereco.pais}", {self._endereco.cep}, "{self._endereco.estado}")'
        self._conectar_mysql(comando)
    
    def listar(self):
        comando = "SELECT * FROM funcionario"
        resultado = self._conectar_mysql(comando)
        return resultado

    def editar(self, valores:dict):
        comando = f"UPDATE funcionario SET nome = '{valores['NOME']}', telefone = {valores['TELEFONE']}, cpf = {valores['CPF']}, cargo = '{valores['CARGO']}', salario = {float(valores['SALARIO'])}, rua = '{valores['RUA']}', numero = '{valores['NUMERO']}', bairro = '{valores['BAIRRO']}', cidade = '{valores['CIDADE']}', pais = '{valores['PAIS']}', cep = {valores['CEP']}, estado = '{valores['ESTADO']}' WHERE cpf = {valores['CPF-ATUAL']} "
        self._conectar_mysql(comando)

    def deletar(self,cpf:int):
        comando = f"DELETE FROM funcionario WHERE cpf = {cpf}"
        self._conectar_mysql(comando)

# CONSTRUINDO AS JANELAS #
def janela_funcionarios():
    layout = [
        [sg.Button("Cadastrar Funcionários", key="-CADASTRAR-FUN-", size=(18))],
        [sg.Button("Listar Funcionários", key="-LISTAR-FUN-", size=(18))],
        [sg.Button("Voltar", key='-FUNCIONARIO-VOLTAR-')]
    ]
    return sg.Window("Ludens", layout, finalize=True, element_justification='c')

# TELA DE CADASTRO
def tela_cadastrar_funcionario():
    dados_funcionario = [
        [sg.Text('DADOS DO FUNCIONÁRIO')],
        [sg.Text("Nome:", size=(8)), sg.InputText(key = "NOME-FUNCIONARIO")],
        [sg.Text("Telefone:", size=(8)), sg.Input(key="TELEFONE-FUNCIONARIO")],
        [sg.Text("CPF:", size=(8)), sg.Input(key="CPF-FUNCIONARIO")],
        [sg.Text("Cargo:", size=(8)), sg.InputText(key="CARGO-FUNCIONARIO")],
        [sg.Text("Salário:", size=(8)), sg.Input(key="SALARIO-FUNCIONARIO")]
    ]

    layout = [
        [sg.Column(dados_funcionario, vertical_alignment='t'), sg.Column(e.tela_dados_endereco())],
        [sg.Button("Cadastrar", key="-CADASTRARF-"), sg.Button("Cancelar", key='-FUNCIONARIO-CADASTRO-CANCEL-', button_color="red")]
    ]
    return sg.Window("Ludens", layout, finalize=True)

# LISTAR  FUNCIONÁRIO #
def listar_funcionario(funcionarios):
    linhas = []
    for i in funcionarios:
        linhas.append(i)
    
    if len(linhas) == 0:
        layout = [
            [sg.Text('Não existem funcionários cadastrados')],
            [sg.Button('Voltar', key='LISTAR-FUNCIONARIO-VOLTAR')]
        ]
        return sg.Window('Listar funcionários', layout, finalize=True, element_justification='c')
    else:
        layout = [
            [sg.Text('LISTA DE FUNCIONÁRIOS')],
            [sg.Table(linhas, ['NOME', 'TELEFONE', 'CPF', 'CARGO', 'SALÁRIO'], justification='left', key='TABELA-FUNCIONARIOS')],
            [sg.Button('Editar dados', key='EDITAR-FUNCIONARIO'), sg.Button('Excluir', button_color='red', key='EXCLUIR-FUNCIONARIO')],
            [sg.Button('Voltar', key='LISTAR-FUNCIONARIO-VOLTAR')]
        ]
        return sg.Window('Lista de funcionários', layout, finalize=True)

# EDITAR FUNCIONÁRIO #
def editar_funcionario(funcionario):
    dados_funcionario = [
        [sg.Text('DADOS DO FUNCIONÁRIO')],
        [sg.Text("Nome:", size=(8)), sg.Input(funcionario[0],key = "NOME")],
        [sg.Text("Telefone:", size=(8)), sg.Input(funcionario[1],key="TELEFONE")],
        [sg.Text("CPF:", size=(8)), sg.Input(funcionario[2],key="CPF")],
        [sg.Text("Cargo:", size=(8)), sg.Input(funcionario[3], key="CARGO")],
        [sg.Text("Salário:", size=(8)), sg.Input(funcionario[4], key="SALARIO")],
        [sg.Text('CPF atual:'), sg.Input(funcionario[2], key="CPF-ATUAL", readonly= True)]
    ]

    dados_endereco = [
        [sg.Text("DADOS DE ENDEREÇO")],
        [sg.Text("Rua:", size=(18)), sg.Input(funcionario[5], key="RUA")],
        [sg.Text("Número da residencia:", size=(18)), sg.Input(funcionario[6], key="NUMERO")],
        [sg.Text("Bairro:", size=(18)), sg.Input(funcionario[7], key="BAIRRO")],
        [sg.Text("Cidade:", size=(18)), sg.Input(funcionario[8], key="CIDADE")],
        [sg.Text("Estado:", size=(18)), sg.Input(funcionario[11], key="ESTADO")],
        [sg.Text("País", size=(18)), sg.Input(funcionario[9], key="PAIS")],
        [sg.Text("CEP:", size=(18)), sg.Input(funcionario[10], key="CEP")],
        ]

    layout = [
        [sg.Column(dados_funcionario, vertical_alignment='t'), sg.Column(dados_endereco)],
        [sg.Button('Confirmar', button_color='green', key='EDITAR-FUNCIONARIO-CONFIRM'), sg.Button('Voltar', key='EDITAR-FUNCIONARIO-VOLTAR')]
    ]
    return sg.Window('Editar Funcionário', layout, finalize=True) 

# EXCLUIR FUNCIONÁRIO #
def excluir_funcionario(funcionario):
        dados_funcionario = [
            [sg.Text('DADOS DO FUNCIONÁRIO')],
            [sg.Text("Nome:", size=(8)), sg.Input(funcionario[0] ,key = "NOME-FUNCIONARIO", readonly = True)],
            [sg.Text("Telefone:", size=(8)), sg.Input(funcionario[1],key="TELEFONE-FUNCIONARIO", readonly= True)],
            [sg.Text("CPF:", size=(8)), sg.Input(funcionario[2], key="CPF", readonly= True)],
            [sg.Text("Cargo:", size=(8)), sg.InputText(funcionario[3],key="CARGO-FUNCIONARIO", readonly= True)],
            [sg.Text("Salário:", size=(8)), sg.Input(funcionario[4], key="SALARIO-FUNCIONARIO", readonly= True)]
        ]

        dados_endereco = [
            [sg.Text("DADOS DE ENDEREÇO")],
            [sg.Text("Rua:", size=(18)), sg.Input(funcionario[5], readonly=True, key="RUA")],
            [sg.Text("Número da residencia:", size=(18)), sg.Input(funcionario[6], readonly= True, key="NUMERO")],
            [sg.Text("Bairro:", size=(18)), sg.Input(funcionario[7], readonly=True, key="BAIRRO")],
            [sg.Text("Cidade:", size=(18)), sg.Input(funcionario[8], readonly=True, key="CIDADE")],
            [sg.Text("Estado:", size=(18)), sg.Input(funcionario[11], readonly=True, key="ESTADO")],
            [sg.Text("País", size=(18)), sg.Input(funcionario[9], readonly=True, key="PAIS")],
            [sg.Text("CEP:", size=(18)), sg.Input(funcionario[10], readonly=True, key="CEP")],
            ]

        layout = [
            [sg.Column(dados_funcionario, vertical_alignment='t'), sg.Column(dados_endereco)],
            [sg.Button('Excluir', button_color='red', key='EXCLUIR-FUNCIONARIO-CONFIRM'), sg.Button('Voltar', key='EXCLUIR-FUNCIONARIO-VOLTAR')]
        ]
        return sg.Window('Excluir funcionário', layout, finalize=True)