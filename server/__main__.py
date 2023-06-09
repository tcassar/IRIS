"""Establishes web socket stream, sets up logging"""

import asyncio
import logging
import websockets

from server.sockets import hello


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    # set up logging from websockets
    logger = logging.getLogger("websockets")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    # run the handler
    asyncio.run(main())
