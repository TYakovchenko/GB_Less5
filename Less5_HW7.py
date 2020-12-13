#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.
import json
profit = {}
av = {}
okvd = 0
okvd_aver = 0
i = 0
with open('HW7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
    if profit.setdefault(name) >= 0:
            okvd = okvd + profit.setdefault(name)
            i += 1
    if i != 0:
        okvd_aver = okvd / i
        print(f'Средняя прибль - {okvd_aver:.2f}')
    else:
        print(f'коронавирус:/ Работа в убыток')
    av = {'средняя прибыль': round(okvd_aver)}
    profit.update(av)
    print(f'Прибыль каждой компании: {profit}')

with open('HW7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Файл с расширением json : \n '

f' {js_str}')