import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    print("player : ", player.lower())
    print("ai : ", ai.lower())
    if player.lower() == ai.lower():
        result = "Empate!"
    elif (player.lower() == "papel" and ai.lower() == "tijeras") or (player.lower() == "tijeras" and ai.lower() == "piedra"):
        result = "Perdiste!"
    elif (player.lower() == "piedra" and ai.lower() == "tijeras") or (player.lower() == "papel" and ai.lower() == "piedra"):
        result = "Ganaste!"
    return result

# Entry Point
def Game():
    #
    #
    player = input("Introudce an option between: ""Piedra"", ""Papel"" or ""Tijeras"": ")

    # Copy array
    optionsGame = options

    #Value IA
    ai = random.choice(optionsGame)
    #
    #
    # 
    winner = quienGana(player, ai)

    print(winner)

Game()