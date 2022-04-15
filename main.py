def splited_txt(text):
    txt = text.split()

    return txt

def splited_words(word):
    wrd = list(word)

    return wrd

source_text = input("text - ")

eng_word = ["`", 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
rus_word = ['ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']

for w in splited_txt(source_text):
    #print(splited_txt(source_text))
    for tr in w:
            if tr in eng_word:
                print(rus_word[eng_word.index(tr)])