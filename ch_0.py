# Challenge 0
import urllib.request as request
from collections import defaultdict
from html.parser import HTMLParser

url = f'http://www.pythonchallenge.com/pc/def/{2**38}.html'
print(url)

# Challenge 1
cryptic_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

deciphered_text = ''.join([chr((ord(c) - 95) % 26 + 97) if c.isalpha() else c for c in cryptic_text])
print(deciphered_text)
trantab = str.maketrans(''.join([chr(x) for x in range(97, 123)]),
                        ''.join([chr((x - 95) % 26 + 97) for x in range(97, 123)]))
print(cryptic_text.translate(trantab))
next_page = 'map'.translate(trantab)
print(f'http://www.pythonchallenge.com/pc/def/{next_page}.html')


# Challenge 2
class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_comment(self, data):
        char_count = defaultdict(int)
        print(data)
        for char in data:
            char_count[char] += 1
            if char.isalpha():
                print(char)
        print(sorted(char_count.items()))


page = request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
page_bytes = page.read()
page_string = page_bytes.decode('utf8')
page.close()

parser = MyHTMLParser()
parser.feed(page_string)

# Challenge 3
# Get the comment and get each small case letter that's flanked by 3 upper case letters
