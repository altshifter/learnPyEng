# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
              #попытка 1. работает, но очень криво все.
'''
ip=input('ip adress: ')
ip_oct=ip.split('.')
big=False
#проверка ввода
if len(ip_oct) == 4 and (''.join(ip_oct)).isdigit():
  i=-1
  while i<len(ip_oct)-1:
    i+=1
    if ip_oct[i] and int(ip_oct[i]) < 256 and int(ip_oct[i]) >=0:
      big=True
    else:
      big=False
      break
else:
  print('Неправильный IP-адрес')  
#последняя проверка и ответы
if big:                                 
  if ip == '0.0.0.0':
    print('unassigned')
  elif ip == '255.255.255.255':
    print('local broadcast')
  elif int(ip_oct[0]) <= 223:
    print('unicast')
  elif int(ip_oct[0]) <= 239 and int(ip_oct[0]) >= 224:
    print('multicast')
  else:
    print('unused')
else:
  print('Неправильный IP-адрес')
#это не глупо если это работает
'''
#пробежался по решениям.. мдее.. надо заного прочитать тему.. попробую еще раз
#попытка 2

ip=input('ip adress: ')
ip_oct=ip.split('.')
correct_ip=True

if len(ip_oct) != 4:
  correct_ip=False
for num in ip_oct:
  correct_ip = num.isdigit() and 0 <= int(num) <= 255 and correct_ip

if correct_ip:                                 
  if ip == '0.0.0.0':
    print('unassigned')
  elif ip == '255.255.255.255':
    print('local broadcast')
  elif int(ip_oct[0]) <= 223:
    print('unicast')
  elif 239 >= int(ip_oct[0]) >= 224:
    print('multicast')
  else:
    print('unused')
else:
  print('Неправильный IP-адрес')