from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.color


def setup(bot):
    bot.add_cog(CogName(bot))