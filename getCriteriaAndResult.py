from g4f.client import Client

client = Client(

) 
#występuje błąd async, jednak zwraca odpowiedź
def getCriteria(question):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": ('Podaj kryteria dla Large Languages Models, aby móc ocenić ich dobre i złe strony wyboru danego modelu, dla pytania:'+question)}]
    )
    return response.choices[0].message.content


print (getCriteria("Szukam telefonu z dużym ekranem i mocną baterią."))