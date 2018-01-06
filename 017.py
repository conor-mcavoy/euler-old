ones_letter_map = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
teens_letter_map = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
tens_letter_map = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}


total = 11
for x in range(1, 1000):
    size = 0
    tens_part = x % 100
    if tens_part < 10:
        size = ones_letter_map[tens_part]
    elif tens_part < 20:
        size = teens_letter_map[tens_part]
    else:
        tens_part_only = tens_part // 10
        ones_part = tens_part % 10
        size = tens_letter_map[tens_part_only] + ones_letter_map[ones_part]

    hundreds_part = x // 100
    if hundreds_part < 1:
        total += size
    elif tens_part != 0:
        total += 10 + ones_letter_map[hundreds_part] + size
    else:
        total += 7 + ones_letter_map[hundreds_part] + size

print(total)
