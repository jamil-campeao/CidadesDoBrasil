# Projeto: Validação de CEPs de Municípios do Brasil

## Sobre o Projeto
Este projeto foi desenvolvido para resolver um problema específico: criar uma planilha contendo todos os municípios do Brasil com seus respectivos códigos do IBGE, nomes dos municípios e CEPs. Durante a busca por bases de dados existentes, percebi que as planilhas disponíveis não atendiam aos meus requisitos, pois muitas delas incluíam CEPs de municípios sem CEP único, dificultando o uso dos dados.

A solução encontrada foi criar um script em Python que integrasse a API da ViaCEP para validar os CEPs de cada município e identificar quais possuem CEP único.

## Processo de Desenvolvimento
1. Base de Dados Inicial:
- Utilizei a planilha dos múnicipios de Michel Herszenhau como base inicial. Fonte: https://terminaldeinformacao.com/2019/01/12/tabela-com-lista-de-ceps-do-brasil/
- Removi nomes duplicados de municípios para evitar redundâncias na consulta.

2. Consulta na API ViaCEP:
- Descobri que a API retorna o status 200 e o corpo com a mensagem "erro": "True" para municípios sem CEP único.
- Com base nisso, elaborei um script que consulta cada CEP e classifica-o como único ou não único.

3. Execução do Script:
- Incluí um intervalo de 10 segundos entre as requisições para evitar bloqueios na API.
- A execução levou cerca de 14 horas devido à quantidade de municípios e ao intervalo definido.

4. Correção de Erros:
- Identifiquei que algumas requisições falhavam devido à ausência de um 0 no início de alguns CEPs.
- Ajustei esses erros e rodei o script novamente para completar o processo.

5. Limpeza e Organização dos Dados:
- Removi os CEPs dos municípios sem CEP único.
- Mantive apenas os municípios com CEP único e adicionei uma coluna na planilha indicando o status do CEP.

6. Inserção no Banco de Dados:
- Organizei os dados finais e criei um script SQL de inserção para armazenar as informações no meu banco de dados

## Tecnologias Utilizadas
- Python: Para desenvolvimento do script de validação e consulta na API.
- API [ViaCEP](https://viacep.com.br/): Para obter informações dos CEPs.
- SQL: Para armazenar os dados finais em um banco de dados.

## Como Utilizar o Repositório: 
- Clone o repositório:
```bash 
https://github.com/jamil-campeao/CidadesDoBrasil.git
```

- Instale as [dependências](https://github.com/jamil-campeao/CidadesDoBrasil/tree/main/Dependencias) necessárias 
```bash
pip install -r dependencias.txt
```

- Execute o script principal:
```bash
python verificaCepUnico.py
```

## Estrutura do repositório
- ./src: Planilha, script em python e arquivo sql de exemplo
- ./Dependencias: arquivo das dependências do projeto

## Resultados
- Planilha final contendo todos os municípios do Brasil com CEPs únicos devidamente validados.
- Script SQL para inserção desses dados em um banco de dados.
- Base de dados organizada e pronta para utilização em aplicações futuras.



