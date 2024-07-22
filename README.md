# Sistema de Gestão de Restaurantes

## Descrição
Este projeto é uma aplicação Python que simula um sistema de gestão de restaurantes. Permite a criação de restaurantes, adição de itens ao cardápio, recebimento de avaliações de clientes e visualização de informações detalhadas sobre os restaurantes e seus cardápios.

## Funcionalidades
- **Criação de Restaurantes**: Permite criar novos restaurantes especificando nome e categoria.
- **Gestão de Cardápio**: Adiciona pratos, bebidas e sobremesas ao cardápio de cada restaurante.
- **Recebimento de Avaliações**: Aceita avaliações dos clientes para cada restaurante.
- **Listagem de Restaurantes**: Exibe todos os restaurantes registrados com suas informações básicas e média de avaliações.
- **Exibição de Cardápio**: Mostra detalhes dos itens disponíveis no cardápio de cada restaurante.

## Tecnologias Utilizadas
- Python

## Estrutura do Projeto
- `restaurante.py`: Contém a classe `Restaurante` que gerencia os dados e operações relacionadas aos restaurantes.
- `item_cardapio.py`: Define a classe abstrata `ItemCardapio` e a estrutura para itens de cardápio.
- `prato.py`, `bebida.py`, `sobremesa.py`: Subclasses de `ItemCardapio` que especificam diferentes tipos de itens de cardápio.
- `avaliacao.py`: Contém a classe `Avaliacao` para gerenciar as avaliações dos clientes.
- `app.py`: Arquivo principal que instancia objetos e executa o programa.

## Como Executar
Para rodar o projeto, assegure-se de que o Python está instalado em seu ambiente. Em seguida, execute o seguinte comando na raiz do projeto:

```bash
python app.py
