import requests


def namoz(city):
    URL = f'https://islomapi.uz/api/present/day?region={city}'

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        city = data['region']
        date = data['date']
        hafta_kuni = data['weekday']
        bomdod = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom = data['times']['shom_iftor']
        xufton = data['times']['hufton']
        return f"🏘Shahar: <b>{city}</b>\n\n📅Sana: <b>{date}</b>\n🗓Hafta kuni: <b>{hafta_kuni}</b>\n\n🌄Bomdod: <b>{bomdod}</b>\n🌤Quyosh: <b>{quyosh}</b>\n🏞Peshin: <b>{peshin}</b>\n🌇Asr: <b>{asr}</b>\n🌆Shom: <b>{shom}</b>\n🌃Xufton: <b>{xufton}</b>"
    else:
        return f"Error: {response.status_code}"
    
# print(namoz('Toshkent'))