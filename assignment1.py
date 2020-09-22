i = input()
thriller = ["dark","mindhunter","parasite","inception","insidious","interstellar","prison break","money heist","war","jack ryan"]
comedy = ["friends","3 idiots","brooklyn 99","how i met your mother","rick and morty","the big bang theory","the office","space force"]
if i.lower() in thriller : 
    print("It is a thriller")
elif i.lower() in comedy : 
    print("It is a comedy")
else : 
    print("It's neither comedy nor thriller")