import urllib.request

def url_ok(url):
    try:
        response = urllib.request.urlopen(url)
        print("Consegui acessar o site com sucesso!")
    except urllib.error.URLError:
        print("Não foi possível acessar o site.")

url_ok('http://pudim.com.br/')
