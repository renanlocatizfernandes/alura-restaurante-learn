from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia',5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_doce = Sobremesa('Surpresa de uva', 10.00, 'Brigadeiro', 'pequeno', 'O melhor pao da cidade')
sobremesa_doce.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_doce)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()