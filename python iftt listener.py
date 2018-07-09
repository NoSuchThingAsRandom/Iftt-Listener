import logging
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
import ssl
import subprocess

token = "PASSWORD"


class httpFunctions(BaseHTTPRequestHandler):
	def do_GET(self):
		logger.info("Sending get request")
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("Hello!", "utf8"))
		return

	def do_POST(self):
		logger.info("Post received")
		self.send_response(200)
		self.end_headers()
		logger.info(self.client_address)
		logger.info(self.headers)
		length = int(self.headers["content-length"])
		body = str(self.rfile.read(length)).replace("b'", "").replace("'", "")
		data = json.loads(body)
		if token != data["TOKEN"]:
			logger.info("INVALID")
			return
		logger.info("Token valid, doing task: " + data["TASK"])
		if data["TASK"] == "TESTING":
			logger.info("Testing successful")
			return
		elif data["TASK"]=="ALEXA":
			logger.info("Alexa received")
		elif data["TASK"]=="SAM PC":
			logger.info("SAM PC")
			logger.info(subprocess.run(["./tpPlug.sh","192.168.0.36","on"]))
			time.sleep(1)
			logger.info(subprocess.run(["./wakePC.sh","SAM"]))
		elif data["TASK"]=="PETE PC":
			logger.info("Booting Pete's computer")
			logger.info(subprocess.run(["./tpPlug.sh","192.168.0.48","on"]))
			time.sleep(1)
			logger.info(subprocess.run(["./wakePC.sh","PETE"]))
		else:
			logger.info("Unknown request")
		return



logger =logging.getLogger("exmaple")
logger.setLevel(logging.INFO)
fh =logging.FileHandler("Boot_PC_LOGS/"+str(datetime.date.today())+".log")
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("Started Program")
PORT = 6000

httpd = HTTPServer(("192.168.0.43", PORT), httpFunctions)

httpd.socket=ssl.wrap_socket(httpd.socket,
                              server_side=True,
                               certfile="cert.pem",
                               keyfile="key.pem")

logger.info("Server started")
httpd.serve_forever()
