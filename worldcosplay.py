# coding=utf-8
from sys import argv
import requests

member_id = argv[1]

url = 'http://worldcosplay.net/en/api/member/photos?member_id=%s&page=1&limit=100000&rows=16&p3_photo_list=1' % member_id

r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    if data['has_error'] != 0:
        print u'接口挫了'
        exit(1)

    photo_data_list = data['list']
    index = 0
    for photo_data in photo_data_list:
        url = photo_data['photo']['sq300_url']
        subject = photo_data['photo']['subject']
        url = url.replace('/sq300', '')
        filename = '%s_%s_%s.jpg' % (member_id, index, subject)

        with open(filename, 'wb') as handle:
            response = requests.get(url, stream=True)

            if not response.ok:
                # Something went wrong
                print u'这个图片没有下来：%s' % url
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
            print u'下完了%s张' % (index + 1)
        index += 1

else:
    print u'挫了'