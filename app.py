from flask import Flask, render_template_string
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Full Name
    full_name = "Your Full Name"  # Replace with your actual full name

    # System Username
    username = os.getlogin()

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top output
    top_output = subprocess.getoutput("top -b -n 1")  # Get the `top` command output

    # HTML Template to render the data
    html = f"""
    <html>
    <head><title>Htop Endpoint</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
