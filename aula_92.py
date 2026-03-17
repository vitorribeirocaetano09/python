def fibonnati():
    penultimo = 0
    ultimo = 1
    print(f"{penultimo},{ultimo}")
    while True:
        proximo = penultimo+ultimo
        print(proximo)
        penultimo = ultimo
        ultimo = proximo

if __name__ == "__main__":
        fibonnati()