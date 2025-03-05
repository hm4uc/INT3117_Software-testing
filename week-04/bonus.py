def bonus(year: int, target: bool) -> int:
    bonus_amount = 0

    if year < 0:
        raise ValueError("year must be >= 0")
    
    if target: 
        if 0 <= year < 1:
            bonus_amount = 5000000
        elif 1 <= year < 3:
            bonus_amount = 10000000
        else:
            bonus_amount = 15000000
    
    return bonus_amount
