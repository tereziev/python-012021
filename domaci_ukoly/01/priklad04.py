morseCode = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

message = input("Zadejte zprávu, kteru chcete převézt do morseovky: ")

#řešení bez mezer:

for sign in message:
        #for code in morseCode:
        #    if sign == code:
        #        print(morseCode[sign], end=" ")
        print(morseCode[sign], end=" ")

#řešení s mezerami mezi slovy ve větě:

if sign in morseCode:
    print(morseCode[sign], end=" ")
elif sign == " ":
    print('/', end=" ")
else:
    print('??', end=" ")
