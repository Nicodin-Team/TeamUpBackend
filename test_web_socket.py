import asyncio
import json
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/ws/chat/test/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1Mjg2NDE2LCJpYXQiOjE3MjAxMDI0MTYsImp0aSI6IjBmOTcxYjE4ZDExNTRlY2JiMjQ5YTA0OTljZjVkZDA1IiwidXNlcl9pZCI6MX0.J3vfegLlzISurlMmtxbmibmdqyl8mBBbHPhv237Dtng"
    async with websockets.connect(uri) as websocket:
        # Test sending a message
        message = {"message": "Hello, WebSocket by user 2!"}
        await websocket.send(json.dumps(message))
        print(f"Sent: {message}")

        # Test receiving a message
        while(True):
            response = await websocket.recv()
            print(f"Received: {response}")

# Run the test
asyncio.get_event_loop().run_until_complete(test_websocket())
