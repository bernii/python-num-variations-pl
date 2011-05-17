# -*- coding: utf-8 -*-
'''
Created on 2010-04-11

@author: berni
'''

#Define exceptions


class NoSuchWordInDictionary(Exception):
    '''
    Unable to return word variation as it is not available in dictionary
    '''
    pass


class NotInteger(Exception):
    '''
    Passed number is not an integer
    '''
    pass


class NumWords(object):
    '''
    Get word variation for a number
    '''

    # default built-in polish words
    dictionary = [['komentarz', 'komentarzy', 'komentarze'],
                  [u'słówko', u'słówek', u'słówka'],
                  # add your additional words here
                 ]

    def add_word(self, one_words_list):
        '''
        Add word to dictionary
        @param one_words_list: List with word variations
        '''
        self.dictionary.append(one_words_list)

    def add_words(self, multiple_words_list):
        '''
        Add multiple words to dictionary
        @param multiple_words_list: List with words variations
        '''
        self.dictionary.extend(multiple_words_list)

    def get_word_int_formatted(self, word, number):
        '''
        Main function for getting word for a specific number
        @param word:
        @param number:
        '''
        ldigits = lambda n, l = []: not n and l or l.insert(0, n % 10) or ldigits(n / 10, l)
        if not isinstance(number, int):
            raise NotInteger
        if number < 0:
            number *= -1
        digits = ldigits(number)

        out = None
        for wlist in self.dictionary:
            if wlist[0] == word:
                out = wlist
        if out is None:
            raise NoSuchWordInDictionary

        if number == 1:
            return word
        elif digits[-1] in [0, 1] or (digits[-1] >= 5 and digits[-1] <= 9) or number in [12, 13, 14]:
            # 16,26,27,28,29,30,21
            return out[1]
        elif number > 1000 and (digits[-2] > 10):
            return out[1]
        else:
            return out[2]
        return word
