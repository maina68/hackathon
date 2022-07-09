def fat_convert():
    fat_grams = int(input('Enter grams of fat you have taken today: '))
    converted = fat_grams * 9
    print(f'You have taken {converted} calories today')

    
def carbs_convert():
    carbs_grams = int(input('Enter grams of carbohydrates you have taken today: '))
    converted = carbs_grams * 9
    print(f'You have taken {converted} calories today')


print('''Please select a an operation(1 or 2)
1.fat_convert
2carbS_convert
''')

select = int(input('select an operator, 1 or 2 :'))
if select == 1:
    fat_convert()

else:
    carbs_convert()