import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    result = ''
    player = player.capitalize()
    print("Player: ", player)
    print("Ai: ", ai)
    if player == ai:
        result = "Empate!"
    elif (player == "Papel" and ai == "Tijeras") or (player == "Tijeras" and ai == "Piedra"):
        result = "Perdiste!"
    elif (player == "Piedra" and ai== "Tijeras") or (player == "Papel" and ai == "Piedra"):
        result = "Ganaste!"
    return result

# Entry Point
def Game():
    player = input("Introduce an option between: Piedra, Papel or Tijeras: ")

    # Copy array
    optionsGame = options

    #Value IA
    ai = random.choice(optionsGame)
    
    winner = quienGana(player, ai)

    print(winner)

Game()