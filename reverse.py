text = input('Seu texto: ')
reversedText = ''

for l in range(len(text), 0, -1):
    reversedText += text[l - 1]
    
print(reversedText)
