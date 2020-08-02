import decimal


def classic_round(num, d_places=2):
    if not isinstance(num, str):
        num = str(num)
        if not isinstance(d_places, int):
            d_places = int(d_places)
    d_places_value = '0'
    if d_places == 0:
        return int(decimal.Decimal(num).quantize(decimal.Decimal('0'),rounding=decimal.ROUND_HALF_UP))
    else:
        return float(decimal.Decimal(num).quantize(decimal.Decimal('0.'+('0'*d_places)),rounding=decimal.ROUND_HALF_UP))
