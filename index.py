import plivo

PLIVO_AUTH_ID = ""
PLIVO_AUTH_TOKEN = ""

plivo_number = "119494822725"
destination_number = "+919460861875"
text = "Yo Navi"

message_params = {
      'src':plivo_number,
      'dst':destination_number,
      'text':text,
    }

p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

print p.send_message(message_params) 
