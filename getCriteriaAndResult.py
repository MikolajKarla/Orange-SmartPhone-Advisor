from g4f.client import Client
from g4f.Provider import Bing

client = Client(
) 
#występuje błąd async, jednak zwraca odpowiedź

def getCriteria(question):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[{"role": "user", "content": ('Podaj 4-7 kryteriów dla Large Languages Models, aby móc ocenić ich dobre i złe strony wyboru danego modelu językowego. Podaj według formatu: <table class="border"><tr class="border"><td class="border"><strong> kryterium 1:</strong></td><td  class="border"><strong>kryterium 2:</strong></td><td class="border"><strong> kryterium 3:</strong></td><td  class="border"><strong>kryterium 4:</strong></td></tr><tr><td class="border">opis kryterium</td><td class="border">opis kryterium</td><td class="border">opis kryterium</td><td class="border">opis kryterium</td></tr></table>.Będzie on udostępniony na stronie, nie pisz nic poza tą tabelą.Oto pytanie:'+question)}]
    )
    getResults(response.choices[0].message.content)
    return response.choices[0].message.content
    


def getResults(question):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[{"role": "user", "content": ('Podaj 4-8 modeli językowych, które będa spełniać te kryteria najlepiej i wypisz je w następnych kolumnach:'+question)}]
    )
    print( response.choices[0].message.content)


print (getCriteria("Szukam telefonu z dużym ekranem i mocną baterią."))