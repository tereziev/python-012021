"""
Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

    Zjisti, kolik má soubor řádek a kolik sloupců.
    Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
    U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru. Tentokrát využij způsob dle vlastního výběru :-)

"""
#import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twilio = pandas.read_csv("twlo.csv")

print("#1 Kolik má soubor řádek a kolik sloupců:")
#print(f"Soubor má {twilio.shape} sloupců a řádek.")
print(f"Soubor má {twilio.shape[0]} řádek.")
print(f"Soubor má {len(twilio.columns)} sloupců.")

print("---")

print("#2 Načíst 5 prvních řádků s cenami:")
print(twilio.head())
print(twilio.iloc[0:5,])

print("---")

print("#3 Podívej se na poslední řádek souboru:")
print(twilio.tail(1))
print(twilio.iloc[-1:,])