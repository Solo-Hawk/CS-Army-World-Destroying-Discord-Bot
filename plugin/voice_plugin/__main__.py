import os, sys
import typing
import discord
import queue
from threading import Thread
import asyncio
import time

class VoicePlugin(object):
    def __init__(self):
        self.voice = None
        self.player = None
        self.song_queue = queue.Queue()
        self.thread = None
        self.loop = None

    async def join(self,voice, message, discord_client: object) -> str:
        if self.voice != None:
            self.voice = voice

        if self.thread == None:
            self.thread = asyncio.ensure_future(self.daemon())
       #     self.loop = asyncio.get_event_loop()
       #     self.loop.run_until_complete(self.thread)

        temp = message.content.split()
        self.song_queue.put(temp[1])

    async def stop(self, voice, message, discord_client):
        try:
            self.player.pause()
        except Exception as e:
            pass

    async def vol(self, voice, message, discord_client):
        try:
            self.player.volume = message.content.split()[-1]
        except Exception as e:
            pass

    async def start(self, voice, message, discord_client):
        try:
            self.player.resume()
        except Exception as e:
            pass

    async def skip(self, voice, message, discord_client):
        self.player.stop()

    async def daemon(self):
        print("thread one")
        while True:
            if self.player == None or self.player.is_done():
                print("strange")
                temp = self.song_queue.get()
                print(temp)
                self.player = await self.voice.create_ytdl_player(self.song_queue.get())
                self.player.volume = 0.2
                self.player.start()
                print(self.player)
            await asyncio.sleep(1)
