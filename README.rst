=========================
python-num-variations-pl
=========================

This repository hosts project for generating plural forms of polish words in python (for Django).

When to use it? (in Polish)
============================

Chcia³byœ ¿eby jakiœ wyraz by³ odmieniany w zale¿onoœci od liczby przy jakiej stoi? Dziêki temu projektowi mo¿esz dokonaæ automatyczniej odmiany wyrazu w zale¿noœci od liczby. Zamiast:
:: 
  1 s³ówko, 2 s³ówko, 3 s³ówko,..., 23425 s³ówko,...

uzyskasz:
::
  1 s³ówko, 2 s³ówka, 3 s³ówka,..., 23425 s³ówek,...

Tak chyba jest lepiej? ;)

How to use it in Django:
=========================

You can add it to your tags.py, simplest way: 
::
  from num_variations_pl import NumWords
  @register.simple_tag
    def getWordIntVariation(word, number):
      nw = NumWords()
	  # add a new word with its variations 
      nw.addWords([u"widelec",u"widelców",u"widelce"])
	  # add multiple words with variations
      nw.addWordsList([[u"pi³ka",u"pi³ek",u"pi³ki"],[u"³y¿ka",u"³y¿ek",u"³y¿ki"]])
	  return nw.get_word_int_formatted(word,number)
