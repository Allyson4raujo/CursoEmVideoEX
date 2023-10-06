import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://onepieceex.net/')
except:
    print('Não consegui reconhecer')
else:
    print('TUdo ok')

