from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>ChatGPT Wrapper</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
            }
            .messages {
                height: 400px;
                overflow-y: scroll;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f8f9fa;
            }
            .message {
                margin-bottom: 10px;
            }
            .message.user {
                text-align: right;
                background-color: #e9ecef;
                color: #343a40;
                border-radius: 10px;
                padding: 10px;
                margin-right: 0;
                margin-left: auto;
            }
            .message.assistant {
                text-align: left;
                background-color: #343a40;
                color: #f8f9fa;
                border-radius: 10px;
                padding: 10px;
                margin-right: auto;
                margin-left: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="messages" id="messages"></div>
            <div class="input-group">
                <input type="text" id="messageText" class="form-control" placeholder="Type your message..." aria-label="Message" aria-describedby="button-addon2">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" id="sendButton">Send</button>
                </div>
            </div>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = $('#messages');
                var message = $('<div>').addClass('message assistant').text(event.data);
                messages.append(message);
                messages.scrollTop(messages[0].scrollHeight);
            };
            $('#sendButton').click(function() {
                var input = $('#messageText');
                var message = $('<div>').addClass('message user').text(input.val());
                $('#messages').append(message);
                ws.send(input.val());
                input.val('');
                $('#messages').scrollTop($('#messages')[0].scrollHeight);
            });
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        import google.generativeai as genai

        genai.configure(api_key="AIzaSyAZ7dtvfCTX0X8V6Qfaxi6TN_VQ9rCM9wo")

        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(data)
        await websocket.send_text(response.text)

# AIzaSyAZ7dtvfCTX0X8V6Qfaxi6TN_VQ9rCM9wo