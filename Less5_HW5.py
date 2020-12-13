#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summ():
    try:
        with open('HW5.txt', 'w+') as file_obj:
            line = input('Введите цифры: \n')
            file_obj.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Номер неверный')

summ()