import Endereco as ed, Funcionario as f, Cliente as c, Mesa as m, Produto as pd, PySimpleGUI as sg
sg.theme('Dark Blue 3')
def janela_principal():
    
    layout=[
        [sg.Button("Gestão da Empresa", key='-EMPRESA-', size=(18, 1))],
        [sg.Button("Sair", key='-SAIR-', size=(7, 1), button_color='red')]
    ]
    return sg.Window("Ludens", layout, size=(300,100), element_justification='c', finalize=True)
    
#janela empresa
def janela_empresa():
    layout = [
        [sg.Text('')],
        [sg.Button("Funcionários",size=(10), key="-FUNCIONARIOS-")],
        [sg.Button("Produtos", size=(10), key="-PRODUTOS-")],
        [sg.Button("Clientes", size=(10), key="-CLIENTES-")],
        [sg.Button("Mesas", size=(10), key="-MESAS-")],
        [sg.Button("Voltar", key="-EMPRESA-VOLTAR-")]
    ]
    return sg.Window("Ludens", layout, size=(250, 250), finalize=True, element_justification='c')

"""Inicio do sistema"""

janela = janela_principal()
while True:
    window, event, values = sg.read_all_windows()

    # EVENTO DE FECHAR O SOFTWARE #
    if event == sg.WIN_CLOSED or event == '-SAIR-':
        window.close()
        break

    # EVENTOS DA JANELA PRINCIPAL #
    if event == '-EMPRESA-':
        window.close()
        janela = janela_empresa()
    
    # EVENTOS DA JANELA EMPRESA #    
    if event == '-EMPRESA-VOLTAR-':
        window.close()
        janela = janela_principal()
        
    elif event == '-FUNCIONARIOS-':
        window.close()
        janela = f.janela_funcionarios()
    
    elif event == '-PRODUTOS-':
        window.close()
        janela = pd.janela_produtos()

    elif event == '-MESAS-':
        window.close()
        janela = m.janela_mesas()
    
    elif event == '-CLIENTES-':
        window.close()
        janela = c.janela_cliente()

    # EVENTOS DA JANELA FUNCIONÁRIO #
    if event == '-FUNCIONARIO-VOLTAR-':
        window.close()
        janela = janela_empresa()

    elif event == '-CADASTRAR-FUN-':
        window.close()
        janela = f.tela_cadastrar_funcionario()

    elif event == '-LISTAR-FUN-':
        window.close()
        funcionarios = f.Funcionario(None, None, None, None, None, None).listar()
        janela = f.listar_funcionario(funcionarios)

    # CADASTRANDO FUNCIONÁRIO #
    if event == '-FUNCIONARIO-CADASTRO-CANCEL-':
        window.close()
        janela = f.janela_funcionarios()

    elif event == "-CADASTRARF-":
        values["CPF-FUNCIONARIO"] = int(values["CPF-FUNCIONARIO"])
        values["SALARIO-FUNCIONARIO"] = int(values["SALARIO-FUNCIONARIO"])
        values["CEP"] = int(values["CEP"])
        values["TELEFONE-FUNCIONARIO"] = int(values["TELEFONE-FUNCIONARIO"])
        f.Funcionario(values["NOME-FUNCIONARIO"], values["TELEFONE-FUNCIONARIO"], ed.Endereco(values["RUA"], values["NUMERO"], values["BAIRRO"], values["CIDADE"], values["ESTADO"], values["PAIS"], values["CEP"]), values["CPF-FUNCIONARIO"], values["CARGO-FUNCIONARIO"], values["SALARIO-FUNCIONARIO"]).cadastrar()
        window.close()
        sg.popup('Funcionário cadastrado')
        janela = f.tela_cadastrar_funcionario()

    # LISTANDO FUNCIONÁRIOS #
    if event == 'LISTAR-FUNCIONARIO-VOLTAR':
        window.close()
        janela = f.janela_funcionarios()
        funcionarios = None

    elif event == 'EXCLUIR-FUNCIONARIO':
        if len(values['TABELA-FUNCIONARIOS']) == 0:
            sg.popup('Escolha um funcionário para deletar')
        else:
            window.close()
            janela = f.excluir_funcionario(funcionarios[values['TABELA-FUNCIONARIOS'][0]])

    # EDITANDO FUNCIONÁRIO #
    if event == 'EDITAR-FUNCIONARIO':
        if len(values['TABELA-FUNCIONARIOS']) == 0:
            sg.popup('Escolha um funcionário para editar')
        else:
            window.close()
            janela = f.editar_funcionario(funcionarios[values['TABELA-FUNCIONARIOS'][0]])

    if event == 'EDITAR-FUNCIONARIO-CONFIRM':
        f.Funcionario(None, None, None, None, None, None).editar(values)
        window.close()
        sg.popup('Funcionário editado!')
        funcionarios = f.Funcionario(None, None, None, None, None, None).listar()
        janela = f.listar_funcionario(funcionarios)

    elif event == 'EDITAR-FUNCIONARIO-VOLTAR':
        window.close()
        funcionarios = f.Funcionario(None, None, None, None, None, None).listar()
        janela = f.listar_funcionario(funcionarios)

    # EXCLUINDO FUNCIONÁRIO #
    if event == 'EXCLUIR-FUNCIONARIO-CONFIRM':
        f.Funcionario(None, None, None, None, None, None).deletar(values['CPF'])
        window.close()
        sg.popup('Funcionário deletado')
        funcionarios = f.Funcionario(None, None, None, None, None, None).listar()
        janela = f.listar_funcionario(funcionarios)

    elif event == 'EXCLUIR-FUNCIONARIO-VOLTAR':
        window.close()
        funcionarios = f.Funcionario(None, None, None, None, None, None).listar()
        janela = f.listar_funcionario(funcionarios)

    # JANELA CLIENTE #
    if event == '-CLIENTE-VOLTAR-':
        window.close()
        janela = janela_empresa()

    elif event == '-CADASTRAR-CLI-':
        window.close()
        janela = c.janela_cadastrarC()

    # CADASTRANDO CLIENTE #
    if event == '-CLIENTE-CADASTRO-CANCEL-':
        window.close()
        janela = c.janela_cliente()
    
    elif event == '-CADASTRARC-':
        values['TELEFONE-CLIENTE'] = int(values['TELEFONE-CLIENTE'])
        values["CEP"] = int(values["CEP"])
        c.Cliente(values['NOME-CLIENTE'], values['TELEFONE-CLIENTE'], ed.Endereco(values["RUA"], values["NUMERO"], values["BAIRRO"], values["CIDADE"], values["ESTADO"], values["PAIS"], values["CEP"])).cadastrar()
        window.close()
        sg.popup('Cliente cadastrado!')
        janela = c.janela_cadastrarC()

    # LISTAR CLIENTES #
    if event == '-LISTAR-CLI-':
        window.close()
        clientes = c.Cliente(None, None, None).listar()
        janela = c.listar_clientes(clientes)

    if event == 'LISTAR-CLIENTES-VOLTAR':
        window.close()
        clientes = None
        janela = c.janela_cliente()
    
    # EDITANDO CLIENTE #
    if event == 'EDITAR-CLIENTE':
        if len(values['TABELA-CLIENTES']) == 0:
            sg.popup('Escolha um cliente para editar')
        else:
            window.close()
            janela = c.editar_cliente(clientes[values['TABELA-CLIENTES'][0]])

    if event == 'CLIENTE-EDITAR-CONFIRM':
        c.Cliente(None, None, None).editar(values)
        window.close()
        sg.popup('Cliente editado!')
        clientes = c.Cliente(None, None, None).listar()
        janela = c.listar_clientes(clientes)

    elif event == 'CLIENTE-EDITAR-VOLTAR':
        window.close()
        clientes = c.Cliente(None, None, None).listar()
        janela = c.listar_clientes(clientes)

    # EXCLUIR CLIENTE #
    if event == 'EXCLUIR-CLIENTE':
        if len(values['TABELA-CLIENTES']) == 0:
            sg.popup('Escolha um cliente para excluir')
        else:
            window.close()
            janela = c.excluir_cliente(clientes[values['TABELA-CLIENTES'][0]])

    if event == 'EXCLUIR-CLIENTE-CONFIRM':
        c.Cliente(None, None, None).deletar(values['TELEFONE'])
        window.close()
        sg.popup('Cliente deletado')
        clientes = c.Cliente(None, None, None).listar()
        janela = c.listar_clientes(clientes)

    elif event == 'EXCLUIR-CLIENTE-VOLTAR':
        window.close()
        clientes = c.Cliente(None, None, None).listar()
        janela = c.listar_clientes(clientes)

#JANELAS PRODUTOS#
    if event == '-PRODUTOS-VOLTAR-':
        window.close()
        janela = janela_empresa()

    elif event == '-CADASTRARPRO-':
        window.close()
        janela = pd.tela_cadastrar_prod()
    
# CADASTRANDO PRODUTOS #
    if event == '-PRODUTOS-CADASTRO-CANCEL-':
        window.close()
        janela = pd.janela_produtos()
    
    elif event == '-CADASTRARP-':
        values['PRECO-PRODUTO'] = float(values['PRECO-PRODUTO'])
        values['CODIGO-PRODUTO'] = int(values['CODIGO-PRODUTO'])
        values['ESTOQUE-PRODUTO'] = int(values['ESTOQUE-PRODUTO'])
        values['LUCRO-PRODUTO'] = float(values['LUCRO-PRODUTO'])
        pd.Produto(values['NOME-PRODUTO'], values['PRECO-PRODUTO'], values['CODIGO-PRODUTO'], values['ESTOQUE-PRODUTO'], values['LUCRO-PRODUTO']).cadastrar()
        window.close()
        sg.popup("Produto Cadastrado!")
        janela = pd.tela_cadastrar_prod()

    # LISTANDO PRODUTOS #
    if event == '-LISTARPRO-':
        window.close()
        produtos = pd.Produto(None, None, None, None, None).listar()
        janela = pd.janela_listar_produto(produtos)
    
    if event == '-VOLTAR-LISTA-PRODUTOS-':
        window.close()
        janela = pd.janela_produtos()
        produtos = None
    
    # BUSCANDO PRODUTO ESPECÍFICO #
    if "PESQUISA" in values:
        if event == '-VOLTAR-LISTA-PRODUTOS-':
            pass
        else:
            pesquisa = pd.Produto(None, None, None, None, None).busca_especifica(values['PESQUISA'])
            window['TABELA-PRODUTOS'].update(pesquisa)
    else:
        pass
    
    # EDITANDO PRODUTO #
    if event == '-EDITAR-PRODUTO-':
        if len(values['TABELA-PRODUTOS']) == 0:
            sg.popup('Escolha um produto para editar')
        else:
            window.close()
            janela = pd.editar_produto(produtos[values['TABELA-PRODUTOS'][0]])
    
    if event == '-EDITAR-PRODUTO-CONFIRM-':
        pd.Produto(None, None, None, None, None).editar(values)
        window.close()
        sg.popup('Produto editado!')
        produtos = pd.Produto(None, None, None, None, None).listar()
        janela = pd.janela_listar_produto(produtos)

    elif event == 'EDITAR-PRODUTO-VOLTAR':
        window.close()
        produtos = pd.Produto(None, None, None, None, None).listar()
        janela = pd.janela_listar_produto(produtos)

    # DELETANDO PRODUTOS #
    if event == '-EXCLUIR-PRODUTO-':
        if len(values['TABELA-PRODUTOS']) == 0:
            sg.popup('Escolha um produto para excluir')
        else:
            window.close()
            janela = pd.excluir_produto(produtos[values['TABELA-PRODUTOS'][0]])
    
    if event == '-EXCLUIR-PRODUTO-CONFIRM-':
        pd.Produto(None, None, None, None, None).deletar(int(values['-CODIGO-PROD-']))
        window.close()
        sg.popup('Produto excluido')
        produtos = pd.Produto(None, None, None, None, None).listar()
        janela = pd.janela_listar_produto(produtos)
    
    elif event == 'EXCLUIR-PRODUTO-VOLTAR':
        window.close()
        produtos = pd.Produto(None, None, None, None, None).listar()
        janela = pd.janela_listar_produto(produtos)
    
# JANELA MESA #
    if event == '-MESA-VOLTAR-':
        window.close()
        janela = janela_empresa()

    elif event == '-CADASTRAR-MESA-':
        window.close()
        janela = m.cadastro_mesas()

    elif event == '-LISTAR-MESA-':
        window.close()
        mesas = m.Mesa(None, None, None).listar()
        janela = m.listar_mesa(mesas)

    # CADASTRANDO MESA #
    if event == '-MESA-CADASTRO-CANCEL-':
        window.close()
        janela = m.janela_mesas()

    elif event == '-CADASTRAR-MESA-CONFIRM-':
        values['NUMERO-MESA'] = int(values['NUMERO-MESA'])
        values['CAPACIDADE-MESA'] = int(values['CAPACIDADE-MESA'])
        m.Mesa(values['NUMERO-MESA'], values['LUGAR-MESA'], values['CAPACIDADE-MESA']).cadastrar()
        window.close()
        sg.popup('Mesa cadastrada')
        janela = m.cadastro_mesas()

    # LISTAR MESA #
    if event == 'LISTAR-MESA-VOLTAR':
        window.close()
        janela = m.janela_mesas()
        mesas = None

    # EDITAR MESA #
    if event == 'EDITAR-MESA':
        if len(values['-TABELA-MESAS-']) == 0:
            sg.popup('Escolha uma mesa para editar')
        else:
            window.close()
            janela = m.editar_mesa(mesas[values['-TABELA-MESAS-'][0]])

    if event == 'EDITAR-MESA-CONFIRM':
        m.Mesa(None, None, None).editar(values)
        window.close()
        sg.popup('Mesa editada!')
        mesas = m.Mesa(None, None, None).listar()
        janela = m.listar_mesa(mesas)

    elif event == 'EDITAR-MESA-VOLTAR':
        window.close()
        mesas = m.Mesa(None, None, None).listar()
        janela = m.listar_mesa(mesas)

    # DELETAR MESA #
    if event == 'EXCLUIR-MESA':
        if len(values['-TABELA-MESAS-']) == 0:
            sg.popup('Escolha uma mesa para deletar')
        else:
            window.close()
            janela = m.deletar_mesa(mesas[values['-TABELA-MESAS-'][0]])

    if event == 'EXCLUIR-MESA-VOLTAR':
        window.close()
        mesas = m.Mesa(None, None, None).listar()
        janela = m.listar_mesa(mesas)
    
    elif event == 'EXCLUIR-MESA-CONFIRM':
        m.Mesa(None, None, None).deletar(values['NUMERO-MESA'])
        window.close()
        sg.popup('Mesa excluida!')
        mesas = m.Mesa(None, None, None).listar()
        janela = m.listar_mesa(mesas)