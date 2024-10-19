from flask import Flask, jsonify
from datetime import datetime
import subprocess
import pytz
import os
import platform
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    name = "Your Unique Full Name"  
    
    username = os.getlogin()
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    os_info = f"{platform.system()} {platform.release()} {platform.version()}"
    

    cpu_count = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)
    

    memory_info = psutil.virtual_memory()
    total_memory = round(memory_info.total / (1024 ** 3), 2)  # Convert to GB
    available_memory = round(memory_info.available / (1024 ** 3), 2)  # Convert to GB
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    #here im building the response
    response = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <p><strong>OS Info:</strong> {os_info}</p>
    <p><strong>CPU Count:</strong> {cpu_count}</p>
    <p><strong>CPU Usage:</strong> {cpu_usage}%</p>
    <p><strong>Total Memory:</strong> {total_memory} GB</p>
    <p><strong>Available Memory:</strong> {available_memory} GB</p>
    <h2>TOP Command Output</h2>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
