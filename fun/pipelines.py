# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from fun import settings
import os


class FunPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            index = 0
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            for image_url in item['image_urls']:
                l = image_url.split('/')
                image_file_name = l[len(l) - 1]
                file_path = '%s/%s_%s' % (dir_path, index, image_file_name)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)
                index += 1
            item['images'] = images
        return item
