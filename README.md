### Статсус тестов:
[![Actions Status](https://github.com/K0Hb/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/K0Hb/python-project-lvl2/actions)
<a href="https://codeclimate.com/github/K0Hb/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/568fa041cd5ff0b16dc4/test_coverage" /></a>
<a href="https://codeclimate.com/github/K0Hb/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/568fa041cd5ff0b16dc4/maintainability" /></a>
____
### Добро пожаловать на страницу репозитория моего 2ого проекта. 
______
### Описание:
Программа gendiff находит различия в файлах и выводит их в 3 форматах (JSON и YML/YAML).
______
### Установка:
`pip install git+https://github.com/K0Hb/python-project-lvl2.git`
______
### Использование:
# Вызов:
`gendiff --format path/to/file1 path/to/file2`
# Можно вызвать справку используя флаг:
`gendiff -h`
# Формат вывода  по умолчанию 'stylish' , так же возможно выбрать формат вывода 'plain' и 'json' с помощью флага:
`gendiff --format plain`