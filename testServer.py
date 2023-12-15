import asyncio
 
import websockets
 
# create handler for each connection
 
async def handler(websocket, path):
    data = await websocket.recv()
    print(data)
    reply = f"Data recieved as:  {data}!"
    await websocket.send(str([1,2]))

start_server = websockets.serve(handler, "localhost", 3030)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

