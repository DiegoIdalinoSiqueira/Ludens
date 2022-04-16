import PySimpleGUI as sg

class Endereco:
    def __init__(self, rua:str, numero:str, bairro:str, cidade:str, estado:str, pais:str, cep:int)->None: 
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def pais(self):
        return self.__pais
    
    @property
    def cep(self):
        return self.__cep

# CONSTRUINDO AS TELAS #
def tela_dados_endereco():
    dados_endereco = [
        [sg.Text("DADOS DE ENDEREÇO")],
        [sg.Text("Rua:", size=(18)), sg.InputText(key="RUA")],
        [sg.Text("Número da residencia:", size=(18)), sg.InputText(key="NUMERO")],
        [sg.Text("Bairro:", size=(18)), sg.InputText(key="BAIRRO")],
        [sg.Text("Cidade:", size=(18)), sg.InputText(key="CIDADE")],
        [sg.Text("Estado:", size=(18)), sg.InputText(key="ESTADO")],
        [sg.Text("País", size=(18)), sg.InputText(key="PAIS")],
        [sg.Text("CEP:", size=(18)), sg.Input(key="CEP")],
        ]
    return dados_endereco