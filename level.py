# Calculations related to levels
def ability_points(level):
    if level >= 120:
        return 18 + level * 5
    else:
        return "fuck u"


def hyper_stats(level):
    if level == 300:
        return 1699
    elif level >= 290:
        return 18 * level - 3702
    elif level >= 280:
        return 17 * level - 3413
    elif level >= 270:
        return 16 * level - 3134
    elif level >= 260:
        return 15 * level - 2865
    elif level >= 250:
        return 14 * level - 2606
    else:
        return "fuck u"
