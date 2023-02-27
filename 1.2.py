password = input('Введите пароль:')
if len(password)<6:
    print ('Слишком короткий пароль')
elif password [0:7] == "abricos":
    print('Ненадёжный пароль')
else:
    print('Надёжный пароль')