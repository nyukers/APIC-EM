import json

# Можно загрузить содержимое JSON-файла в переменную data
with open("json-example.json") as f:
    data = f.read()

	# json_dict - это словарь, а json.loads отвечает за размещение данных JSON в этом словаре.
json_dict = json.loads(data)

# Вывод информации о сформированной в результате структуре данных Python
print("The JSON document is loaded as type {0}\n".format(type(json_dict)))

# "Документ JSON загружается как тип ... "
print("Now printing each item in this document and the type it contains")

# "Теперь выводится каждый элемент этого документа и тип данных, содержащихся в нем"
for k, v in json_dict.items():
    print("-- The key {0} contains a {1} value.".format(str(k), str(type(v)))
# "-- Ключ {0} содержит значение {1}."
)
