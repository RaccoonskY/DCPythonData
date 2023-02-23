import datetime
import requests

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
VK_API_VERSION = 5.81


def get_user_id(uid):
    if isinstance(uid, int):
        return uid

    user_payload = {'v': VK_API_VERSION,
                    'access_token': ACCESS_TOKEN,
                    'user_ids': uid}
    user_get = requests.get('https://api.vk.com/method/users.get', params=user_payload)
    user_id = dict(user_get.json())['response'][0]['id']

    return user_id


def get_friends(user_id):
    friends_payload = {'v': VK_API_VERSION,
                       'access_token': ACCESS_TOKEN,
                       'user_id': user_id,
                       'fields': 'bdate'}
    friends_get = requests.get('https://api.vk.com/method/friends.get', params=friends_payload)
    friends = dict(friends_get.json())['response']['items']

    return friends


def get_pairs(users):
    current_year = datetime.datetime.now().year

    ages = []
    for user in users:
        if 'bdate' in user and len(user['bdate'].split('.')) == 3:
            birth_year = datetime.datetime.strptime(user['bdate'], "%d.%m.%Y").year
            age = current_year - birth_year
            ages.append(age)

    pairs = count_ages(ages)
    return pairs


def count_ages(ages):
    pairs = []
    unique_ages = set(ages)
    for age in unique_ages:
        person_count = ages.count(age)
        pairs.append((age, person_count))

    return pairs


def sort_pairs(pairs):
    sorted_by_age = sorted(pairs, key=lambda item: item[0])
    sorted_by_count = sorted(sorted_by_age, key=lambda item: item[1], reverse=True)
    return sorted_by_count


def calc_age(uid):
    user_id = get_user_id(uid)
    friends = get_friends(user_id)
    pairs = get_pairs(friends)
    sorted_pairs = sort_pairs(pairs)

    return sorted_pairs


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
