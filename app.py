from aiohttp import web
import socketio
from datetime import datetime
import asyncio

sio = socketio.AsyncServer()
app = web.Application()
runner = web.AppRunner(app)
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_get('/', index)

async def tick():
    tt = datetime.now().isoformat()
    await sio.emit('tick', {'data': tt})
    print(tt)
    await asyncio.sleep(2)
    await tick()

async def main():
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    while True:
        await tick()


if __name__ == '__main__':
    asyncio.run(main())
