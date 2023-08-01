def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    return media

def solicitar_notas():
    notas = []

    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    return notas

notas = solicitar_notas()
media = calcular_media(notas)

print("Notas digitadas:", notas)
print("Média:", media)
