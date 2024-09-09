from cliente import Cliente
from notafiscal import NotaFiscal

# Instanciando:

um_cliente = Cliente(123, "Rua Geral, sem nº")
segundo_cliente = Cliente(456, "Avenida Importante, nº 456")
terceiro_cliente = Cliente(789, "Rua Mais Importante, nº 789")

# colocando os clientes em uma lista de clientes:
clientes = [um_cliente, segundo_cliente, terceiro_cliente]

# O cliente 123 fez uma compra
uma_nota_fiscal = NotaFiscal(11, um_cliente)

# O cliente 456 fez duas compras
outra_nota_fiscal = NotaFiscal(22, segundo_cliente)
mais_outra_nota_fiscal = NotaFiscal(33, segundo_cliente)

# colocando as notas fiscais em uma lita de notas:
notas = [uma_nota_fiscal, outra_nota_fiscal, mais_outra_nota_fiscal]

for nota in notas:
    print("="*40)
    print("Nota Fiscal:", nota.numero)
    print("Cliente:", nota.cliente.codigo, "| endereço:", nota.cliente.endereco)
