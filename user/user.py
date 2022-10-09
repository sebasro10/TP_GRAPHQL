from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
from google.protobuf.json_format import MessageToDict

import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

def existsUser(userId):
   for user in users:
        if str(user["id"]) == str(userId): return True
   return False

def getBookingsByUserID(userId):
   with grpc.insecure_channel('booking_graphql:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      bookingsByUserID = MessageToDict(stub.GetBookingsByUserID(booking_pb2.UserID(userid=userId)))
   channel.close()
   return bookingsByUserID

def createBooking(newBooking):
   with grpc.insecure_channel('booking_graphql:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      bookingsByUserID = MessageToDict(stub.CreateBooking(newBooking))
   channel.close()
   return bookingsByUserID

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/bookings/<nameorid>", methods=['GET'])
def get_bookings_bynameorid(nameorid):
   for user in users:
        if str(user["name"]) == str(nameorid) or str(user["id"]) == str(nameorid):
            return make_response(jsonify(getBookingsByUserID(user["id"])),200)
   return make_response(jsonify({"error":"user not found"}),400)

@app.route("/bookings/<userid>", methods=['POST'])
def create_booking(userid):
   req = request.get_json()
   if existsUser(userid):
      return make_response(jsonify(createBooking(booking_pb2.BookingDataToCreate(userid=userid,date=req["date"],movieid=req["movieid"]))),200)
   return make_response(jsonify({"error":"user not found"}),400)

@app.route("/movies/<userid>", methods=['GET'])
def get_info_movies(userid):
   if existsUser(userid):
      bookings = getBookingsByUserID(userid)
      for date in bookings["dates"]:
         movies= []
         for movieid in date["movies"]:
            query = "query{" + f'movie_with_id(_id:"{movieid}")' + """ {
                           id
                           title
                           rating
                           director
                        }
                     }"""
            movies.append(requests.post('http://movie_graphql:3001/graphql', json={'query':query}).json()["data"]["movie_with_id"])
         date["movies"] = movies

      return make_response(jsonify(bookings),200)
   return make_response(jsonify({"error":"user not found"}),400)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
