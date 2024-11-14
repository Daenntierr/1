import colorama
import inspect

# Отримуємо всі члени модуля colorama
for name, obj in inspect.getmembers(colorama):
    print(f'{name}: {obj}')

# Отримуємо деталі компонента наприклад, init
print("\nSignature of colorama.init:")
signature = inspect.signature(colorama.init)
print(signature)