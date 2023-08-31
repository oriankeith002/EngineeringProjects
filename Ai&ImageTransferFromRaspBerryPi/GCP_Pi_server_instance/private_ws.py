import asyncio
from websockets.server import serve


async def echo(websocket):
    # await websocket.send("hi")
    async for message in websocket:
        print("Received: ", str(message)[:20])
        await websocket.send("count: 3")


async def main():
    async with serve(echo, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())


