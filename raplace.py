
# объявление функции
def replace(text: str, old: str, new: str = ''):
    new_text = ''.join(new if i == old else i for i in text)
    print(new_text)

replace('Нет', 'т')
replace('Bella Ciao', 'a') 
replace('nobody; i myself farewell analysis', 'l', 'z') 
replace('commend me to my kind lord meaning', 'M', 'w') 