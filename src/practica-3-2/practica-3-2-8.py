#!/usr/bin/env python3

import os

def check_translation(translation: str) -> list[str, str]:
    if translation.find(":") == -1:
        return (False, False)
    else:
        translation = translation.split(":")
        es = translation[0].strip()
        en = translation[1].strip()
        
        return (es, en)

def add_dictionary(es_en:dict, es: str, en: str) -> dict:
    try:
        es_en[es] = en
        return es_en
    except Exception as e:
        print("\n[-] ERROR When adding es_en dictionary: \n{e}")
        exit()

def check_save(i: str) -> bool:
    i = i.strip().lower().replace('"', '').replace("'", "").replace(' ', '')
    if i == "save" or i == "guardar":
        return True
    else:
        return False

def make_translator(es_en: dict) -> dict:
    save = False
    while not save:
        translation = input("~> ").strip()
        save = check_save(translation)
        if not save:
            es, en = check_translation(translation)
            if es == False or en == False:
                print("[-] ERROR: You haven't introduced a correct translation format.")
            else:
                es_en = add_dictionary(es_en, es, en)
                
    return es_en
            
def translate_sentence(sentence: str, es_en: dict) -> str:
    words = sentence.split(' ')
    translated_sentence = ""
    
    for word in words:
        if es_en[word]
    
    """ for word in words:
        for translation in es_en:
            if word.lower() == translation.lower():
                translated_word = translation.lower()
                if word[0].isupper():
                    translated_word = translated_word.capitalize()
            else:
                translated_word = word     
        translated_sentence += f" {translated_word}"
    return translated_sentence """
    
# Main function
def main():
    es_en = {}
    
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("──────────────────────────────────────────")
    print("Welcome to the Spanish-English Translator")
    print("──────────────────────────────────────────")
    
    print("(1) Make your translation dict!")
    print("- Introduce words for the translation in the following format (spanish:english)")
    print("- When you want to stop, just enter 'save'")
    es_en = make_translator(es_en)
    if es_en == {}:
        print("\nWe don't have anything to do, you haven't introduced any translation!\n")
    else:
        print("\n──────────────────────────────────────────")
        print("(2) Now write a sentence in spanish:")
        sentence = input("~> ").strip()
        print(es_en)
        print(sentence)
        translated_sentence = translate_sentence(sentence, es_en)
        print(translated_sentence)
        
    

# Start program
if __name__ == '__main__':
    main()