import falcon
import psycopg2

class RequestHandler:
    def on_get(self, req, resp):
        try:
	    print("ON_GET")
            resp.body = SQL.query(req.get_param("URL", "BODY"))  # How will this be represented
            resp.status = falcon.HTTP_200
        except mysql:
            resp.status = falcon.HTTP_400
        # May be use for a 404 Here.

    def on_post(self, req, resp):
        try:
	    print("ON_POST")
            SQL.enter(req.get_param("URL", "BODY"))
            resp.status = falcon.HTTP_200
        except mysql:
            resp.status = falcon.HTTP_400

app = falcon.API()

requestHandler = RequestHandler()

app.add_route("/", requestHandler)
app.add_route("/VehicleTrack", requestHandler)
