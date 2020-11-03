text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

nWords = len(text.split())

print("Liczba słów: " + str(nWords))

# słownik
chars = {}

for char in text:
    chars[char] = chars.get(char, 0) + 1

print("Ilość wystąpień dla każdej litery: ")
print(chars)