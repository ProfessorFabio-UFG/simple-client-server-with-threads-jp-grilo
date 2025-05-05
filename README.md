[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1lvR2g5j)

# Simple Client-Server with Threads

Este repositório contém um projeto simples de cliente-servidor utilizando threads, criado como parte de um exercício no GitHub Classroom.

## Descrição

O projeto exemplifica a implementação de um modelo cliente-servidor usando a linguagem Python. Ele demonstra como um servidor pode lidar com múltiplas conexões simultâneas utilizando threads, permitindo que múltiplos clientes se conectem e interajam com o servidor ao mesmo tempo.

## Estrutura do Projeto

A estrutura do repositório contém os seguintes componentes principais:

- **Servidor**: Implementação do lado servidor, responsável por receber conexões, processar solicitações e responder aos clientes.
- **Cliente**: Implementação do lado cliente, responsável por se conectar ao servidor e enviar solicitações.
- **Threads**: Uso de threads para gerenciar múltiplas conexões de clientes simultaneamente.

## Comandos de Interação

### Lado Cliente
1. O cliente conecta-se ao servidor no endereço `127.0.0.1` e porta `9999`.
2. O cliente envia solicitações no seguinte formato:
   ```
   <num1> <operation> <num2>
   ```
   Exemplos de comandos suportados:
   - `10 add 5` (soma)
   - `20 subtract 8` (subtração)
   - `4 multiply 2` (multiplicação)
   - `9 divide 3` (divisão)

3. Para encerrar a interação, o cliente pode digitar:
   ```
   exit
   ```

4. Após enviar o comando, o cliente recebe a resposta do servidor, que pode ser o resultado da operação ou uma mensagem de erro.

### Lado Servidor
1. O servidor recebe a solicitação enviada pelo cliente.
2. Ele verifica se o comando está no formato correto (`<num1> <operation> <num2>`). Caso contrário, responde com:
   ```
   Error: Invalid request format. Use: <num1> <operation> <num2>
   ```
3. O servidor executa a operação solicitada:
   - **add**: soma os dois números.
   - **subtract**: subtrai o segundo número do primeiro.
   - **multiply**: multiplica os dois números.
   - **divide**: divide o primeiro número pelo segundo (se o divisor não for zero).
4. Caso a operação não seja suportada, responde com:
   ```
   Error: Unsupported operation. Use: add, subtract, multiply, divide.
   ```
5. Se ocorrer algum erro, como entrada inválida, o servidor responde com mensagens de erro apropriadas, como:
   ```
   Error: Invalid numbers provided.
   Error: Division by zero is not allowed.
   ```

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/ProfessorFabio-UFG/simple-client-server-with-threads-jp-grilo.git
   cd simple-client-server-with-threads-jp-grilo
   ```

2. Execute o servidor:

   ```bash
   python server.py
   ```

3. Em outra instância do terminal, execute o cliente:

   ```bash
   python client.py
   ```

4. Interaja com o servidor através do cliente.

## Funcionalidades

- Aceitação de múltiplas conexões simultâneas de clientes.
- Comunicação entre cliente e servidor utilizando sockets.
- Gerenciamento de conexões utilizando threads.
