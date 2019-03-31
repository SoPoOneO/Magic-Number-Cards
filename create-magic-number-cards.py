def conv(num,b):
    convStr = "0123456789"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]

base = int(raw_input("Numeric base? "))
dec_places = int(raw_input("Decimal places? "))

high = base ** dec_places
card_sets = [[[] for x in range(base-1)] for y in range(dec_places)]
for x in range(1, high):
    converted = conv(x, base).rjust(dec_places, '0')

    for i in range( len(converted) ):
        dig = converted[i]
        if dig != "0":
            card_sets[i][int(dig)-1].append(converted + " => " + str(x))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_index = 0
for card_set in card_sets:
    for card in card_set:
        print letters[letter_index] + ": " + str(card)
        letter_index += 1
