def splited_txt(text):
    txt = text.split()

    return txt

def splited_words(word):
    wrd = list(word)

    return wrd

source_text = input("text - ")

for w in splited_txt(source_text):
    print(splited_words(w))