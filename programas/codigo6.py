#este programa practica el comando while
numeroSecreto = 777
print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input('Dame otro numero:'))

while numero != numeroSecreto:
    print('!Ja, Ja! !Estas atrapado en mi ciclo')
    numero = int(input('Dame otro numero:'))

print('!Bien hecho, muggle! Eres libre ahora')
