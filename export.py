from etherpad_lite import EtherpadLiteClient
import os
import requests
import click
import ftfy

URL = 'http://yourserver:yourport'
APIKEY = 'inser your key here'

client = EtherpadLiteClient(base_url=URL + '/api',
                            base_params={'apikey': APIKEY},
                            api_version='1.2.9')

os.makedirs('exported_pads', exist_ok=True)

pad_list = client.listAllPads()['padIDs']
with click.progressbar(pad_list) as progress_bar:
    for pad_name in progress_bar:
        with open('exported_pads' + os.sep + pad_name + '.txt', 'w') as file:
            pad_content = ftfy.fix_text(requests.get(URL + '/p/' + pad_name + '/export/txt').text)
            file.write(pad_content)
