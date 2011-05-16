=========================
python-num-variations-pl
=========================

This repository hosts project for generating plural forms of polish words in python (for Django).

When to use it? (in Polish)
============================

Chciałbyś żeby jakiś wyraz był odmieniany w zależoności od liczby przy jakiej stoi? Dzięki temu projektowi możesz dokonać automatyczniej odmiany wyrazu w zależności od liczby. Zamiast:
:: 
  1 słówko, 2 słówko, 3 słówko,..., 23425 słówko,...

uzyskasz:
::
  1 słówko, 2 słówka, 3 słówka,..., 23425 słówek,...

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
      nw.addWordsList([[u"piłka",u"piłek",u"piłki"],[u"łyżka",u"łyżek",u"łyżki"]])
      return nw.get_word_int_formatted(word,number)