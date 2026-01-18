from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception as e:
        return f"Could not connect to Redis: {e}"
        
    return f'''
    <html>
        <head>
            <title>Docker Compose Demo</title>
            <style>
                body {{ font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f0f8ff; }}
                .box {{ border: 2px solid #007bff; padding: 20px; display: inline-block; background: white; border-radius: 10px; }}
                h1 {{ color: #007bff; }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Hello from Docker Compose! 🐳</h1>
                <p>This page has been viewed <strong>{count}</strong> times.</p>
                <p><small>(Counter is stored in Redis)</small></p>
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
