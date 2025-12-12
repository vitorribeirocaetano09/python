fila_pedidos = ["pizza", "hamburguer", "salada"]
while fila_pedidos: 
    pedido_atual = fila_pedidos.pop(0) 
    print(f"Processando pedido: {pedido_atual}")
print("Fila de pedidos vazia.")
