
apetece_helado = input("¿Te apetece un helado? (Si / No): ").upper()
tiene_dinero = input("¿Pero tienes dinero para helado? (Si / No): ").upper()
tu_tia = input("¿Estas con tu tia? (Si / No)").upper()

if apetece_helado == "SI" and tiene_dinero == "SI" or tu_tia == "SI":
    print("Pues compratelo tolete")
else:
    print("Pues nada entonces")