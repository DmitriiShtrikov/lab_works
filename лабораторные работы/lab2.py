def greet(name):
    print('Привет,',name+'.')
greet(input('Введите имя:'))

def square(number):
    print(number**2)
square(int(input('Введите число:')))

def max_of_two(x, y):
    if x>y:
        print(x)
    else:
        print(y)
x = int(input('Введите первое число:'))
y = int(input('Введите второе число:'))
result=max_of_two(x, y)
def describe_person(name, age=30):
    print('ваше имя:',name)
    if age=='':
        age=30
    else:
        know_age=int(input('Хотите внести возраст? (1=ДА  2=НЕТ):'))
        if know_age == 1:
            print('Здравствуйте,', name + ',', 'ваш возраст:', age)
        else:
            print('Здравствуйте,', name + ',', 'ваш возраст: неизвестен')
    print('Здравствуйте,', name + ',', 'ваш возраст:', age)
print(describe_person(input('Введите имя '), input('Введите возраст')))
def is_prime(number):
    for i in range(2,int(number)):
        if number % i == 0 and number != 0:
            return False
        else:
            return True

print(is_prime(int(input('Введите простое число '))))