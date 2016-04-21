import falcon
import psycopg2
import SQL
from wsgiref import simple_server

class RequestHandler:
    def on_get(self, req, resp):
        try:
            print("ON_GET")
            resp.body = SQL.query(req.path, req.stream)  # How will this be represented
            resp.status = falcon.HTTP_200
        except psycopg2:
            resp.status = falcon.HTTP_400
        except falcon:
            resp.status = falcon.HTTP_501

        # May be use for a 404 Here.

    def on_post(self, req, resp):
        try:
            print("ON_POST")
            SQL.enter(req.path, req.stream)
            resp.status = falcon.HTTP_200
        except psycopg2:
            resp.status = falcon.HTTP_400
        except falcon:
            resp.status = falcon.HTTP_501

app = falcon.API()

requestHandler = RequestHandler()

app.add_route("/", requestHandler)
app.add_route("/VehicleTrack", requestHandler)

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()
