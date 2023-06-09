async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello, {name}"
    await websocket.send(greeting)
    print(f">>> {greeting}")
