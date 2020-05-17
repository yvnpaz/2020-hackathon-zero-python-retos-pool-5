import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    result=''
    player = player.capitalize()
    ai = ai.capitalize()
    print('Player: ', player)
    print('AI: ', ai)
    if player == ai:
        result = 'Empate!'
    elif (player == 'Papel' and ai == 'Tijeras') or (player == 'Tijeras' and ai == 'Piedra') or (player == 'Piedra' and ai == 'Papel'):
        result = 'Perdiste!'
    elif (player == 'Piedra' and ai== 'Tijeras') or (player == 'Papel' and ai == 'Piedra') or (player == 'Tijeras' and ai == 'Papel'):
        result = 'Ganaste!'
    return result

# Entry Point
def Game():
    player = input('Introduce una opcion entre piedra, papel or tijeras: ')

    # Copy array
    optionsGame = options

    #Value IA
    ai = random.choice(optionsGame)

    winner = quienGana(player, ai)

    print(winner)

Game()