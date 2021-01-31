import fangcore
import os

pages = {}


for file in os.listdir("HTML"):
	opened = open("HTML/" + file, "rb")
	pages[file] = opened.read()
	opened.close()

HTTP_server = None
def response_handler(client_obj):

	if client_obj.split_request == []:
		client_obj.set_page(pages['Rawr-main.html'])
		client_obj.add_tag(b"Content-Type", b"text/html")
	else:
		if client_obj.split_request[0] == "REINIT":
			HTTP_server.stop_http_server()
			return
		try:
			client_obj.set_page(pages[client_obj.split_request[0]])
		except KeyError:
			client_obj.set_response_header(b"404 Page Not Found")

HTTP_server = fangcore.HTTPServer()

HTTP_server.start_http_server("localhost", 80, 2)

HTTP_server.set_response_method(response_handler)

