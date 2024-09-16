"""""
print('Hola')

def my_print(text):
  print(text * 2)

my_print('Este es mi texto ')
my_print('Hola ')

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b)

suma(1, 5)
suma(10, 4)
"""""


def max_num(numbers):
  numbers = list(numbers)
  max_number = numbers[0]
  for number in numbers:
    if number > max_number:
      max_number = number
  print("The max number is: ", max_number)
listnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_num(listnumbers)