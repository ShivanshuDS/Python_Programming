# Enter RGB color character and find out which character you have entered.
rgb=input("Enter a RGB Character(R,G,B):-").upper()
if rgb=='R':
    print(f"{rgb} for Red. you are choose red color")
elif rgb=='G':
    print(f"{rgb} for Green. you are choose red color")
elif rgb=='B':
    print(f'{rgb} for Black. you are choose black color')
else:
    print(f'{rgb} choose invalid char')