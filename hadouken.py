def hadouken():
    player = "Ryu"
    enemy = "Ken"
    player_life = 100

    if not player == "Ryu":
        print("Ryu ha perdido")
        print("Ken ha ganado")
        return

    if not enemy == "Ken":
        print("Ryu ha perdido")
        print("Ken ha ganado")
        return

    if player_life <= 0:
        print("Ryu ha perdido")
        print("Ken ha ganado")
        return

    print("Ryu ha usado Hadouken")
    print("Ken ha sido golpeado")
    player_life -= 10

hadouken()
