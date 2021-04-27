# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip=input('ip adress: ')
ip_oct=ip.split('.')
big=False
ip_correct=False
#проверка ввода

while not ip_correct:
  ip_oct=ip.split('.')
  if len(ip_oct) == 4 and (''.join(ip_oct)).isdigit(): #4 октета и цифры
    i=-1
    while i<len(ip_oct)-1:
      i+=1
      if ip_oct[i] and int(ip_oct[i]) < 256 and int(ip_oct[i]) >=0: #непустой октет и не минусовое значение
        big=True
        ip_correct=True
      else:
        big=False
        break
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
    ip=input('ip adress: ')
#это не глупо если это работает 2
#но под конец запутался уже