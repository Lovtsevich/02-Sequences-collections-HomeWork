text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются"""

text = text.lower()
words = text.split()
polindroms = []

for ind in range(len(words)):
    word = words[ind].strip("!@#$%^&*()'_}{:\"?><.,}")
    rev_word = word[::-1]
    if (word == rev_word and len(word) > 1 and (word not in polindroms)):
        polindroms.append(word)
reversed_text = " ".join(words)

print(polindroms)