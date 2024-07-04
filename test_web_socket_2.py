import asyncio
import json
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/ws/chat/testroom/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1Mjg2NjY0LCJpYXQiOjE3MjAxMDI2NjQsImp0aSI6IjBiZmU3NWEzYmFlNTRkZTFiMjFjZGZkZjRiYmE5MWExIiwidXNlcl9pZCI6Nn0.mstJYQOYCLmXNlFZ8aghqtzZ9pVUPdqJUQAHYTSnkKg"
    async with websockets.connect(uri) as websocket:
        # Test sending a message
        message = {"message": "Hello, WebSocket! by user 1"}
        await websocket.send(json.dumps(message))
        print(f"Sent: {message}")

        # Test receiving a message
        while(True):
            response = await websocket.recv()
            print(f"Received: {response}")

# Run the test

asyncio.get_event_loop().run_until_complete(test_websocket())