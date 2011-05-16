# -*- coding: utf-8 -*-

'''
Created on 2010-04-11

@author: berni
'''

#Define exceptions
class NoSuchWordInDictionary(Exception): pass     
class NotInteger(Exception): pass 

class NumWords(object):

    # default built-in polish words
    dictionary = [ ['komentarz','komentarzy','komentarze'] ,
                    [u'słówko',u'słówek',u'słówka'] ,
                    # add your additional words here
                 ]

    def add_words(self,one_words_list):
        self.dictionary.append(one_words_list)
        
    def add_words_list(self,multiple_words_list):
        self.dictionary.extend(multiple_words_list)
        
    def get_word_int_formatted(self, word, number):
        ldigits = lambda n, l=[]: not n and l or l.insert(0,n%10) or ldigits(n/10,l)
        if not isinstance(number, int):
            raise NotInteger
        if number<0:
            number *=-1
        digits = ldigits(number)

        out = None
        for list in self.dictionary:
            if list[0] == word:
                out = list
        if out is None:
            raise NoSuchWordInDictionary
                 
        if number == 1:
            return word
        elif digits[-1] in [0,1] or ( digits[-1] >= 5 and digits[-1] <=9) or number in [12,13,14] : 
            # 16,26,27,28,29,30,21
            return out[1]
        elif number > 1000 and (digits[-2] > 10):
            return out[1]
        else:
            return out[2] 
        return word