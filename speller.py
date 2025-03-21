from spellchecker import SpellChecker

spell = SpellChecker()

def correct_sentence(sentence):
    words = sentence.split()
    corrected_words = [spell.correction(word) or word for word in words]
    return " ".join(corrected_words)

#print(correct_sentence("whta is the weathar like?")) 
#print(correct_sentence("I want to gö to longon"))