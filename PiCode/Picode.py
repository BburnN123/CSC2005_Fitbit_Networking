#code for Raspberry pi to test
import SocketServer
import SimpleHTTPServer
import math
import json

import datetime
import csv
import os.path
from os import path
import json
from io import BytesIO

PORT = 9090

data = dict()
t = datetime.datetime.now().date().strftime("%m_%d_%Y")

filename = "test_" + t + ".csv"
fieldnames = ['time', 'gyro_x', 'gyro_y', 'gyro_z', 'accel_x', 'accel_y', 'accel_z']


class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        req = self.rfile.read(content_length)
       
        json_body =  json.loads(req)
        if not path.exists(filename):
            with open(filename, 'w') as csv_output:  
                csv_writer = csv.DictWriter(csv_output, fieldnames = fieldnames, delimiter=",", lineterminator='\n')
                csv_writer.writeheader()

        with open(filename, mode='a+', encoding='utf-8-sig') as csv_output:
            csv_writer = csv.DictWriter(csv_output, fieldnames = fieldnames, delimiter=",", lineterminator='\n')
            output = { 'time' : "", 'gyro_x' : json_body["gyro"]["x"] , 'gyro_y' : json_body["gyro"]["y"] , 'gyro_z' : json_body["gyro"]["z"], 'accel_x' : json_body["accel"]["x"], 'accel_y' : json_body["accel"]["y"], 'accel_z' : json_body["accel"]["z"]}
            csv_writer.writerow(output)      
       
        #write to CV or something

httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
