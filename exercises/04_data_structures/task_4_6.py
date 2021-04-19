# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

v1=ospf_route.replace('[', ' ')
v2=v1.replace(']', ' ')
v3=v2.replace(',', ' ')
result1 = v3.split()
result1.remove('via')
prefix, ad_Metric, next_hop, last_update, outbound_interface = result1

result = '''
Prefix                {:20}
AD/Metric             {:20}
Next-Hop              {:20}
Last update           {:20}
Outbound Interface    {:20}
'''

print(result.format(prefix, ad_Metric, next_hop, last_update, outbound_interface))
