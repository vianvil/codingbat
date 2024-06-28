def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        if you <=2 or date <=2:
            return 0
        else:
            return 2
    elif you > 2 and date > 2:
        return 1