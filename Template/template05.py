# Импортирование библиотеки Jinja2
from jinja2 import Environment, FileSystemLoader

# bracket_expansion - библиотека от независимого производителя.
# Чтобы воспользоваться этой библиотекой, сначала установите ее с помощью pip.
from bracket_expansion import bracket_expansion

# Объявление среды выполнения шаблона
ENV = Environment(loader=FileSystemLoader('.'))

# Фильтры добавляются в объект ENV после его объявления.
# bracket_expansion - функция, передаваемая в механизм шаблонов;
# она будет автоматически выполняться при обработке шаблона.
ENV.filters['bracket_expansion'] = bracket_expansion
template = ENV.get_template("template.j2")

# Функция bracket_expansion, передаваемая в качестве фильтра, требует
# текстового образца для работы с ним. Такой образец передается
# в переменной iface_pattern
print(template.render(iface_pattern='GigabitEthernet0/0/[0-3]'))