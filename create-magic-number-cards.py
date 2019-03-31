from string import ascii_uppercase, digits

def main():
    base = int(input("Numeric base? "))
    dec_places = int(input("Decimal places? "))

    high = base ** dec_places
    card_sets = [[[] for x in range(base-1)] for y in range(dec_places)]
    for x in range(1, high):
        converted = convertBase(x, base).rjust(dec_places, '0')

        for i, digit in enumerate(converted):
            if digit != "0":
                card_sets[i][int(digit)-1].append(x)

    letter_index = 0
    for card_set in card_sets:
        for card in card_set:
            print(ascii_uppercase[letter_index] + ": " + str(card))
            letter_index += 1

def convertBase(num,b):
    if num<b:
        return digits[num]
    else:
        return convertBase(num//b,b) + digits[num%b]

if __name__ == '__main__':
   main()
