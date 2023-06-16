"""Напишите функцию, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление."""


def key_parametrs_only(**kwargs):
    reverted_dct = {}
    for key, value in kwargs.items():
        if isinstance(value, list | dict | set | bytearray | memoryview):
            value = str(value)
        reverted_dct[value] = key
    return reverted_dct


print(key_parametrs_only(name="Sergey", age=28, weight=34.5, hobbies=["runing", "dancing", "travelling"],
                         animals=("dog", "cat"), relatives={"Galya": "mother", "Alex": "brother"},
                         shops={"tea", "bread", "milk"}))
