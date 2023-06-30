from implementacaoClasses import *

# Exemplo de uso das classes criadas:
servidor = Servidor()
ia = IA()
porta = Porta(1)
servidor.cadastrarFuncionario("João", 30, "Departamento A")
servidor.cadastrarFuncionario("Maria", 35, "Departamento B")

servidor.cadastrarVoz(servidor.dadosFuncionarios[0])
servidor.cadastrarVoz(servidor.dadosFuncionarios[1])

voz1 = "João"
voz2 = "Pedro"

auth, func = ia.analisarVoz(voz1, servidor)
if auth:
    if servidor.autenticacao(func):
        servidor.funcionariosAtivos += 1
        porta.autorizacaoAcesso(servidor)
    else:
        print("Funcionário não autenticado")
else:
    print("Voz não reconhecida")

auth, func = ia.analisarVoz(voz2, servidor)
if auth:
    if servidor.autenticacao(func):
        servidor.funcionariosAtivos += 1
        porta.autorizacaoAcesso(servidor)
    else:
        print("Funcionário não autenticado")
else:
    print("Voz não reconhecida")
