
# объявление функции
def replace(text: str, old: str, new: str = ''):
    new_text = ''
    for i in text:
        if i == old:
            new_text += new
        else:
            new_text += i
    print(new_text)

replace('Нет', 'т')
replace('Bella Ciao', 'a') 
replace('nobody; i myself farewell analysis', 'l', 'z') 
replace('commend me to my kind lord meaning', 'M', 'w') 