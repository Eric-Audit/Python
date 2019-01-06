#!/usr/bin/env python3
vowels = ("a", "e", "i", "o", "u")

def find_vowel(word):
            for i in range(len(word)):
               if word[i] in vowels:
                 return i
            return -1
def main():
    print("Pig Latin Translator")
    print()
    choice = "y"
    while choice.lower() == "y":
        raw_text = input("Enter text: ").strip()
        for char in "!@#$%^&*()_+{}|\;;'./<>?`~*-+":
            raw_text = raw_text.replace(char, "")
        raw_text = raw_text.lower()
        print("English:   ", raw_text)
        
        full_text =  raw_text.split()
        
        print("Pig Latin:  ")
        for word in full_text:
          vowel = find_vowel(word)  
          if(vowel == -1):
            print(word, ' ', end='')

          elif(vowel == 0):
            print(word + "way", ' ', end='')

          else:
            print(word[vowel:] + word[:vowel] + "ay", ' ', end='')
        print()
        print()
        choice = input("Continue? (y/n): ")
        print()

if __name__ == "__main__":
    main()
