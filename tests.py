# coding: utf-8
'''
Created on 2011-05-13

@author: berni
'''
from num_variations_pl import NumWords
import unittest
import num_variations_pl


class KnownValues(unittest.TestCase):
    '''
    Test case for known values
    '''
    known_values = (
                    ([22, u'słówko'], u'słówka'),
                    ([12, u'słówko'], u'słówek'),
                    ([4522, u'słówko'], u'słówka'),
                    ([32, u'słówko'], u'słówka'),
                    ([12, u'słówko'], u'słówek'),
                    ([111, u'słówko'], u'słówek'),
                    ([0, u'słówko'], u'słówek'),
                    ([1, u'słówko'], u'słówko'),
                    ([2, u'słówko'], u'słówka'),
                    ([-2, u'słówko'], u'słówka'),
                    ([234, u'słówko'], u'słówka'),
                    ([234231, 'komentarz'], 'komentarzy'),
                    ([1234232, 'komentarz'], 'komentarze'),
                    ([34230, 'komentarz'], 'komentarzy'),
                  )

    def test_get_word_int_formatted_known_values(self):
        """get_word_int_formatted should give known result with known input"""
        nw = NumWords()
        for lis, out in self.known_values:
            result = nw.get_word_int_formatted(lis[1], lis[0])
            self.assertEqual(out, result)

    def test_get_word_int_formatted_added_values(self):
        """get_word_int_formatted should give known result with known input"""
        nw = NumWords()
        nw.add_word([u"widelec", u"widelców", u"widelce"])
        nw.add_words([[u"piłka", u"piłek", u"piłki"], [u"łyżka", u"łyżek", u"łyżki"]])
        self.assertEqual(u"widelce", nw.get_word_int_formatted(u"widelec", 2))
        self.assertEqual(u"łyżek", nw.get_word_int_formatted(u"łyżka", 5))


class BadInput(unittest.TestCase):
    bad_query_strings = ("kasd", "asdafd", "komentasz", "baewda")
    not_ints = (2.5, float(2223123), 234.254, )

    def test_get_word_int_formatted_bad_input(self):
        """get should fail with words that are not in dict"""
        nw = NumWords()
        for s in self.bad_query_strings:
            self.assertRaises(num_variations_pl.NoSuchWordInDictionary, nw.get_word_int_formatted, s, 2)

    def test_get_word_int_formatted_not_int(self):
        """get should fail with numbers that are not int"""
        nw = NumWords()
        for n in self.not_ints:
            self.assertRaises(num_variations_pl.NotInteger, nw.get_word_int_formatted,
                              KnownValues.known_values[0][1], n)

if __name__ == "__main__":
    unittest.main()
