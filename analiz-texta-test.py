import re
from collections import Counter

def analyze_text(text):
    """Анализирует текст и выдает подробную статистику"""
    # Основная статистика
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Подсчет символов
    char_count = len(text)
    char_no_spaces = len(text.replace(' ', ''))
    
    # Подсчет слов
    word_count = len(words)
    unique_words = len(set(words))
    
    # Самые частые слова
    word_freq = Counter(words)
    most_common = word_freq.most_common(5)
    
    # Длина предложений
    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
    
    return {
        'characters_total': char_count,
        'characters_no_spaces': char_no_spaces,
        'words_total': word_count,
        'words_unique': unique_words,
        'sentences': len(sentences),
        'avg_sentence_length': round(avg_sentence_length, 2),
        'most_common_words': most_common,
        'reading_time_minutes': round(word_count / 200, 1)  # 200 слов в минуту
    }

# Пример использования
sample_text = """
Python — это высокоуровневый язык программирования общего назначения. 
Он был создан Гвидо ван Россумом и впервые выпущен в 1991 году. 
Python поддерживает несколько парадигм программирования, включая процедурное, 
объектно-ориентированное и функциональное программирование.
"""

stats = analyze_text(sample_text)
print("=== АНАЛИЗ ТЕКСТА ===")
for key, value in stats.items():
    print(f"{key}: {value}")
