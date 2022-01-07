def find(n):
    leftTeam = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }

    rightTeam = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1,
    }

    rightWins = 0
    leftWins = 0
    counter = 0

    while counter < len(n):
        for key, value in leftTeam.items():
            if key == n[counter]:
                counter += 1
                leftWins += value

        for key, value in rightTeam.items():
            if key == n[counter]:
                counter += 1
                rightWins += value


find("mwmwmwmwmwmwmmm")