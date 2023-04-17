ch=input("Enter any character :")
match ch.lower():
    case 'a'|'e'|'i'|'o'|'u':
        print("Vowel")
    
    case _:
        print("Consonant")
