RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


for x in range(12):                            #флаг Нидерландов
    if x < 4: print(f'{RED}{" " * 40}{END}')  
    elif x < 8: print(f'{WHITE}{" " * 40}{END}')
    else: print(f'{BLUE}{" " * 40}{END}')
    
