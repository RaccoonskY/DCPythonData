import collections
import json
import datetime

import requests

def calc_age(uid):
    current_year = datetime.datetime.now().year
    access_token = '92b0d2e792b0d2e792b0d2e75791a21b74992b092b0d2e7f146e8e7090b813dfa76951c'
    parameters = {'user_ids': uid}
    id_js_req = requests.request('GET', url=("https://api.vk.com/method/users.get?v=5.81&access_token="+access_token),params=parameters).json()
    id = dict(id_js_req)['response'][0]['id']
    parameters = {'user_id': id, 'fields': 'bdate'}
    friends = requests.request('GET', url=('https://api.vk.com/method/friends.get?v=5.81&access_token='+access_token), params=parameters)
    age_list = []

    for i in friends.json()['response']['items']:
        if i.get('bdate') != None:
            if len(i['bdate']) > 5:
                year = current_year - int(i['bdate'][len(i['bdate'])-4:])
                contained = False
                for j in age_list:
                    if j.__contains__(year):
                        j[1] +=1
                        contained = True
                    if contained:
                        break
                if not contained:
                    age_list.append([year,1])

    age_list.sort(key=lambda x: x[0])
    age_list.sort(key=lambda x:x[1],reverse=True)

    age_list = [(i[0],i[1]) for i in age_list]
    return age_list



if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)