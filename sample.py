from flask import Blueprint, request,Response
import json
from bson import json_util


routes = Blueprint('ussd_routes', __name__)

# handle ussd request
@routes.route('/ussd',methods=['POST'])
def handle_ussd_requests():
    post_dict = request.get_json()
    # print(" ==>> request" + str(post_dict))
    result = handler(post_dict)    
    # print("  <<== response" + str(result))
    if result:
        # result['Message'],result['Type'], result['ClientState']
        return make_ussd_response1(result, 200)
    return make_ussd_response('Please try again', 400)



def handler(responseData):
    if (responseData['text'] == ""):

        # // This is the first request. Note how we start the response with CON
        response  = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"
    elif (responseData['text'] == "1"):

        # // Business logic for first level response
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"
    return response




def make_ussd_response(response, statusCode):
  return Response(response=json.dumps(response,
      default=json_util.default),
      status=statusCode,
      mimetype="application/json")

def make_ussd_response1(response, statusCode):
  return Response(response=json.dumps(response,
      default=json_util.default),
      status=statusCode,
      mimetype="text/plain")
