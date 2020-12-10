# Импорт библиотек Jinja2 и PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml

# Объявление среды выполнения шаблона
ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    """ get_interface_speed returns the default Mbps value for a given
        network interface by looking for certain keywords in the name
    """
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

# Фильтры добавляются в объект ENV после его объявления. Отметим, что
# в действительности здесь передается только имя функции get_interface_speed,
# но она не вызывается - механизм шаблонов автоматически выполнит эту функцию
# после вызова template.render().
ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("templatestuff/template.j2")

# Загружаются данные из YAML-файла и передаются в шаблон для обработки.
with open("templatestuff/data.yml") as f:
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))
