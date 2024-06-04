from g4f.client import Client
from g4f.Provider import Bing
from bs4 import BeautifulSoup


client = Client(
) 
#występuje błąd async, jednak zwraca odpowiedź

def getCriteria(question:str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[{"role": "user", "content": ('Podaj 4-7 kryteriów dla Large Languages Models, aby móc ocenić ich dobre i złe strony wyboru danego modelu językowego. Podaj według formatu: <table class="border"><tr class="border"><td class="border"><strong> kryterium 1:</strong></td><td  class="border"><strong>kryterium 2:</strong></td><td class="border"><strong> kryterium 3:</strong></td><td  class="border"><strong>kryterium 4:</strong></td></tr><tr><td class="border">opis kryterium</td><td class="border">opis kryterium</td><td class="border">opis kryterium</td><td class="border">opis kryterium</td></tr></table>.Będzie on udostępniony na stronie, nie pisz nic poza tą tabelą.Oto pytanie:'+question)}]
    )
    # getResults(response.choices[0].message.content)
    soup = BeautifulSoup(response.choices[0].message.content, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name != 'table' and tag.name != 'tr' and tag.name != 'td':
            tag.decompose()
    # for tag in soup.find_all('td'):
    #     tag.decompose()
    print(soup)
    soup = str(soup)
    return soup
    

#nie dziala jeszcze
# def getResults(question:str):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",
#         provider=Bing,
#         messages=[{"role": "user", "content": ('Podaj 4-8 modeli językowych, które będa spełniać te kryteria najlepiej i wypisz je w następnych kolumnach:'+question)}]
#     )
#     print( response.choices[0].message.content)

