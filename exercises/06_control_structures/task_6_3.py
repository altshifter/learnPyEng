# -*- coding: utf-8 -*-
"""
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ними делать (добавлять, удалять, перезаписывать).

Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка
указывает как воспринимать номера VLAN, которые идут дальше.

Пример значения и соответствующей команды:
* ['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
* ['del', '17'] - команда switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - команда switchport trunk allowed vlan 11,30

Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть,
если в словаре trunk будут другие номера интерфейсов, код должен работать.

Для данных в словаре trunk_template вывод на
стандартный поток вывода должен быть таким:
interface FastEthernet 0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet 0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet 0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}
'''
for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
   '''
   # попытка номер раз   
'''
                               #ВАЩЕ НЕ УВЕРЕН ЧТО ТАК ДОЛЖНО БЫТЬ.... но работает
for intf, vlan in trunk.items():
    print("interface FastEthernet " + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            for keys, vlan in trunk.items():
              a=','.join(trunk[intf])
              if a.startswith('add,'):
                vlan2=a.replace('add,', 'add ')
                print(f" {command} {vlan2}")
                break
              elif a.startswith('only,'):
                vlan2=a.replace('only,', '')
                print(f" {command} {vlan2}")
                break
              elif a.startswith('del,'):
                vlan2=a.replace('del,', 'remove ')
                print(f" {command} {vlan2}")
                break
        else:
            print(f" {command}")
                                          #надо решения на задания посмотреть. мне кажется, что я делаю что-то не так
                                          #это не глупо если это работает 3
                                          '''
                                          # номер два

for intf, vlan in trunk.items():
  print(f"interface FastEthernet {intf}")
  for command in trunk_template:
    if command.endswith("allowed vlan"):
      do = vlan[0]
      vlans = ",".join(vlan[1:])
      if do == "add":
        print(f" {command} add {vlans}")
      elif do == "only":
        print(f" {command} {vlans}")
      elif do == "del":
        print(f" {command} remove {vlans}")
    else:
      print(f" {command}")

                                          