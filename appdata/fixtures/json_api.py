import requests
import json

from appdata.models import StateCasesModel, CountryModel


def get_json_data():
    url = 'https://coronavirus.app/get-places'
    headers = {
        "authority": "coronavirus.app",
        "sec-fetch-dest": "empty",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "x-date-req": "2020-03-30T05:41:27.387Z",
        "x-pqww": "gWXQwNeAAgObugSYiiho",
        "content-type": "application/json",
        "accept": "*/*",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "referer": "https://coronavirus.app/map",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cookie": "cookiesaccepted=accepted; _ga=GA1.2.1525784884.1585381088; darkmode=off; logarithmic_charts=off; __stripe_mid=730a8c6c-5582-488b-966d-f9f2099b0e3e; _gid=GA1.2.1156321064.1585546011; __session=eyJ0b2tlbiI6IjliMWFjZWE2OWM4N2I4NDdiMzJkM2RkZTJjMTY5YzVjODI3Zjk4NzlkYmQxOWU0YzM1MGM0YjM0ZTVhY2FkNTE1M2YwMGE5NTBlN2VjYTI0NjFiOGE0NjY0MDA5NDA2OEQ0RzI0c3Q2UDFUQjJLdk5Pbm9KUFAyaWpTS3JJTWd4SDVsSDRkeWZKVlJoR2hnTGdOeTNJRTM5aWt6QXVCbkdpYW9xQkZVaWxuTGFnbmpVWVc1YXE1WGRGckg5dEdXSlBvdkJVR0N6V2FOY2Vqd0ErQWlPbmlBdFNEWU1WV2dGSmZHSmQ2VDVyRkplSnRQUmRneEYyekczSUUxdG02NXdHSGd4WGVyOElJU0RHcmpZS01wdENzWWEyc05EU25PRFAzeElTVHpJRE8yTFF1dFE3WnNDUlRCMFRFdldJV3JITG1uYXNMZ0pBR1lzcFo1aW9UL2UzQVk3K0JCVE9HSEJ1dUlZQUhTOGdhM0I1b2VLTyttQmhqczI1T2swN2x2YmI4aUkyOGs4WnpDVHF0U1JqSjk4S05jOHpucnF2Zm1XT3dLM0ppamVMaG0xSU9yRHU5R2hOc1RGUVF1bGR2RG9RSm40TlZjK3l0TURMbGxTQWMwZjVHUEF4VnZDYTU5UDV2b3hTV3dIUnhuc0lycDRUSUlyYjJ4ZG1QWVM2S1NOMWNtdjZnNFJzdWtveHVtZ0o4c3FUWllHajJ4ZVNhNG01WlgvcXlXVVpFV2poaDNRUmhlVFloSVpqUmY0Ym0zbVd2WkZIU3ZnNTNGbFlFVXpRUlVhcENjQ293Y3FWWGh5QUtLTnFsTDZFU0hHUFdxbExjZ1g2OW12dkUzN3ZjcHY5Sml0bzBBTElhOD0ifQ==; _gat_gtag_UA_156994128_2=1",
        "if-none-match": 'W/"13005-vaHL+0hApbsNowedg8C8KN254l0"'
    }
    r = requests.get(url, headers=headers)
    print(r.json())
    f = open("updated_data.json", "w")
    f.write(json.dumps(r.json(), indent=2))
    f.close()

# from appdata.fixtures.json_api import get_json_data


def data_insertion_or_update_in_database():
    with open('updated_data.json', 'r') as States:
        states_data = json.load(States)
        # country_code = []
        for each_state in states_data['data']:
            try:
                print("In Data Values Update")
                state_obj = StateCasesModel.objects.get(name=each_state['name'])
                state_obj.total_cases = each_state['infected']
                state_obj.total_deaths = each_state['dead']
                state_obj.total_recovers = each_state['recovered']
                state_obj.save()
            except StateCasesModel.DoesNotExist:
                print("In Data Values Create")
                print(CountryModel.objects.get(code=each_state['country']))
                # print(each_state.keys())
                if 'pop' in each_state.keys():
                    population = each_state['pop']
                else:
                    population = "not confirmed"
                state_obj = StateCasesModel(
                    name=each_state['name'],
                    country=CountryModel.objects.get(code=each_state['country']),
                    total_cases=each_state['infected'],
                    total_deaths=each_state['dead'],
                    total_recovers=each_state['recovered'],
                    latitude=each_state['latitude'],
                    longitude=each_state['longitude'],
                    population=population,
                    sick=each_state['sick']
                )
                # country_code.append(each_state['country'])
                state_obj.save()
                # print(len(list(dict.fromkeys(country_code))))


# from appdata.fixtures.json_api import data_insertion_or_update_in_database
