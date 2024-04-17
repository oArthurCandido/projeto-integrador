# LembrEscola

LembrEscola é um software desenvolvido como parte do Projeto Integrador do 4º semestre do curso de Bacharelado em Tecnologia da Informação da Universidade Virtual do Estado de São Paulo (UNIVESP).

## Descrição

LembrEscola é um software para gerenciamento de horários e lembretes escolares, visando facilitar a comunicação entre a escola e os responsáveis pelos estudantes. Ele permite o acesso fácil e direto aos horários escolares e lembretes relacionados, fortalecendo as relações dentro do ambiente escolar e contribuindo para uma educação mais democrática.

## Instalação

1. Clone o repositório: git clonehttps://github.com/oArthurCandido/projeto-integrador.git

2. Instale as dependências:

pip install -r requirements.txt

3. Configure as variáveis de ambiente no arquivo `.env`. veja o arquivo `.env.example` para saber quais variáveis são necessárias.

4. Execute as migrações do banco de dados:

python manage.py migrate

5. Inicie o servidor:

python manage.py runserver

## Como contribuir

1. Fork o repositório

2. Crie uma branch para a sua feature (`git checkout -b feat/MinhaFeature`)

3. Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`)

4. Faça push para a branch (`git push origin feat/MinhaFeature`)

5. Crie um novo Pull Request

