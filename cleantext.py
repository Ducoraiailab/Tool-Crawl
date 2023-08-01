
import re
from unicodedata import normalize
def remove_icon_facebook(s):
    fb_icons = [':-)', ':)', ':]', '=)', ':-(', ':(', ':[', '=(', ':-P', ':P', ':-p', ':p', ':-D', ':D', '=D', '-O',
                ':O',
                ':-o', ':o', '>:-(', '>:(', ';-)', ';)', ':-/', ':/', ':-\\', ':\\', ':’(', ':-*', ':*', '^_^', '-_-',
                'o.O',
                'O.o', '>-:O', '>:O', '>-:o', '>:o', ':v', ':3', '8-)', '8)', 'B-)', 'B)', '8-|', '8|', 'B-)', 'B|',
                ':$',
                'O:-)', 'O:)', '3:-)', '3:)', '<3', ':|]', ':putnam:', '(^^^)', '<(“)', '(y)', ':poop:']
    for fb_icon in fb_icons:
        s = s.replace(fb_icon, '')
    return s
def make_dictionary_literal():
    vietnamese_raw = [b'a\xcc\x80', b'\xc4\x83\xcc\x80', b'\xc3\xa2\xcc\x80', b'e\xcc\x80', b'\xc3\xaa\xcc\x80',
                      b'i\xcc\x80', b'o\xcc\x80', b'\xc3\xb4\xcc\x80', b'\xc6\xa1\xcc\x80', b'u\xcc\x80',
                      b'\xc6\xb0\xcc\x80', b'y\xcc\x80',
                      b'a\xcc\x81', b'\xc4\x83\xcc\x81', b'\xc3\xa2\xcc\x81', b'e\xcc\x81', b'\xc3\xaa\xcc\x81',
                      b'i\xcc\x81', b'o\xcc\x81', b'\xc3\xb4\xcc\x81', b'\xc6\xa1\xcc\x81', b'u\xcc\x81',
                      b'\xc6\xb0\xcc\x81', b'y\xcc\x81',
                      b'a\xcc\x83', b'\xc4\x83\xcc\x83', b'\xc3\xa2\xcc\x83', b'e\xcc\x83', b'\xc3\xaa\xcc\x83',
                      b'i\xcc\x83', b'o\xcc\x83', b'\xc3\xb4\xcc\x83', b'\xc6\xa1\xcc\x83', b'u\xcc\x83',
                      b'\xc6\xb0\xcc\x83', b'y\xcc\x83',
                      b'a\xcc\x89', b'\xc4\x83\xcc\x89', b'\xc3\xa2\xcc\x89', b'e\xcc\x89', b'\xc3\xaa\xcc\x89',
                      b'i\xcc\x89', b'o\xcc\x89', b'\xc3\xb4\xcc\x89', b'\xc6\xa1\xcc\x89', b'u\xcc\x89',
                      b'\xc6\xb0\xcc\x89', b'y\xcc\x89',
                      b'a\xcc\xa3', b'\xc4\x83\xcc\xa3', b'\xc3\xa2\xcc\xa3', b'e\xcc\xa3', b'\xc3\xaa\xcc\xa3',
                      b'i\xcc\xa3', b'o\xcc\xa3', b'\xc3\xb4\xcc\xa3', b'\xc6\xa1\xcc\xa3', b'u\xcc\xa3',
                      b'\xc6\xb0\xcc\xa3', b'y\xcc\xa3']

    vietnamese_standard = [b'\xc3\xa0', b'\xe1\xba\xb1', b'\xe1\xba\xa7', b'\xc3\xa8', b'\xe1\xbb\x81', b'\xc3\xac',
                           b'\xc3\xb2', b'\xe1\xbb\x93', b'\xe1\xbb\x9d', b'\xc3\xb9', b'\xe1\xbb\xab', b'\xe1\xbb\xb3',
                           b'\xc3\xa1', b'\xe1\xba\xaf', b'\xe1\xba\xa5', b'\xc3\xa9', b'\xe1\xba\xbf', b'\xc3\xad',
                           b'\xc3\xb3', b'\xe1\xbb\x91', b'\xe1\xbb\x9b', b'\xc3\xba', b'\xe1\xbb\xa9', b'\xc3\xbd',
                           b'\xc3\xa3', b'\xe1\xba\xb5', b'\xe1\xba\xab', b'\xe1\xba\xbd', b'\xe1\xbb\x85', b'\xc4\xa9',
                           b'\xc3\xb5', b'\xe1\xbb\x97', b'\xe1\xbb\xa1', b'\xc5\xa9', b'\xe1\xbb\xaf', b'\xe1\xbb\xb9',
                           b'\xe1\xba\xa3', b'\xe1\xba\xb3', b'\xe1\xba\xa9', b'\xe1\xba\xbb', b'\xe1\xbb\x83',
                           b'\xe1\xbb\x89', b'\xe1\xbb\x8f', b'\xe1\xbb\x95', b'\xe1\xbb\x9f', b'\xe1\xbb\xa7',
                           b'\xe1\xbb\xad', b'\xe1\xbb\xb7',
                           b'\xe1\xba\xa1', b'\xe1\xba\xb7', b'\xe1\xba\xad', b'\xe1\xba\xb9', b'\xe1\xbb\x87',
                           b'\xe1\xbb\x8b', b'\xe1\xbb\x8d', b'\xe1\xbb\x99', b'\xe1\xbb\xa3', b'\xe1\xbb\xa5',
                           b'\xe1\xbb\xb1', b'\xe1\xbb\xb5']


    dictionary = dict(zip(vietnamese_raw, vietnamese_standard))

    return dictionary
def convert_to_vietnamese_standard(s):
    return normalize('NFC', s)
def remove_raw_text(s):
    a = ' '.join(re.findall('[\w\(\)\.\,\:\- ]+', s))
    return " ".join(a.split()).strip()
def remove_other(s):
    # Bo chu xau
    d1 = [b'\xda\x80', b'\xda\x81', b'\xda\x82', b'\xda\x83', b'\xda\x84', b'\xda\x85', b'\xda\x86',
          b'\xda\x87', b'\xda\x88', b'\xda\x89', b'\xda\x8a', b'\xda\x8b', b'\xda\x8c', b'\xda\x8d',
          b'\xda\x8e', b'\xda\x8f', b'\xda\x90', b'\xda\x91', b'\xda\x92', b'\xda\x93', b'\xda\x94',
          b'\xda\x95', b'\xda\x96', b'\xda\x97', b'\xda\x98', b'\xda\x99', b'\xda\x9a', b'\xda\x9b',
          b'\xda\x9c', b'\xda\x9d', b'\xda\x9e', b'\xda\x9f', b'\xda\xa0', b'\xda\xa1', b'\xda\xa2',
          b'\xda\xa3', b'\xda\xa4', b'\xda\xa5', b'\xda\xa6', b'\xda\xa7', b'\xda\xa8', b'\xda\xa9',
          b'\xda\xaa', b'\xda\xab', b'\xda\xac', b'\xda\xad', b'\xda\xae', b'\xda\xaf', b'\xda\xb0',
          b'\xda\xb1', b'\xda\xb2', b'\xda\xb3', b'\xda\xb4', b'\xda\xb5', b'\xda\xb6', b'\xda\xb7',
          b'\xda\xb8', b'\xda\xb9', b'\xda\xba', b'\xda\xbb', b'\xda\xbc', b'\xda\xbd', b'\xda\xbe',
          b'\xda\xbf', b'\xdb\x80', b'\xdb\x81', b'\xdb\x82', b'\xdb\x83', b'\xdb\x84', b'\xdb\x85',
          b'\xdb\x86', b'\xdb\x87', b'\xdb\x88', b'\xdb\x89', b'\xdb\x8a', b'\xdb\x8b', b'\xdb\x8c',
          b'\xdb\x8d', b'\xdb\x8e', b'\xdb\x8f', b'\xdb\x90', b'\xdb\x91', b'\xdb\x92', b'\xdb\x93',
          b'\xdb\x94', b'\xdb\x95', b'\xdb\x96', b'\xdb\x97', b'\xdb\x98', b'\xdb\x99', b'\xdb\x9a',
          b'\xdb\x9b', b'\xdb\x9c', b'\xdb\x9d', b'\xdb\x9e', b'\xdb\x9f', b'\xdb\xa0', b'\xdb\xa1',
          b'\xdb\xa2', b'\xdb\xa3', b'\xdb\xa4', b'\xdb\xa5', b'\xdb\xa6', b'\xdb\xa7', b'\xdb\xa8',
          b'\xdb\xa9', b'\xdb\xaa', b'\xdb\xab', b'\xdb\xac', b'\xdb\xad', b'\xdb\xae', b'\xdb\xaf',
          b'\xdb\xb0', b'\xdb\xb1', b'\xdb\xb2', b'\xdb\xb3', b'\xdb\xb4', b'\xdb\xb5', b'\xdb\xb6',
          b'\xdb\xb7', b'\xdb\xb8', b'\xdb\xb9', b'\xdb\xba', b'\xdb\xbb', b'\xdb\xbc', b'\xdb\xbd',
          b'\xdb\xbe', b'\xdb\xbf']
    d2 = [b'\xe1\x9e\x80', b'\xe1\x9e\x81', b'\xe1\x9e\x82', b'\xe1\x9e\x83', b'\xe1\x9e\x84', b'\xe1\x9e\x85',
          b'\xe1\x9e\x86', b'\xe1\x9e\x87', b'\xe1\x9e\x88', b'\xe1\x9e\x89', b'\xe1\x9e\x8a', b'\xe1\x9e\x8b',
          b'\xe1\x9e\x8c',
          b'\xe1\x9e\x8d', b'\xe1\x9e\x8e', b'\xe1\x9e\x8f', b'\xe1\x9e\x90', b'\xe1\x9e\x91', b'\xe1\x9e\x92',
          b'\xe1\x9e\x93',
          b'\xe1\x9e\x94', b'\xe1\x9e\x95', b'\xe1\x9e\x96', b'\xe1\x9e\x97', b'\xe1\x9e\x98', b'\xe1\x9e\x99',
          b'\xe1\x9e\x9a',
          b'\xe1\x9e\x9b', b'\xe1\x9e\x9c', b'\xe1\x9e\x9d', b'\xe1\x9e\x9e', b'\xe1\x9e\x9f', b'\xe1\x9e\xa0',
          b'\xe1\x9e\xa1',
          b'\xe1\x9e\xa2', b'\xe1\x9e\xa3', b'\xe1\x9e\xa4', b'\xe1\x9e\xa5', b'\xe1\x9e\xa6', b'\xe1\x9e\xa7',
          b'\xe1\x9e\xa8',
          b'\xe1\x9e\xa9', b'\xe1\x9e\xaa', b'\xe1\x9e\xab', b'\xe1\x9e\xac', b'\xe1\x9e\xad', b'\xe1\x9e\xae',
          b'\xe1\x9e\xaf',
          b'\xe1\x9e\xb0', b'\xe1\x9e\xb1', b'\xe1\x9e\xb2', b'\xe1\x9e\xb3', b'\xe1\x9e\xb4', b'\xe1\x9e\xb5',
          b'\xe1\x9e\xb6',
          b'\xe1\x9e\xb7', b'\xe1\x9e\xb8', b'\xe1\x9e\xb9', b'\xe1\x9e\xba', b'\xe1\x9e\xbb', b'\xe1\x9e\xbc',
          b'\xe1\x9e\xbd',
          b'\xe1\x9e\xbe', b'\xe1\x9e\xbf', b'\xe1\x9f\x80', b'\xe1\x9f\x81', b'\xe1\x9f\x82', b'\xe1\x9f\x83',
          b'\xe1\x9f\x84',
          b'\xe1\x9f\x85', b'\xe1\x9f\x86', b'\xe1\x9f\x87', b'\xe1\x9f\x88', b'\xe1\x9f\x89', b'\xe1\x9f\x8a',
          b'\xe1\x9f\x8b',
          b'\xe1\x9f\x8c', b'\xe1\x9f\x8d', b'\xe1\x9f\x8e', b'\xe1\x9f\x8f', b'\xe1\x9f\x90', b'\xe1\x9f\x91',
          b'\xe1\x9f\x92',
          b'\xe1\x9f\x93', b'\xe1\x9f\x94', b'\xe1\x9f\x95', b'\xe1\x9f\x96', b'\xe1\x9f\x97', b'\xe1\x9f\x98',
          b'\xe1\x9f\x99',
          b'\xe1\x9f\x9a', b'\xe1\x9f\x9b', b'\xe1\x9f\x9c', b'\xe1\x9f\x9d', b'\xe1\x9f\x9e', b'\xe1\x9f\x9f',
          b'\xe1\x9f\xa0',
          b'\xe1\x9f\xa1', b'\xe1\x9f\xa2', b'\xe1\x9f\xa3', b'\xe1\x9f\xa4', b'\xe1\x9f\xa5', b'\xe1\x9f\xa6',
          b'\xe1\x9f\xa7',
          b'\xe1\x9f\xa8', b'\xe1\x9f\xa9', b'\xe1\x9f\xaa', b'\xe1\x9f\xab', b'\xe1\x9f\xac', b'\xe1\x9f\xad',
          b'\xe1\x9f\xae',
          b'\xe1\x9f\xaf', b'\xe1\x9f\xb0', b'\xe1\x9f\xb1', b'\xe1\x9f\xb2', b'\xe1\x9f\xb3', b'\xe1\x9f\xb4',
          b'\xe1\x9f\xb5',
          b'\xe1\x9f\xb6', b'\xe1\x9f\xb7', b'\xe1\x9f\xb8', b'\xe1\x9f\xb9', b'\xe1\x9f\xba', b'\xe1\x9f\xbb',
          b'\xe1\x9f\xbc',
          b'\xe1\x9f\xbd', b'\xe1\x9f\xbe', b'\xe1\x9f\xbf']
    d3 = [b'\xcc\x80', b'\xcc\x81', b'\xcc\x82', b'\xcc\x83', b'\xcc\x84', b'\xcc\x85',
          b'\xcc\x86', b'\xcc\x87', b'\xcc\x88', b'\xcc\x89', b'\xcc\x8a', b'\xcc\x8b', b'\xcc\x8c',
          b'\xcc\x8d', b'\xcc\x8e', b'\xcc\x8f', b'\xcc\x90', b'\xcc\x91', b'\xcc\x92', b'\xcc\x93',
          b'\xcc\x94', b'\xcc\x95', b'\xcc\x96', b'\xcc\x97', b'\xcc\x98', b'\xcc\x99', b'\xcc\x9a',
          b'\xcc\x9b', b'\xcc\x9c', b'\xcc\x9d', b'\xcc\x9e', b'\xcc\x9f', b'\xcc\xa0', b'\xcc\xa1',
          b'\xcc\xa2', b'\xcc\xa3', b'\xcc\xa4', b'\xcc\xa5', b'\xcc\xa6', b'\xcc\xa7', b'\xcc\xa8',
          b'\xcc\xa9', b'\xcc\xaa', b'\xcc\xab', b'\xcc\xac', b'\xcc\xad', b'\xcc\xae', b'\xcc\xaf',
          b'\xcc\xb0', b'\xcc\xb1', b'\xcc\xb2', b'\xcc\xb3', b'\xcc\xb4', b'\xcc\xb5', b'\xcc\xb6',
          b'\xcc\xb7', b'\xcc\xb8', b'\xcc\xb9', b'\xcc\xba', b'\xcc\xbb', b'\xcc\xbc', b'\xcc\xbd',
          b'\xcc\xbe', b'\xcc\xbf', b'\xcd\x80', b'\xcd\x81', b'\xcd\x82', b'\xcd\x83', b'\xcd\x84',
          b'\xcd\x85', b'\xcd\x86', b'\xcd\x87', b'\xcd\x88', b'\xcd\x89', b'\xcd\x8a', b'\xcd\x8b',
          b'\xcd\x8c', b'\xcd\x8d', b'\xcd\x8e', b'\xcd\x8f', b'\xcd\x90', b'\xcd\x91', b'\xcd\x92',
          b'\xcd\x93', b'\xcd\x94', b'\xcd\x95', b'\xcd\x96', b'\xcd\x97', b'\xcd\x98', b'\xcd\x99',
          b'\xcd\x9a', b'\xcd\x9b', b'\xcd\x9c', b'\xcd\x9d', b'\xcd\x9e', b'\xcd\x9f', b'\xcd\xa0',
          b'\xcd\xa1', b'\xcd\xa2', b'\xcd\xa3', b'\xcd\xa4', b'\xcd\xa5', b'\xcd\xa6', b'\xcd\xa7',
          b'\xcd\xa8', b'\xcd\xa9', b'\xcd\xaa', b'\xcd\xab', b'\xcd\xac', b'\xcd\xad', b'\xcd\xae',
          b'\xcd\xaf', b'\xcd\xb0', b'\xcd\xb1', b'\xcd\xb2', b'\xcd\xb3', b'\xcd\xb4', b'\xcd\xb5',
          b'\xcd\xb6', b'\xcd\xb7', b'\xcd\xb8', b'\xcd\xb9', b'\xcd\xba', b'\xcd\xbb', b'\xcd\xbc',
          b'\xcd\xbd', b'\xcd\xbe', b'\xcd\xbf', b'\xce\x80', b'\xce\x81', b'\xce\x82', b'\xce\x83',
          b'\xce\x84', b'\xce\x85', b'\xce\x86', b'\xce\x87', b'\xce\x88', b'\xce\x89', b'\xce\x8a',
          b'\xce\x8b', b'\xce\x8c', b'\xce\x8d', b'\xce\x8e', b'\xce\x8f', b'\xce\x90', b'\xce\x91',
          b'\xce\x92', b'\xce\x93', b'\xce\x94', b'\xce\x95', b'\xce\x96', b'\xce\x97', b'\xce\x98',
          b'\xce\x99', b'\xce\x9a', b'\xce\x9b', b'\xce\x9c', b'\xce\x9d', b'\xce\x9e', b'\xce\x9f',
          b'\xce\xa0', b'\xce\xa1', b'\xce\xa2', b'\xce\xa3', b'\xce\xa4', b'\xce\xa5', b'\xce\xa6',
          b'\xce\xa7', b'\xce\xa8', b'\xce\xa9', b'\xce\xaa', b'\xce\xab', b'\xce\xac', b'\xce\xad',
          b'\xce\xae', b'\xce\xaf', b'\xce\xb0', b'\xce\xb1', b'\xce\xb2', b'\xce\xb3', b'\xce\xb4',
          b'\xce\xb5', b'\xce\xb6', b'\xce\xb7', b'\xce\xb8', b'\xce\xb9', b'\xce\xba', b'\xce\xbb',
          b'\xce\xbc', b'\xce\xbd', b'\xce\xbe', b'\xce\xbf', b'\xcf\x80', b'\xcf\x81', b'\xcf\x82',
          b'\xcf\x83', b'\xcf\x84', b'\xcf\x85', b'\xcf\x86', b'\xcf\x87', b'\xcf\x88', b'\xcf\x89',
          b'\xcf\x8a', b'\xcf\x8b', b'\xcf\x8c', b'\xcf\x8d', b'\xcf\x8e', b'\xcf\x8f', b'\xcf\x90',
          b'\xcf\x91', b'\xcf\x92', b'\xcf\x93', b'\xcf\x94', b'\xcf\x95', b'\xcf\x96', b'\xcf\x97',
          b'\xcf\x98', b'\xcf\x99', b'\xcf\x9a', b'\xcf\x9b', b'\xcf\x9c', b'\xcf\x9d', b'\xcf\x9e',
          b'\xcf\x9f', b'\xcf\xa0', b'\xcf\xa1', b'\xcf\xa2', b'\xcf\xa3', b'\xcf\xa4', b'\xcf\xa5',
          b'\xcf\xa6', b'\xcf\xa7', b'\xcf\xa8', b'\xcf\xa9', b'\xcf\xaa', b'\xcf\xab', b'\xcf\xac',
          b'\xcf\xad', b'\xcf\xae', b'\xcf\xaf', b'\xcf\xb0', b'\xcf\xb1', b'\xcf\xb2', b'\xcf\xb3',
          b'\xcf\xb4', b'\xcf\xb5', b'\xcf\xb6', b'\xcf\xb7', b'\xcf\xb8', b'\xcf\xb9', b'\xcf\xba',
          b'\xcf\xbb', b'\xcf\xbc', b'\xcf\xbd', b'\xcf\xbe', b'\xcf\xbf']
    d4 = [b'\xe0\xb8\x80', b'\xe0\xb8\x81', b'\xe0\xb8\x82', b'\xe0\xb8\x83', b'\xe0\xb8\x84', b'\xe0\xb8\x85',
          b'\xe0\xb8\x86', b'\xe0\xb8\x87', b'\xe0\xb8\x88', b'\xe0\xb8\x89', b'\xe0\xb8\x8a', b'\xe0\xb8\x8b',
          b'\xe0\xb8\x8c',
          b'\xe0\xb8\x8d', b'\xe0\xb8\x8e', b'\xe0\xb8\x8f', b'\xe0\xb8\x90', b'\xe0\xb8\x91', b'\xe0\xb8\x92',
          b'\xe0\xb8\x93',
          b'\xe0\xb8\x94', b'\xe0\xb8\x95', b'\xe0\xb8\x96', b'\xe0\xb8\x97', b'\xe0\xb8\x98', b'\xe0\xb8\x99',
          b'\xe0\xb8\x9a',
          b'\xe0\xb8\x9b', b'\xe0\xb8\x9c', b'\xe0\xb8\x9d', b'\xe0\xb8\x9e', b'\xe0\xb8\x9f', b'\xe0\xb8\xa0',
          b'\xe0\xb8\xa1',
          b'\xe0\xb8\xa2', b'\xe0\xb8\xa3', b'\xe0\xb8\xa4', b'\xe0\xb8\xa5', b'\xe0\xb8\xa6', b'\xe0\xb8\xa7',
          b'\xe0\xb8\xa8',
          b'\xe0\xb8\xa9', b'\xe0\xb8\xaa', b'\xe0\xb8\xab', b'\xe0\xb8\xac', b'\xe0\xb8\xad', b'\xe0\xb8\xae',
          b'\xe0\xb8\xaf',
          b'\xe0\xb8\xb0', b'\xe0\xb8\xb1', b'\xe0\xb8\xb2', b'\xe0\xb8\xb3', b'\xe0\xb8\xb4', b'\xe0\xb8\xb5',
          b'\xe0\xb8\xb6',
          b'\xe0\xb8\xb7', b'\xe0\xb8\xb8', b'\xe0\xb8\xb9', b'\xe0\xb8\xba', b'\xe0\xb8\xbb', b'\xe0\xb8\xbc',
          b'\xe0\xb8\xbd',
          b'\xe0\xb8\xbe', b'\xe0\xb8\xbf', b'\xe0\xb9\x80', b'\xe0\xb9\x81', b'\xe0\xb9\x82', b'\xe0\xb9\x83',
          b'\xe0\xb9\x84',
          b'\xe0\xb9\x85', b'\xe0\xb9\x86', b'\xe0\xb9\x87', b'\xe0\xb9\x88', b'\xe0\xb9\x89', b'\xe0\xb9\x8a',
          b'\xe0\xb9\x8b',
          b'\xe0\xb9\x8c', b'\xe0\xb9\x8d', b'\xe0\xb9\x8e', b'\xe0\xb9\x8f', b'\xe0\xb9\x90', b'\xe0\xb9\x91',
          b'\xe0\xb9\x92',
          b'\xe0\xb9\x93', b'\xe0\xb9\x94', b'\xe0\xb9\x95', b'\xe0\xb9\x96', b'\xe0\xb9\x97', b'\xe0\xb9\x98',
          b'\xe0\xb9\x99',
          b'\xe0\xb9\x9a', b'\xe0\xb9\x9b', b'\xe0\xb9\x9c', b'\xe0\xb9\x9d', b'\xe0\xb9\x9e', b'\xe0\xb9\x9f',
          b'\xe0\xb9\xa0',
          b'\xe0\xb9\xa1', b'\xe0\xb9\xa2', b'\xe0\xb9\xa3', b'\xe0\xb9\xa4', b'\xe0\xb9\xa5', b'\xe0\xb9\xa6',
          b'\xe0\xb9\xa7',
          b'\xe0\xb9\xa8', b'\xe0\xb9\xa9', b'\xe0\xb9\xaa', b'\xe0\xb9\xab', b'\xe0\xb9\xac', b'\xe0\xb9\xad',
          b'\xe0\xb9\xae',
          b'\xe0\xb9\xaf', b'\xe0\xb9\xb0', b'\xe0\xb9\xb1', b'\xe0\xb9\xb2', b'\xe0\xb9\xb3', b'\xe0\xb9\xb4',
          b'\xe0\xb9\xb5',
          b'\xe0\xb9\xb6', b'\xe0\xb9\xb7', b'\xe0\xb9\xb8', b'\xe0\xb9\xb9', b'\xe0\xb9\xba', b'\xe0\xb9\xbb',
          b'\xe0\xb9\xbc',
          b'\xe0\xb9\xbd', b'\xe0\xb9\xbe', b'\xe0\xb9\xbf'
          ]
    d5 = [b'\xe3\x84\x80', b'\xe3\x84\x81', b'\xe3\x84\x82', b'\xe3\x84\x83', b'\xe3\x84\x84', b'\xe3\x84\x85',
          b'\xe3\x84\x86', b'\xe3\x84\x87', b'\xe3\x84\x88', b'\xe3\x84\x89', b'\xe3\x84\x8a', b'\xe3\x84\x8b',
          b'\xe3\x84\x8c',
          b'\xe3\x84\x8d', b'\xe3\x84\x8e', b'\xe3\x84\x8f', b'\xe3\x84\x90', b'\xe3\x84\x91', b'\xe3\x84\x92',
          b'\xe3\x84\x93',
          b'\xe3\x84\x94', b'\xe3\x84\x95', b'\xe3\x84\x96', b'\xe3\x84\x97', b'\xe3\x84\x98', b'\xe3\x84\x99',
          b'\xe3\x84\x9a',
          b'\xe3\x84\x9b', b'\xe3\x84\x9c', b'\xe3\x84\x9d', b'\xe3\x84\x9e', b'\xe3\x84\x9f', b'\xe3\x84\xa0',
          b'\xe3\x84\xa1',
          b'\xe3\x84\xa2', b'\xe3\x84\xa3', b'\xe3\x84\xa4', b'\xe3\x84\xa5', b'\xe3\x84\xa6', b'\xe3\x84\xa7',
          b'\xe3\x84\xa8',
          b'\xe3\x84\xa9', b'\xe3\x84\xaa', b'\xe3\x84\xab', b'\xe3\x84\xac', b'\xe3\x84\xad', b'\xe3\x84\xae',
          b'\xe3\x84\xaf',
          b'\xe3\x84\xb0', b'\xe3\x84\xb1', b'\xe3\x84\xb2', b'\xe3\x84\xb3', b'\xe3\x84\xb4', b'\xe3\x84\xb5',
          b'\xe3\x84\xb6',
          b'\xe3\x84\xb7', b'\xe3\x84\xb8', b'\xe3\x84\xb9', b'\xe3\x84\xba', b'\xe3\x84\xbb', b'\xe3\x84\xbc',
          b'\xe3\x84\xbd',
          b'\xe3\x84\xbe', b'\xe3\x84\xbf', b'\xe3\x85\x80', b'\xe3\x85\x81', b'\xe3\x85\x82', b'\xe3\x85\x83',
          b'\xe3\x85\x84',
          b'\xe3\x85\x85', b'\xe3\x85\x86', b'\xe3\x85\x87', b'\xe3\x85\x88', b'\xe3\x85\x89', b'\xe3\x85\x8a',
          b'\xe3\x85\x8b',
          b'\xe3\x85\x8c', b'\xe3\x85\x8d', b'\xe3\x85\x8e', b'\xe3\x85\x8f', b'\xe3\x85\x90', b'\xe3\x85\x91',
          b'\xe3\x85\x92',
          b'\xe3\x85\x93', b'\xe3\x85\x94', b'\xe3\x85\x95', b'\xe3\x85\x96', b'\xe3\x85\x97', b'\xe3\x85\x98',
          b'\xe3\x85\x99',
          b'\xe3\x85\x9a', b'\xe3\x85\x9b', b'\xe3\x85\x9c', b'\xe3\x85\x9d', b'\xe3\x85\x9e', b'\xe3\x85\x9f',
          b'\xe3\x85\xa0',
          b'\xe3\x85\xa1', b'\xe3\x85\xa2', b'\xe3\x85\xa3', b'\xe3\x85\xa4', b'\xe3\x85\xa5', b'\xe3\x85\xa6',
          b'\xe3\x85\xa7',
          b'\xe3\x85\xa8', b'\xe3\x85\xa9', b'\xe3\x85\xaa', b'\xe3\x85\xab', b'\xe3\x85\xac', b'\xe3\x85\xad',
          b'\xe3\x85\xae',
          b'\xe3\x85\xaf', b'\xe3\x85\xb0', b'\xe3\x85\xb1', b'\xe3\x85\xb2', b'\xe3\x85\xb3', b'\xe3\x85\xb4',
          b'\xe3\x85\xb5',
          b'\xe3\x85\xb6', b'\xe3\x85\xb7', b'\xe3\x85\xb8', b'\xe3\x85\xb9', b'\xe3\x85\xba', b'\xe3\x85\xbb',
          b'\xe3\x85\xbc',
          b'\xe3\x85\xbd', b'\xe3\x85\xbe', b'\xe3\x85\xbf', b'\xe3\x86\x80', b'\xe3\x86\x81', b'\xe3\x86\x82',
          b'\xe3\x86\x83',
          b'\xe3\x86\x84', b'\xe3\x86\x85', b'\xe3\x86\x86', b'\xe3\x86\x87', b'\xe3\x86\x88', b'\xe3\x86\x89',
          b'\xe3\x86\x8a',
          b'\xe3\x86\x8b', b'\xe3\x86\x8c', b'\xe3\x86\x8d', b'\xe3\x86\x8e', b'\xe3\x86\x8f', b'\xe3\x86\x90',
          b'\xe3\x86\x91',
          b'\xe3\x86\x92', b'\xe3\x86\x93', b'\xe3\x86\x94', b'\xe3\x86\x95', b'\xe3\x86\x96', b'\xe3\x86\x97',
          b'\xe3\x86\x98',
          b'\xe3\x86\x99', b'\xe3\x86\x9a', b'\xe3\x86\x9b', b'\xe3\x86\x9c', b'\xe3\x86\x9d', b'\xe3\x86\x9e',
          b'\xe3\x86\x9f',
          b'\xe3\x86\xa0', b'\xe3\x86\xa1', b'\xe3\x86\xa2', b'\xe3\x86\xa3', b'\xe3\x86\xa4', b'\xe3\x86\xa5',
          b'\xe3\x86\xa6',
          b'\xe3\x86\xa7', b'\xe3\x86\xa8', b'\xe3\x86\xa9', b'\xe3\x86\xaa', b'\xe3\x86\xab', b'\xe3\x86\xac',
          b'\xe3\x86\xad',
          b'\xe3\x86\xae', b'\xe3\x86\xaf', b'\xe3\x86\xb0', b'\xe3\x86\xb1', b'\xe3\x86\xb2', b'\xe3\x86\xb3',
          b'\xe3\x86\xb4',
          b'\xe3\x86\xb5', b'\xe3\x86\xb6', b'\xe3\x86\xb7', b'\xe3\x86\xb8', b'\xe3\x86\xb9', b'\xe3\x86\xba',
          b'\xe3\x86\xbb',
          b'\xe3\x86\xbc', b'\xe3\x86\xbd', b'\xe3\x86\xbe', b'\xe3\x86\xbf', b'\xe3\x87\x80', b'\xe3\x87\x81',
          b'\xe3\x87\x82',
          b'\xe3\x87\x83', b'\xe3\x87\x84', b'\xe3\x87\x85', b'\xe3\x87\x86', b'\xe3\x87\x87', b'\xe3\x87\x88',
          b'\xe3\x87\x89',
          b'\xe3\x87\x8a', b'\xe3\x87\x8b', b'\xe3\x87\x8c', b'\xe3\x87\x8d', b'\xe3\x87\x8e', b'\xe3\x87\x8f',
          b'\xe3\x87\x90',
          b'\xe3\x87\x91', b'\xe3\x87\x92', b'\xe3\x87\x93', b'\xe3\x87\x94', b'\xe3\x87\x95', b'\xe3\x87\x96',
          b'\xe3\x87\x97',
          b'\xe3\x87\x98', b'\xe3\x87\x99', b'\xe3\x87\x9a', b'\xe3\x87\x9b', b'\xe3\x87\x9c', b'\xe3\x87\x9d',
          b'\xe3\x87\x9e',
          b'\xe3\x87\x9f', b'\xe3\x87\xa0', b'\xe3\x87\xa1', b'\xe3\x87\xa2', b'\xe3\x87\xa3', b'\xe3\x87\xa4',
          b'\xe3\x87\xa5',
          b'\xe3\x87\xa6', b'\xe3\x87\xa7', b'\xe3\x87\xa8', b'\xe3\x87\xa9', b'\xe3\x87\xaa', b'\xe3\x87\xab',
          b'\xe3\x87\xac',
          b'\xe3\x87\xad', b'\xe3\x87\xae', b'\xe3\x87\xaf', b'\xe3\x87\xb0', b'\xe3\x87\xb1', b'\xe3\x87\xb2',
          b'\xe3\x87\xb3',
          b'\xe3\x87\xb4', b'\xe3\x87\xb5', b'\xe3\x87\xb6', b'\xe3\x87\xb7', b'\xe3\x87\xb8', b'\xe3\x87\xb9',
          b'\xe3\x87\xba',
          b'\xe3\x87\xbb', b'\xe3\x87\xbc', b'\xe3\x87\xbd', b'\xe3\x87\xbe', b'\xe3\x87\xbf'
          ]
    d6 = [b'\xd8\x80', b'\xd8\x81', b'\xd8\x82', b'\xd8\x83', b'\xd8\x84', b'\xd8\x85',
          b'\xd8\x86', b'\xd8\x87', b'\xd8\x88', b'\xd8\x89', b'\xd8\x8a', b'\xd8\x8b', b'\xd8\x8c',
          b'\xd8\x8d', b'\xd8\x8e', b'\xd8\x8f', b'\xd8\x90', b'\xd8\x91', b'\xd8\x92', b'\xd8\x93',
          b'\xd8\x94', b'\xd8\x95', b'\xd8\x96', b'\xd8\x97', b'\xd8\x98', b'\xd8\x99', b'\xd8\x9a',
          b'\xd8\x9b', b'\xd8\x9c', b'\xd8\x9d', b'\xd8\x9e', b'\xd8\x9f', b'\xd8\xa0', b'\xd8\xa1',
          b'\xd8\xa2', b'\xd8\xa3', b'\xd8\xa4', b'\xd8\xa5', b'\xd8\xa6', b'\xd8\xa7', b'\xd8\xa8',
          b'\xd8\xa9', b'\xd8\xaa', b'\xd8\xab', b'\xd8\xac', b'\xd8\xad', b'\xd8\xae', b'\xd8\xaf',
          b'\xd8\xb0', b'\xd8\xb1', b'\xd8\xb2', b'\xd8\xb3', b'\xd8\xb4', b'\xd8\xb5', b'\xd8\xb6',
          b'\xd8\xb7', b'\xd8\xb8', b'\xd8\xb9', b'\xd8\xba', b'\xd8\xbb', b'\xd8\xbc', b'\xd8\xbd',
          b'\xd8\xbe', b'\xd8\xbf', b'\xd9\x80', b'\xd9\x81', b'\xd9\x82', b'\xd9\x83', b'\xd9\x84',
          b'\xd9\x85', b'\xd9\x86', b'\xd9\x87', b'\xd9\x88', b'\xd9\x89', b'\xd9\x8a', b'\xd9\x8b',
          b'\xd9\x8c', b'\xd9\x8d', b'\xd9\x8e', b'\xd9\x8f', b'\xd9\x90', b'\xd9\x91', b'\xd9\x92',
          b'\xd9\x93', b'\xd9\x94', b'\xd9\x95', b'\xd9\x96', b'\xd9\x97', b'\xd9\x98', b'\xd9\x99',
          b'\xd9\x9a', b'\xd9\x9b', b'\xd9\x9c', b'\xd9\x9d', b'\xd9\x9e', b'\xd9\x9f', b'\xd9\xa0',
          b'\xd9\xa1', b'\xd9\xa2', b'\xd9\xa3', b'\xd9\xa4', b'\xd9\xa5', b'\xd9\xa6', b'\xd9\xa7',
          b'\xd9\xa8', b'\xd9\xa9', b'\xd9\xaa', b'\xd9\xab', b'\xd9\xac', b'\xd9\xad', b'\xd9\xae',
          b'\xd9\xaf', b'\xd9\xb0', b'\xd9\xb1', b'\xd9\xb2', b'\xd9\xb3', b'\xd9\xb4', b'\xd9\xb5',
          b'\xd9\xb6', b'\xd9\xb7', b'\xd9\xb8', b'\xd9\xb9', b'\xd9\xba', b'\xd9\xbb', b'\xd9\xbc',
          b'\xd9\xbd', b'\xd9\xbe', b'\xd9\xbf', b'\xda\x80', b'\xda\x81', b'\xda\x82', b'\xda\x83',
          b'\xda\x84', b'\xda\x85', b'\xda\x86', b'\xda\x87', b'\xda\x88', b'\xda\x89', b'\xda\x8a',
          b'\xda\x8b', b'\xda\x8c', b'\xda\x8d', b'\xda\x8e', b'\xda\x8f', b'\xda\x90', b'\xda\x91',
          b'\xda\x92', b'\xda\x93', b'\xda\x94', b'\xda\x95', b'\xda\x96', b'\xda\x97', b'\xda\x98',
          b'\xda\x99', b'\xda\x9a', b'\xda\x9b', b'\xda\x9c', b'\xda\x9d', b'\xda\x9e', b'\xda\x9f',
          b'\xda\xa0', b'\xda\xa1', b'\xda\xa2', b'\xda\xa3', b'\xda\xa4', b'\xda\xa5', b'\xda\xa6',
          b'\xda\xa7', b'\xda\xa8', b'\xda\xa9', b'\xda\xaa', b'\xda\xab', b'\xda\xac', b'\xda\xad',
          b'\xda\xae', b'\xda\xaf', b'\xda\xb0', b'\xda\xb1', b'\xda\xb2', b'\xda\xb3', b'\xda\xb4',
          b'\xda\xb5', b'\xda\xb6', b'\xda\xb7', b'\xda\xb8', b'\xda\xb9', b'\xda\xba', b'\xda\xbb',
          b'\xda\xbc', b'\xda\xbd', b'\xda\xbe', b'\xda\xbf', b'\xdb\x80', b'\xdb\x81', b'\xdb\x82',
          b'\xdb\x83', b'\xdb\x84', b'\xdb\x85', b'\xdb\x86', b'\xdb\x87', b'\xdb\x88', b'\xdb\x89',
          b'\xdb\x8a', b'\xdb\x8b', b'\xdb\x8c', b'\xdb\x8d', b'\xdb\x8e', b'\xdb\x8f', b'\xdb\x90',
          b'\xdb\x91', b'\xdb\x92', b'\xdb\x93', b'\xdb\x94', b'\xdb\x95', b'\xdb\x96', b'\xdb\x97',
          b'\xdb\x98', b'\xdb\x99', b'\xdb\x9a', b'\xdb\x9b', b'\xdb\x9c', b'\xdb\x9d', b'\xdb\x9e',
          b'\xdb\x9f', b'\xdb\xa0', b'\xdb\xa1', b'\xdb\xa2', b'\xdb\xa3', b'\xdb\xa4', b'\xdb\xa5',
          b'\xdb\xa6', b'\xdb\xa7', b'\xdb\xa8', b'\xdb\xa9', b'\xdb\xaa', b'\xdb\xab', b'\xdb\xac',
          b'\xdb\xad', b'\xdb\xae', b'\xdb\xaf', b'\xdb\xb0', b'\xdb\xb1', b'\xdb\xb2', b'\xdb\xb3',
          b'\xdb\xb4', b'\xdb\xb5', b'\xdb\xb6', b'\xdb\xb7', b'\xdb\xb8', b'\xdb\xb9', b'\xdb\xba',
          b'\xdb\xbb', b'\xdb\xbc', b'\xdb\xbd', b'\xdb\xbe', b'\xdb\xbf'
          ]
    d = d1 + d2 + d3 + d4 + d5 + d6
    raw = s.encode()
    for item in d:
        raw = raw.replace(item, b'')
    return raw.decode()
    
def clean_main(s):
    s = str(s)
    s1 = remove_icon_facebook(s)
    s2 = convert_to_vietnamese_standard(s1)
    s4 = remove_other(s2)
    return s4
