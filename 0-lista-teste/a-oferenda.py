d = int(input())

FRIENDS_OFFER = {
    "ARTHUR": 10,
    "LUIZ": 30,
    "PEDRO": 100
}


def selectFriend(value):
    if value <= FRIENDS_OFFER["ARTHUR"]:
        return "Arthur"
    elif FRIENDS_OFFER["ARTHUR"] < value <= FRIENDS_OFFER["LUIZ"]:
        return "Luiz"
    elif FRIENDS_OFFER["LUIZ"] < value <= FRIENDS_OFFER["PEDRO"]:
        return "Pedro"
    else:
        return "Nenhum"


print(selectFriend(d))
