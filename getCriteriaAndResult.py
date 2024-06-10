from g4f.client import Client  
from g4f.Provider import Bing  
from bs4 import BeautifulSoup

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
                    f"Provide 4-7 criteria for evaluating Large Language Models. Use the following format:\n\n"
                    f"<table class='border'>"
                    f"<tr class='border'>"
                    f"<td class='border'>cryteriums</td>"
                    f"<td class='border'>cryteriums</td>"
                    f"<td class='border'>cryteriums</td>"
                    f"<td class='border'>cryteriums</td>"
                    f"</tr><tr><td class='border'>Description of cryterium</td>"
                    f"<td class='border'>Description of cryterium</td>"
                    f"<td class='border'>Description of cryterium</td>"
                    f"<td class='border'>Description of cryterium</td>"
                    f"</tr></table>"
                    f"Do not include anything outside this format."
                    f"Here is the question, return it in Polish language: {question}"
                )
            }
        ]
    )


    soup = BeautifulSoup(response.choices[0].message.content, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name not in ['table', 'tr', 'td']:
            tag.decompose()
    return str(soup)

# Function to get language models that fit the criteria  
def get_results(question: str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        provider=Bing,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Provide 6-8 LLMS (like chatgpt or gemini) that best meet these criteria. give me html table format with criterias and that models.\n\n"
                    f"{question}"
                )
            }
        ]
    )
    soup = BeautifulSoup(response.choices[0].message.content, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name not in ['table', 'tr', 'td']:
            tag.decompose()
    return str(soup)
