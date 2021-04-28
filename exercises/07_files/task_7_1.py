# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt') as f:
    for line in f:
        line = line.replace(",", " ").replace("[", "").replace("]", "")
        line = line.split()
        n1,ip,metr,n2,gw,tim,intf = line
        print('''
Prefix             {0:<25}
AD/Metric          {1:<25}
Next-Hop           {2:<25}
Last update        {3:<25}
Outbound Interface {4:<25}'''.format(ip,metr,gw,tim,intf))