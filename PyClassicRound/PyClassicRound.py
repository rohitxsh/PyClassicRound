import decimal


def classic_round(num, d_places=2):
    try:
        if not isinstance(d_places, int): d_places = int(d_places)
        return int(float(num)-0.5)+1 if d_places == 0 else float(decimal.Decimal(str(num)).quantize(decimal.Decimal('0.'+('0'*d_places)), rounding = decimal.ROUND_HALF_UP))
    except:
        return None
