users_base = {"nana":"maluje", "rysiu":"rzadzi","aniela":"haslo"}
i = 0
users = {}
login = input("podaj nazwe uzytkownika: ")
#passwd = input(f"podaj haslo dla uzytkownika {login} :")
#print(login, passwd)
#users[0]= {login:passwd}
#print(users[0])

for user in users_base:
#    print(user)
    if login == user:
        for i in range(3):
            passwd = input(f"podaj haslo dla uzytkownika {login} :")
            users[0] = {login: passwd}
 #           print(users_base[user])
            if passwd != users_base[user]:
                if i == 2:
                    print("wrong password. too many tries")
                    break
                else:
                    print("wrong password. TRY AGAIN")
 #                   print(i)
            if passwd == users_base[user]:
                print("you are connected")
                break
        break
    else:
        answer = input("this user doesn't exist in our database. DO you want to create an account?[y - yes, n - no]: ")
        break
print("koniec zadania")