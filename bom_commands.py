import requests

static_site_dict = {'adelaide':'IDS60901/IDS60901.94648',
                    'melbourne':'IDV60901/IDV60901.95936',
                    'sydney':'IDN60901/IDN60901.94768',
                    'canberra':'IDN60903/IDN60903.94926'}

data_type_dict = {'dew_point':'dewpt',
                  'temp':'air_temp',
                  'apparent': 'apparent_t',
                  'rain': 'rain_trace'}

def pull_info_for_site(location: str,
                       data: str) -> float:
    assert location.lower() in static_site_dict.keys(), f"Need location in {static_site_dict.keys()}"

    r = requests.get(url=f'http://www.bom.gov.au/fwo/{static_site_dict[location.lower()]}.json',
                     headers={'User-agent': 'Mozilla/5.0'})
    up_to_date_data = r.json()['observations']['data'][0]
    assert data.lower() in data_type_dict.keys(), f"Need data in {data_type_dict.keys()}"
    return float(up_to_date_data[data_type_dict[data]])


if __name__ == '__main__':

   print(pull_info_for_site('canberra','rain'))

