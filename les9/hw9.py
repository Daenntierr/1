import requests

response = requests.get('https://bank.gov.ua/ua/markets/currency-market')
response_text = response.text

usd_list = []

response_parse = response_text.split('<')

for parse in response_parse:
    if '$' in parse:
        if 'USD' in parse:
            parts = parse.split('USD')
            if len(parts) > 1:
                rate_part = parts[1]
                rate = rate_part.split('<')[0]
                usd_list.append(rate.strip())

if usd_list:
    for rate in usd_list:
        print(f"Знайдений курс: {rate}")
else:
    print("Не вдалося знайти курс долара.")