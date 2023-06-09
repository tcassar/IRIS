import asyncio
from unittest import TestCase
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")


class TestSockets(TestCase):

    def test_hello(self):
        asyncio.run(hello())
