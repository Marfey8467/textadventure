# Tic Toc Übung
field: list = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
status: str = "go"
player: str = "X"

if __name__ == "__main__":
    # start game
    print("\n " + field[0] + " | " + field[1] + " | " + field[2] +
          "\n " + field[3] + " | " + field[4] + " | " + field[5] +
          "\n " + field[6] + " | " + field[7] + " | " + field[8])

    # game loop while not win or draw
    while status == "go":
        # Userinput
        int_in = int(input("\n" + player + " bitte einen Zug eingeben (0-8)"))
        # read field with check if move is correct
        if field[int_in] == "E":
            field[int_in] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("wrong move")
            continue
        # check for win, draw
        # win = 3 same symbols in a row
        if field[0] == field[1] == field[2] and field[0] != "E":
            status = "win"
            print(field[0] + " Player wins")
        elif field[3] == field[4] == field[5] and field[3] != "E":
            status = "win"
            print(field[3] + " Player wins")
        elif field[6] == field[7] == field[8] and field[6] != "E":
            status = "win"
            print(field[6] + " Player wins")
        elif field[0] == field[3] == field[6] and field[0] != "E":
            status = "win"
            print(field[0] + " Player wins")
        elif field[1] == field[4] == field[7] and field[1] != "E":
            status = "win"
            print(field[1] + " Player wins")
        elif field[2] == field[5] == field[8] and field[2] != "E":
            status = "win"
            print(field[2] + " Player wins")
        elif field[0] == field[4] == field[8] and field[0] != "E":
            status = "win"
            print(field[0] + " Player wins")
        elif field[2] == field[4] == field[6] and field[2] != "E":
            status = "win"
            print(field[2] + " Player wins")
        # draw = all fields filled and no win
        elif "E" not in field:
            status = "draw"
            print("The game ends in a DRAW")

        # write field
        print("\n " + field[0] + " | " + field[1] + " | " + field[2] +
              "\n " + field[3] + " | " + field[4] + " | " + field[5] +
              "\n " + field[6] + " | " + field[7] + " | " + field[8])
