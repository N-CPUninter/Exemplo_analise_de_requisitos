class Servidor:
    def __init__(self):
        self.dadosFuncionarios = []
        self.vozesCadastradas = []
        self.funcionariosAtivos = 0
        self.autorizacaoEspecial = ""

    def autenticacao(self, funcionario):
        # Lógica de autenticação do funcionário
        return funcionario in self.dadosFuncionarios

    def acessoAutorizado(self):
        # Lógica de controle de acesso autorizado
        return self.funcionariosAtivos > 0

    def cadastrarFuncionario(self, nomeFuncionario, idade, departamento):
        funcionario = Funcionario(nomeFuncionario, idade, departamento)
        self.dadosFuncionarios.append(funcionario)

    def cadastrarVoz(self, funcionario):
        # Lógica para cadastrar a voz do funcionário no servidor
        self.vozesCadastradas.append(funcionario.nomeFuncionario)


class IA:
    def __init__(self):
        self.reconhecerVoz = True
        self.autenticarUsuario = ""

    def analisarVoz(self, voz, servidor):
        # Lógica para análise da voz do usuário
        if voz in servidor.vozesCadastradas:
            index = servidor.vozesCadastradas.index(voz)
            self.autenticarUsuario = voz
            return True, servidor.dadosFuncionarios[index]
        else:
            return False, None


class Porta:
    def __init__(self, idPorta):
        self.idPorta = idPorta

    def autorizacaoAcesso(self, servidor):
        # Lógica para verificar a autorização de acesso com base nas informações do servidor
        if servidor.acessoAutorizado():
            print("Acesso autorizado - Abrir porta")
        else:
            print("Acesso negado")


class Funcionario:
    def __init__(self, nomeFuncionario, idade, departamento):
        self.nomeFuncionario = nomeFuncionario
        self.idade = idade
        self.departamento = departamento
