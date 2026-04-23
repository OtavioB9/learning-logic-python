running_total = 0

num_of_friends = int(input('Coloque o número de amigos: '))

appertizers = float(input('Coloque o valor total gasto com aperitivos: '))

main_courses = float(input('Coloque o valor total gasto com pratos principais: '))

drinks = float(input('Coloque o valor total gasto com bebidas: '))

running_total += appertizers + main_courses + drinks
print('Valor total da conta', running_total)

tip = round (running_total * 0.10, 2)
print('Gorjeta (10%)', tip)

running_total += tip
print(f'Valor total da conta com gorjeta: R$ {running_total:.2f}')


final_bill = running_total/num_of_friends
print(f'O valor total dividido por pessoa ficou R$ {final_bill:.2f}')

each_pays = round (final_bill,2 )
print(f'Cada pessoa deve pagar R$ {each_pays:.2f}')
