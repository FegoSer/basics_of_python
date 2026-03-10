import os
# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# Слово для пошуку (варіант 5)
word_to_find = "Python"

# Слово для заміни та нове слово (варіант 6)
word_to_replace = "World"
replacement_word = "Ukraine"

# Новий рядок для додавання (варіант 7)
new_line = "Новий рядок додано"

# Новий вміст для перезапису (варіант 10)
new_content = "Файл перезаписано"

# Реалізуйте завдання тут
if os.path.exists(input_file):
    # Відкриваємо файл для читання якщо він існує
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Рахуємо слова split()
    words = content.split()
    count = len(words)
    
    # Запис результату в output.txt
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(count))
    
    # Виводимо результат у консоль
    print(count)
else:
    # Повідомлення про помилку якщо файл не знайдено
    print(f"Error: {input_file} not found")