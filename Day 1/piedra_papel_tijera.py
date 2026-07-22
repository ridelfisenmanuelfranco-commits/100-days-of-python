# Día 1 / 100
# Piedra, Papel o Tijeras
# Juega contra la computadora.
import random
opciones = ['piedar', 'papel', 'tijeras']

usuario = input('Elije una opcion: ').lower()
cpu = random.choice(opciones)

print(f'CPU: {cpu}')

if usuario == cpu:
    print('-> Empate <-')
    
elif (
    (usuario == 'piedra' and cpu == 'tijeras') or 
    (usuario == 'papel' and cpu == 'piedra') or 
    (usuario == 'tijeras' and cpu == 'papel')):
    
    print('>- Ganaste <-')
    
else:
    print('-> Perdiste <-')