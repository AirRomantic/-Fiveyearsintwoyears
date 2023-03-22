import re


def prime_numbers(low, high):
    if not isinstance(low, int) or not isinstance(high, int):
        return []
    if low < 2:
        low = 2
    primes = []
    for num in range(low, high + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes


def text_stat(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return {'error': 'Файл не найден'}
    except OSError:
        return {'error': 'Неверный дескриптор'}
    word_amount = len(re.findall(r'\b\w+\b', text))
    paragraph_amount = len(re.findall(r'\n\n+', text)) + 1
    letter_stats = {}
    for letter in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        frequency = text.lower().count(letter) / len(text)
        word_count = len(re.findall(r'\b\w*{}+\w*\b'.format(letter), text.lower()))
        letter_stats[letter] = (frequency, word_count / word_amount)
    bilingual_word_amount = len(re.findall(
        r'\b\w*[a-z]+\w*[абвгдеёжзийклмнопрстуфхцчшщъыьэюя]+\w*\b|\b\w*[абвгдеёжзийклмнопрстуфхцчшщъыьэюя]+\w*[a-z]+\w*\b',
        text.lower()))
    stats = {}
    stats.update({letter: stats_tuple for letter, stats_tuple in letter_stats.items()})
    stats.update({
        'word_amount': word_amount,
        'paragraph_amount': paragraph_amount,
        'bilingual_word_amount': bilingual_word_amount,
    })
    return stats


def roman_numerals_to_int(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for i in reversed(roman_numeral):
        value = roman_numerals[i]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    return result

