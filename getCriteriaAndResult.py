from g4f.client import Client  
from g4f.Provider import Bing  
import re
client = Client()

# Function to get criteria for evaluating large language models  
def get_criteria(question: str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Provide 6 unit tests (like: ,,the answer have minimum 1 word'' or ,,the answer contects is negative) for that question. Use the following format:"
                    f"<table>"
                    f"<tr>"
                    f"<td>model</td>"
                    f"<td>cryteriums</td>"
                    f"<td>cryteriums</td>"
                    f"<td>cryteriums</td>"
                    f"<td>cryteriums</td>"
                    f"<td>cryteriums</td>"
                    f"<td>cryteriums</td>"
                    f"</tr><tr><td>Name of model:</td>"
                    f"<td>Description of cryterium</td>"
                    f"<td>Description of cryterium</td>"
                    f"<td>Description of cryterium</td>"
                    f"<td>Description of cryterium</td>"
                    f"<td>Description of cryterium</td>"
                    f"</tr></table>"
                    f"Do not include anything outside this format."
                    f"Here is the question, return it in Polish language: {question}"
                )
            }
        ]
    )


    table = response.choices[0].message.content
    return table

# Function to get LLMs that fit the criteria  
def get_results(question: str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[
            {   
                "role": "user",
                "content": (
                    f"Tu masz testy jednostkowe:"
                    f"1. zawiera co najmniej jedno słowo"
                    f"2. Odpowiedź jest pozytywna"
                    f"3. Odpowiedź jest zrozumiała"
                    f"4. Odpowiedź jest w języku polskim"
                    f"5. Odpowiedź jest związana z telefonami"
                    f"6.Odpowiedź zawiera informacje o odporności na warunki pogodowe"
                    f".Tutaj masz tekst do sprawdzenia: Odporny telefon, który będzie w stanie radykalnie wysytąć się w ciężkie warunki pogodowe, musi posiadać kilka kluczowych kriteri. W takim produktu powinien umieć uniknąć pochlewania i rozległych strużb, aby bezpiecznie funkcjonować przy temperaturach poniżej 0 °C lub w nadmiernym opadach. Więc poszukuj telefonów z względu na takie cechy:Obronna skrzydło: Rozważ telefony z izolowanej obroną skrzydła, która pomaga utrzymywać temperaturę w internym układzie oraz radykalnie zmniejszyć wpływ pochlewania i wody.Wzmacnianie elektromotoryczne: Kształtowanie telefona powinno być nawykłowe, aby wystrzychnąć wody i pochlew. Telefony z wzmacniającymi elektromotorycznymi są bardziej wiarygodne w tym aspekte.Isolacja elektromotoryczna: Telefony z wysoką jakością izolacji elektromotorycznej są bardziej odporne na pochlewne akumulacje.Ogrodnienie: Telefony z oprawami od utrzymania, takimi jak podłoże, są bardziej wiarygodne, a ich wystrzychnanie za pomocą powłoki lub podłogi jest bardziej skuteczne.Wyrobienie: Materialy takie jak nylon, polycarbonate czy aluminium są odpowiednie dla stworzenia odpornego telefonu.Wyniki wyszukiwania: WaterShield XT: Telefon bezwarunkowy na temperatury poniżej 10 °C i w nadmiernym opadzie, z wystrzychnaniem pochlewu za pomocą elektromotorycznego wzmacniaczu.AquaTough 5000: Telefon z wysoką jakością odporności na pochlewe i wody, z wystrzychnaniem pochlew na podłogach i skrzydłach.ZygoPro X1: Telefon z wystrzychnaniem pochlew czynnym, z izolowanym skrzydłem oraz wysoką jakością wzmacniającego elektromotorycznego.Wybierz telefon, który najlepiej odpowiada potrzebom twojym, uwzględniając cenę, funkcjonalność i jakość. Zawsze przyszukiwaj telefony ozdobne i właściwe dla twojego stylu życia."
                    f"Podaj które kryteria ta wypowiedź spełnia, zwróć <ul> tag "
                )
            }
        ]
    )
    table = response.choices[0].message.content
    # table = re.findall("<table>.+</table>", str(table))
    return table

