import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www)?.[a-zA-Z]+.[a-zA-Z]+')
match = pattern.finditer(urls)
print(list(match))