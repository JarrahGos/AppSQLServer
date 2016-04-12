import falcon
import mysql
from src.Server import SQL


class RequestHandler:
    def on_get(self, req, resp):
        try:
            resp.body = SQL.query(req.get_param("")) # How will this be represented
            resp.status = falcon.HTTP_200
        except mysql:
            resp.status = falcon.HTTP_400
        # May be use for a 404 Here.

    def on_post(self, req, resp):
        try:
            SQL.enter(req.get_param(""))
            resp.status = falcon.HTTP_200
        except mysql:
            resp.status = falcon.HTTP_400

app = falcon.API()

requestHandler = RequestHandler()

app.add_route("/", requestHandler)
