def upper(text):
    '''Возвращает текст заглавными буквами'''
    return text.upper()

def upper_first_letter(text):
    '''Делает каждую первую букву всех слов загловными'''
    words = text.split(' ')
    upper_first_letter_words = [word.title() for word in words]
    return ' '.join(upper_first_letter_words)
