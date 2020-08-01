import math


def classic_round(num, d_places=2):
    if not isinstance(num, float):
        num = float(num)
        if not isinstance(d_places, int):
            d_places = int(d_places)
    if d_places == 0:
        return int(num-0.5)+1
    else:
        x, y = str(num).split(".")[0], str(num).split(".")[1]
        if len(y) > d_places and y[-1] == "5":
            return float(x + "." + str(round(float(str("0.") + y), d_places)).split(".")[1])
        else:
            return round(num, d_places)
