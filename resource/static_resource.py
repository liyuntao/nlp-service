import falcon


class StaticResource(object):
    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200
        resp.content_type = 'appropriate/content-type'
        with open(filename, 'rb') as f:
            resp.body = f.read()
