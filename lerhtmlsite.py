import requests
from bs4 import BeautifulSoup
import pandas as pd

# Baixamos a página que contém as previsões do tempo;
# Criamos uma classe BeautifulSoup para analisar a página;
# Encontramos a div com id seven-day-forecast, e atribuímos para seven_day;
# Dentro de seven_day, encontramos cada item de previsão do tempo individual;
# Extraímos e exibimos o primeiro item da previsão;

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

# ----------------------------------------------------------------------------------------------------

# Como vocês podem ver, dentro de item tonight está toda a informação que queremos. Existem quatro partes de informação que podemos extrair:

# O nome do item – nesse caso, tonight;
# A descrição das condições: estão salvas na propriedade title de img;
# Uma descrição curta das condições – nesse caso, Mostly Clear;
# A temperatura mínima – nesse caso, 49 graus.

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

# ----------------------------------------------------------------------------------------------------

# Agora podemos extrair o atributo title da tag img. Para isso, 
# basta tratar o objeto BeautifulSoup como um dicionário e passar o atributo que 
# queremos como chave:

img = tonight.find("img")
desc = img['title']

# print(desc)

# ----------------------------------------------------------------------------------------------------
# Selecionamos todos os itens com a classe period-name dentro da classe tombstone-container 
# em seven_day.
# Utilizamos uma lista de compreensão para chamar o método get_text para cada objeto BeautifulSoup.

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(range(len(periods)))
print(len(periods))
# print(periods)
# print(short_descs)
# print(temps)
# print(len(descs))

# ----------------------------------------------------------------------------------------------------
# Agora, nós podemos combinar os dados em um DataFrama do Pandas e analisá-los. Um DataFrame é 
# um objeto que pode armazenar dados tabulados, realizando analises facilmente.

weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })
# print(weather)

# ----------------------------------------------------------------------------------------------------
# Agora podemos fazer algumas analises dos dados. Por exemplo, podemos utilizar uma expressão regular e 
# o método Series.str.extract para extrair os valores numéricos das temperaturas.

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

# ----------------------------------------------------------------------------------------------------
# Nós podemos encontrar a média das temperaturas:

print(weather["temp_num"].mean())

# ----------------------------------------------------------------------------------------------------
# Nós podemos também selecionar somente as colunas que ocorrem à noite:

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
# print(is_night)

print(weather[is_night])