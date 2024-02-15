import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

app_id = 'app_id'
app_secret = 'app_secret'
access_token = 'access_token'
page_id = 'page_id'

# Authenticate and get a long-lived user access token
def get_long_lived_token():
    url = f'https://graph.facebook.com/v12.0/oauth/access_token?' \
          f'grant_type=fb_exchange_token&' \
          f'client_id={app_id}&' \
          f'client_secret={app_secret}&' \
          f'fb_exchange_token={access_token}'

    response = requests.get(url)
    data = response.json()
    return data.get('access_token')

long_lived_token = get_long_lived_token()

additional_text = (
    '🏡 вул. Зелена, 115ж\n'
    '🚪 Кількість кімнат: 2\n'
    '💰 Ціна: 395USD\n'
    '📝 Опис: Здається квартира в новобудові 2 кімнати, кімнати ізольовані, вся побутова техніка, кондиціонер, автономне опалення'
)

photo_paths = [
    'images/photo1.jpg',
    'images/photo2.jpg',
    'images/photo3.jpg',
    'images/photo4.jpg',
]

def create_facebook_post(token, text, photo_paths):
    url = f'https://graph.facebook.com/v12.0/{page_id}/photos'
    params = {'access_token': token}

    files = [('file{}'.format(i), ('photo{}.jpg'.format(i), open(photo_path, 'rb'), 'image/jpeg')) for i, photo_path in enumerate(photo_paths, start=1)]

    data = {
        'message': text,
        'published': 'true',
        'no_story': 'false',
    }

    fields = {}
    for key, value in data.items():
        fields[key] = (None, value)

    for key, (filename, file, content_type) in files:
        fields[key] = (filename, file, content_type)

    encoder = MultipartEncoder(fields=fields)
    headers = {'Content-Type': encoder.content_type}

    response = requests.post(url, params=params, data=encoder, headers=headers)

    if response.status_code == 200:
        print('Пост успішно створено!')
    else:
        print(f'Помилка: {response.status_code}, {response.text}')

create_facebook_post(long_lived_token, additional_text, photo_paths)