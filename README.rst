=========================
python-num-variations-pl
=========================

This repository hosts project for generating plural forms of polish words in python (for Django).

When to use it? (in Polish)
============================

Chcia�by� �eby jaki� wyraz by� odmieniany w zale�ono�ci od liczby przy jakiej stoi? Dzi�ki temu projektowi mo�esz dokona� automatyczniej odmiany wyrazu w zale�no�ci od liczby. Zamiast:
:: 
  1 s��wko, 2 s��wko, 3 s��wko,..., 23425 s��wko,...

uzyskasz:
::
  1 s��wko, 2 s��wka, 3 s��wka,..., 23425 s��wek,...

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
      nw.addWords([u"widelec",u"widelc�w",u"widelce"])
	  # add multiple words with variations
      nw.addWordsList([[u"pi�ka",u"pi�ek",u"pi�ki"],[u"�y�ka",u"�y�ek",u"�y�ki"]])
	  return nw.get_word_int_formatted(word,number)
