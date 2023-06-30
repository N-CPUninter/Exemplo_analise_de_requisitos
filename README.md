<!-- Área do Banner -->
<div align="center" style="background-color: white; max-width: 70%;">
  <img alt="BANNER com título: Da Análise ao Código" title="Banner_ADS_v2" src="img/Banner%20Github%20-%20ADS%20v2.png" width="100%" />
</div>

<!-- Título e breve descrição do repositório -->
<div align="center"><h1>Exemplo de Análise de Requisitos</h1><p><b>Exemplo de criação diagramas e código com base em requisitos de sistema de Controle de Acesso fictício</b></p></div>

<!-- Ícones ou links das tecnologias usadas -->
<div align="center">
  <a href="https://www.uml.org/" title="UML"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/UML_logo.svg" alt="UML" height="21px"></a>
  +
  <a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="21px" height="21px"></a>
  +
  <a href="https://plantuml.com/" title="PlantUML">PlantUML</a>
</div>

<!-- Escudos de licença e contador de contribuidores -->
<p align="center">
  <a href="https://github.com/N-CPUninter/Exemplo_analise_de_requisitos/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/N-CPUninter/Exemplo_analise_de_requisitos?color=%237159c1&logoColor=%237159c1&style=flat" alt="Contributors">
  </a>
  <a href="https://opensource.org/license/gpl-3-0">
    <img src="https://img.shields.io/github/license/N-CPUninter/Exemplo_analise_de_requisitos?color=%23BD0000" alt="License">
  </a>
</p>

<!-- Descrição do repositório e demais dados -->
## Descrição

Este repositório contém a implementação de um Sistema de Controle de Acesso, juntamente com os diagramas de casos de uso e de classes. O sistema é projetado para autenticar e autorizar o acesso de funcionários com base na análise de suas vozes.

Este exemplo faz parte do trabalho de Análise de Requisitos da matéria de Análise (e Modelagem) de Sistemas.

## Participantes

| [<img src="https://avatars3.githubusercontent.com/u/60905310?s=460&v=4" width="75px;"/>](https://github.com/guipatriota) |
| :------------------------------------------------------------------------------------------------------------------------: |


| [Prof. Guilherme Patriota](https://github.com/guipatriota)

## Diagramas

Os seguintes diagramas estão disponíveis neste repositório:

- [Diagrama de Casos de Uso](https://www.plantuml.com/plantuml/uml/RP5DQiD038NtEeN8Fe4soRR460hT5KgxL-rnAd16HYDtaTB3z2ozM3L4_J5qOzxJ-_HZvb2CrERJ232cmT04bOylXZrhwemb0r1dedWxvyxjvuUo81KSedxNLCVXxaMDQc42g0Ce7yU4gmSkbaw4VS9MigbuqNNJfL9aLVbluWqGvv8wAjxMKa_5b1RRB_nZU_MNR3ADN1nyadFarujyDb4-ayREOBR_Rtlz6R9R37bMLfpgBqQy1yy7NA_Zdf2xNxbtoIxZeEaYjzvNGzniRYBnRxWjl0CSKkxzMRu0): Apresenta os casos de uso e suas relações no sistema de controle de acesso.
- [Diagrama de Classes](https://www.plantuml.com/plantuml/uml/PL8zJyCm4DtpAqwP0aqgM3CrGbHYGqAm6zk8ar9VvNCo5F7VEJTEUnLBBElTlOyNxpYPcAR3M5LsDCpmvkECZYByL00TEEE8zrEmIC549EvXH4vdRAQJvoVZ3ASeNmrzgOqXuPptC2oOcH95F1bhw9cFtg8PUn0A0JSPz26XpMYZMEvw-2GQbndhcMaeD8uQ3ThY9ohJJQ23L_SMK7Bv5fm_Idfp4CciC1EwMv8FEcaNwyplsjRBK7gAtbBuzjRdbOkTxfedllEKALJKOAIlHKEgR85BzQBIP88MzahwAlfAuhdeeZlVrdOtkjtXt5EZQ6_CQ_R2fdhINhkbh-ilrBqjGq9wUJdrOmrT1_N3TdjVtwZqS2Jc2IlfRPsIOzqKV4euYljgoLWe_e-90H-ShwgT7F9w_m00): Mostra as classes envolvidas no sistema e suas relações.

## Implementação

A implementação das classes do sistema pode ser encontrada no arquivo `implementacaoClasses.py`. O arquivo contém a seguinte estrutura de classes:

- Classe Servidor: Responsável pelo armazenamento dos dados dos funcionários, gerenciamento da autenticação e autorização de acesso.
- Classe IA: Realiza a análise da voz dos funcionários e retorna o resultado da autenticação.
- Classe Porta: Controla o acesso à porta com base na autorização recebida do servidor.
- Classe Funcionario: Representa um funcionário com suas informações básicas.

Além disso, o arquivo `main.py` demonstra um exemplo de uso das classes implementadas. Ele cria instâncias das classes, cadastra funcionários, cadastra vozes, realiza a análise de voz e verifica a autorização de acesso.

## Executando o Exemplo

Para executar o exemplo fornecido, certifique-se de ter o Python instalado em sua máquina. Em seguida, siga estas etapas:

1. Clone este repositório em sua máquina local.
2. Navegue até o diretório clonado através do terminal ou prompt de comando.
3. Execute o comando `python main.py`.

Você verá a saída do exemplo de uso do sistema de controle de acesso, com mensagens indicando se o acesso foi autorizado ou não.

## Contribuição

Se você tiver alguma sugestão, correção de bugs ou melhorias para este exemplo didático de sistema de controle de acesso, sinta-se à vontade para abrir uma issue ou enviar uma pull request. Sua contribuição é muito bem-vinda!

Lembre-se de que todas as alterações no código devem ser originadas de alterações dos diagramas e não o contrário. Sendo assim, tenha isto em mente ao propor sua melhoria.

## Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).

