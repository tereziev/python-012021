"""
Zopakuj si postup při instalaci modulu. Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně, ale umí si kurz měny stáhnout z internetu.

V PyCharmu klikni na File -> Settings -> Project -> Python Interpreter. Následně klikni na tlačítko + (Install) a vyhledej modul forex-python.
Dále klini na Install Package a potvrď instalaci.

Dále se podívej na následující příklad, jak s modulem pracovat. Na prvním řádku je import, aby Python věděl, že s modulem chceme pracovat.
Na druhém řádku vytvoříme objekt prevodnik (je to objekt třídy CurrencyRates), který se stará o převod měn.

Uvažujme třeba, že chceme spočítat, kolik by nás stálo, pokud bychom chtěli 10 dolarů. Použijeme funkci convert(),
která má jako první parametr zkraktu cílové měny, jako druhé parametr zkratku zdrojové měny a jako třetí parametr množství požadovaných dolarů.
Funkce vypočte, kolik jednotek zdrojové měny je potřeba zaplatit, aby to odpovídalo požadovanému množství cílové měny.

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = 10
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()).
Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK. Následně od uživatele získej i požadované množství cílové měny.
Nezapomeň toho množství převést na typ int.
"""
import math
from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovana_mena = input("Zadejte požadovanou měnu (EUR/GBP/DKK): ")
pozadovano_v_cilove_mene = int(input("Zadejte požadovanou částku v cílové měně: "))
cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)
print(f'Vložte částku: {round(cena_v_korunach)} Kč.')

