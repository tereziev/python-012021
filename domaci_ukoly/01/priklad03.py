volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

pozadovanyCas = int(input("Zadejte požadovaný čas meetingu: "))

"""
for cas in volnePokoje:
    if pozadovanyCas == cas :
        print(f"V požadovaný čas jsou volné {len(volnePokoje[cas])} místnosti.")
"""

if pozadovanyCas in volnePokoje:
    print(f"V požadovaný čas jsoou volné {len(volnePokoje[pozadovanyCas])} místnosti.")
else:
    print("Neplatná hodina")
