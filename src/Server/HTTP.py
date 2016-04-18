import falcon
import psycopg2
import SQL

class RequestHandler:
    def on_get(self, req, resp):
        try:
            print("ON_GET")
            resp.body = SQL.query(req.get_param("URL", "BODY"))  # How will this be represented
            resp.status = falcon.HTTP_200
        except psycopg2:
            resp.status = falcon.HTTP_400
        except falcon:
            resp.status = falcon.HTTP_501

        # May be use for a 404 Here.

    def on_post(self, req, resp):
        try:
            print("ON_POST")
            SQL.enter(req.get_param("URL", "BODY"))
            resp.status = falcon.HTTP_200
        except psycopg2:
            resp.status = falcon.HTTP_400
        except falcon:
            resp.status = falcon.HTTP_501

app = falcon.API()

requestHandler = RequestHandler()

app.add_route("/", requestHandler)
app.add_route("/VehicleTrack", requestHandler)
