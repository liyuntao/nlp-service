import falcon

from resource.tag_cloud_resource import TagCloudResource
from resource.static_resource import StaticResource


class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('awesome')


app = falcon.API()

welcome = MainResource()

app.add_route('/', welcome)
app.add_route('/static/{filename}', StaticResource())
app.add_route('/tagcloud', TagCloudResource('images'))

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('0.0.0.0', 8080, app)
    httpd.serve_forever()
