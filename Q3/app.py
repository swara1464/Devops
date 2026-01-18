from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Dockerized App</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }
                h1 { color: #333; }
                .container { border: 1px solid #ddd; padding: 20px; display: inline-block; background: white; border-radius: 8px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from Docker! 🐳</h1>
                <p>This simple web application is running inside a container.</p>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
