users_base = {"nana":"maluje", "rysiu":"rzadzi","aniela":"haslo"}

users = {}
login = input("podaj nazwe uzytkownika: ")
#passwd = input(f"podaj haslo dla uzytkownika {login} :")
#print(login, passwd)
#users[0]= {login:passwd}
#print(users[0])

for user in users_base:
#    print(user)
    if login == user:
#        print(users_base[user])
        passwd = input(f"podaj haslo dla uzytkownika {login} :")
        users[0]= {login:passwd}
        if passwd == users_base[user]:
            print("you are connected")
            break
        #for password in users_base[user]:
        else:
            print("wrong password")
            break
    else:
        answer = input("this user doesn't exist in our database. DO you want to create an account?[y - yes, n - no]: ")
        break
print("koniec zadania")