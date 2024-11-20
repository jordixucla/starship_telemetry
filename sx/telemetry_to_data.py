import time
import http.client, urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

def append_telemetry_data():
    with open("telemetry_ift4.txt", "r") as telemetry_file:
        for line in telemetry_file:
            with open("data.txt", "a") as data_file:
                data_file.write(line)
            time.sleep(1)

def send_data_to_thingspeak():
    for i in range(30):
        # Enviar la temperatura exterior a thingspeak
        params = urllib.parse.urlencode({'field1': i, 'field2': i*2, 'field3': i*3, 'field4': i*4, 'key':'QZH2CNVSE6688TMD'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()    
        print((response.status, response.reason))
        data = response.read()
        conn.close()
        with open("data.txt", "a") as file:
            file.write(f"{i}, {i}, {i*2}, {i*3}, {i*4}\n")
        time.sleep(2)

append_telemetry_data()
