from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
import random
import urllib.parse
import requests

# Create DB
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    rollno TEXT PRIMARY KEY,
    password TEXT,
    parent_phone TEXT,
    student name,
    otp TEXT
)
""")

conn.commit()

# Add sample student
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ai603','1234','7993412288','k.venkat reddy','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ai609','1234','9949418655','k.bramha reddy','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ai143','1234','9440470288','B.mohit sai','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11aic05','1234','9394662255','kiran','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ai650','1234','9652592560','dhanush','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ai070','1234','9949418655','navya','')")
cursor.execute("INSERT OR IGNORE INTO students VALUES ('25b11ece411','1234','9949418655','kavya','')")

conn.commit()


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        data = json.loads(data)

        if self.path == "/generate":
            roll = data["rollno"]
            password = data["password"]
            studend name = data["student name"]
            cursor.execute("SELECT * FROM students WHERE rollno=? AND password=? AND student name=?", (roll, password,student name))
            user = cursor.fetchone()

            if user:
                otp = str(random.randint(1000, 9999))

                cursor.execute("UPDATE students SET otp=? WHERE rollno=?", (otp, roll))
                conn.commit()

                phone = user[2]

                # 🔴 FAST2SMS API (Replace API KEY)
                url = "https://www.fast2sms.com/dev/bulkV2"
                payload = f"variables_values={otp}&route=otp&numbers={phone}"
                headers = {
                    'authorization': "gRfd3krPFhnAH8jt1SqyLUmzc2eCQKYXNGJiObZ4ol9u6B0V5DNfzFW2ngrRcCmZVxlUAH5jKQPE3s4h",
                    'Content-Type': "application/x-www-form-urlencoded"
                }

                requests.post(url, data=payload, headers=headers)

                self.respond("OTP Sent to Parent")

            else:
                self.respond("Invalid Login")

        elif self.path == "/verify":
            roll = data["rollno"]
            otp = data["otp"]

            cursor.execute("SELECT otp FROM students WHERE rollno=?", (roll,))
            real_otp = cursor.fetchone()

            if real_otp and real_otp[0] == otp:
                self.respond("✅ Outpass Approved")
            else:
                self.respond("❌ Wrong OTP")
cursor.execute("""
CREATE TABLE IF NOT EXISTS warden(
    username TEXT,
    password TEXT
)
""")

cursor.execute("INSERT OR IGNORE INTO warden VALUES ('warden@adityauniversity.in','aditya123')")
conn.commit()
    def respond(self, msg):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(msg.encode())
elif self.path == "/warden_login":
    user = data["username"]
    password = data["password"]

cursor.execute("INSERT OR IGNORE INTO warden VALUES ('warden@adityauniversity.in','aditya123')")
conn.commit()
    cursor.execute("SELECT * FROM warden WHERE username=? AND password=?", (user, password))
    result = cursor.fetchone()

    if result:
        self.respond("✅ Login Success")
    else:
        self.respond("❌ Invalid Warden")

server = HTTPServer(("localhost", 8000), MyServer)
print("Server running at http://localhost:8000")
server.serve_forever()
