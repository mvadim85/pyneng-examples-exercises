# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

# Из 2-х списков делаем словарь
command_mode = dict()
command_mode['access'] = access_template
command_mode['trunk'] = trunk_template

# создаем словарь с возможными вопросами
available_questions = {"trunk" : "Введите разрешенные VLANы:", "access" : "Введите номер VLAN:" }


# получаем данные от пользователя
input_mode =(input("Введите режим работы интерфейса (access/trunk):"))
interface = input("Введите тип и номер интерфейса:")
vlan = input(available_questions[input_mode])

# зменяем {} на номер влана
command_mode = "\n".join(command_mode[input_mode]).replace("{}", vlan)

print("interface " + interface)
print(command_mode)
