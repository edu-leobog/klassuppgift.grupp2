import random 

namn = input("Vad heter du? ")
print("jag heter stensaxpåsemästaren, nu ska det spelas! ")

omgångar = int(input("Hur många omgångar vill du spela? "))
if omgångar <= 0 or omgångar > 10:
    print("Du måste spela mellan 1 och 10 omgångar!")
    exit("Avslutar spelet.")

print(f"Vi ska spela {omgångar} omgångar, lycka till {namn}!")

score = 0

for i in range(omgångar):

    computer_val = random.choice(["sten", "sax", "påse"])

    val = input("Välj mellan sten, sax eller påse: ")
    print(f"du valde {val}")
    print(f"omgång {i + 1} av {omgångar}")
    if val == computer_val:
        print("Det blev oavgjort!")
    elif val == "sten" and computer_val == "sax" or val == "sax" and computer_val == "påse" or val == "påse" and computer_val == "sten":
        score = score + 1 
        print(f"Du vann! Datorn valde {computer_val}")
    elif val == "sten" and computer_val == "påse" or val == "sax" and computer_val == "sten" or val == "påse" and computer_val == "sax":
        print(f"Du förlorade! Datorn valde {computer_val}")
    else:
       if val != "sten" and val != "sax" and val != "påse":
        print("Ogiltigt val, försök igen.")

    print(f"Poäng: {score} av {omgångar}")

if score > omgångar / 2:
    print("Du vann spelet!")
elif score == omgångar / 2:
    print("Det blev oavgjort!")
else:
    print("Datorn vann spelet!")