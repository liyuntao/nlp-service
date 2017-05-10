import falcon
import json

from collections import Counter
from wordcloud import WordCloud
import uuid
import logging
import jieba


def generateTagCloud(texts=[]):
    logging.info('received contents from bot...')
    frequencies = Counter([w for text in texts for w in jieba.cut(text, cut_all=False) if len(w) > 1])
    frequencies = {k: min(40, frequencies[k]) for k in frequencies}

    wc = WordCloud(font_path='./font/STHeiti-Light.ttc', width=400, height=400, max_words=100)
    img = wc.generate_from_frequencies(frequencies).to_image()

    logging.info('ready to generate tag-cloud-img...')
    random_image_name = '{uuid}.{ext}'.format(uuid=uuid.uuid4(), ext='png')
    img.save(random_image_name)

    return random_image_name


class TagCloudResource(object):
    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, storage_path):
        self._storage_path = storage_path

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            texts = result['contents']

            file_name = generateTagCloud(texts)

            resp.body = json.dumps({'img_url': file_name})
        except ValueError as ex:
            logging.error(ex)
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The JSON was incorrect.')
