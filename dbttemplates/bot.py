import discord
import json
import os

from discord.ext import commands


class BotName(commands.Bot):
    def __init__(self):
        self._config = json.load(open("config.json", "r"))
        self.color = int(self._config["color"], 16) + 0x200
        
        super().__init__(
            self._config["prefix"],
            intents=discord.Intents.all(),
        )

    async def on_ready(self):
        print(f"[{self.__class__.__name__}] - Connected.")

    def run(self):
        for extention in os.listdir("cogs"):
            if extention.endswith(".py"):
                self.load_extension(f"cogs.{extention[:-3]}")
                print(f"{extention} Loaded Successfully")
                
        super().run(self._config["token"])
        

if __name__ == '__main__':
    bot_instance = BotName()
    bot_instance.run()