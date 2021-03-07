sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kodSoucastky = input("Zadejte kód součástky: ")
pocestKusu = int(input("Zadejte požadované množství: "))

if kodSoucastky in sklad:
    #soucastka = int(sklad[kodSoucastky])
    #if soucastka >= pocestKusu:
    if sklad[kodSoucastky]
        print("Poptávku lze uspokojit v plné výši.")
        #sklad[kodSoucastky] = soucastka - pocestKusu
        print(f"Na skladě zbývá: {sklad[kodSoucastky] - pocestKusu}.")
    else:
        #print(f"Součástka je skladem jen ve výši {soucastka} kusů.")
        print(f"Součástka je skladem jen ve výči {sklad[kodSoucastky]} kusů.")
        sklad.pop(kodSoucastky)
else:
    print(f"Součáskta {kodSoucastky} není skladem.")