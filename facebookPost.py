import requests

# page_id = '203802286158322'
page_id = 'page_id'
access_token = 'access_token'

post_url = f'https://graph.facebook.com/{page_id}/photos'

post_text = (
    '🏡 вул. Зелена, 115ж\n'
    '🚪 Кількість кімнат: 2\n'
    '💰 Ціна: 395USD\n'
    '📝 Опис: Здається квартира в новобудові 2 кімнати, кімнати ізольовані, вся побутова техніка, кондиціонер, автономне опалення'
)

post_payload = {
    'message': post_text,
    'access_token': access_token
}   

photo_paths = [
    'images/photo1.jpg',
    'images/photo2.jpg',
]

photo_files = [('source', (f'photo{i}.jpg', open(photo_path, 'rb'))) for i, photo_path in enumerate(photo_paths)]
files = dict(photo_files)

r = requests.post(post_url, data=post_payload, files=files)

print(r.text)