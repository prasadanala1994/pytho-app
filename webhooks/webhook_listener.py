from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    print('Webhook received!')
    # Simple validation could be implemented here
    subprocess.run(["./update_container.sh"])
    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)