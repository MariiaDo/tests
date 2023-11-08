import json

import requests

url = "https://swapi.dev/api/starships"


if __name__ == '__main__':
    response = requests.request("GET", url)
    data = response.json()['results']
    falcon_info = {}
    for i in data:
        if i['name'] == "Millennium Falcon":
            falcon_info.update(i)
    falcon_common_info = {
        "name": falcon_info['name'],
        "max_atmosphering_speed": falcon_info['max_atmosphering_speed'],
        "starship_class": falcon_info['starship_class']
    }
    pilot_urls = falcon_info['pilots']
    pilots = []
    for _url in pilot_urls:
        pilot_resp = requests.get(_url)
        pilot_result = pilot_resp.json()
        url_planet = pilot_result['homeworld']
        native_pilots_planet_response = requests.get(url_planet).json()
        native_pilots_planet = native_pilots_planet_response["name"]
        pilot_result_itog = {
            "name": pilot_result['name'],
            "height": pilot_result['height'],
            "mass": pilot_result['mass'],
            "native pilots planet": native_pilots_planet,
            "homeworld": pilot_result['homeworld']
        }

        pilots.append(pilot_result_itog)
    falcon_common_info.update({"pilots": pilots})
    result_json = json.dumps(falcon_common_info)
    with open('Millennium_falcon.json', 'w') as f:
        f.write(result_json)



