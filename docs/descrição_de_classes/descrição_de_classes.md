# Descrição de Classes com base nos requisitos e casos de uso descritos

## Classe Servidor:

### Descrição: Essa classe representa o servidor responsável pelo sistema de controle de acesso. É responsável por armazenar os dados dos funcionários, vozes cadastradas e gerenciar a autenticação e autorização de acesso.
#### Atributos:
- dadosFuncionarios: Lista que armazena os dados dos funcionários cadastrados.
- vozesCadastradas: Lista que armazena as vozes cadastradas dos funcionários.
- funcionariosAtivos: Variável que registra o número de funcionários ativos no sistema.
- autorizacaoEspecial: Variável que registra a autorização especial (se houver) para determinado acesso.
#### Métodos:
- autenticacao(funcionario): Realiza a autenticação do funcionário fornecido como parâmetro.
- acessoAutorizado(): Verifica se o acesso foi autorizado.
- cadastrarFuncionario(nomeFuncionario, idade, departamento): Cadastra um novo funcionário no sistema.
- cadastrarVoz(funcionario): Realiza o cadastro da voz do funcionário no sistema.

## Classe IA:

### Descrição: Essa classe representa a inteligência artificial responsável pela análise da voz dos funcionários.
#### Atributos:
- reconhecerVoz: Variável que indica se a IA é capaz de reconhecer a voz.
- autenticarUsuario: Variável que registra o resultado da autenticação do usuário.
#### Métodos:
- analisarVoz(voz, servidor): Realiza a análise da voz fornecida em relação às vozes cadastradas no servidor e retorna o resultado da autenticação, juntamente com o objeto Funcionario correspondente.

## Classe Porta:

### Descrição: Essa classe representa uma porta que é controlada pelo sistema de controle de acesso.
#### Atributos:
- idPorta: Identificador único da porta.
#### Métodos:
- autorizacaoAcesso(servidor): Verifica a autorização de acesso no servidor e executa a ação correspondente na porta.

## Classe Funcionario:

### Descrição: Essa classe representa um funcionário que tem acesso controlado pelo sistema.
#### Atributos:
- nomeFuncionario: Nome do funcionário.
- idade: Idade do funcionário.
- departamento: Departamento em que o funcionário está alocado.
#### Métodos:
