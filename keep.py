from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask with threading!"

def run_app():
    app.run(host='0.0.0.0', port=81)

if __name__ == "__main__":
    thread = threading.Thread(target=run_app)
    thread.start()

    # Thực hiện các công việc khác trong main thread nếu cần
    # Ví dụ:
    print("Flask app is running in a separate thread")
