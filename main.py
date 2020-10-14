import discord
import tokenFile
# id from msg - message.author.id

class MyClient(discord.Client):
    async def initializate(self):
        self.battleCh = None
        self.isWaitingForSlap = False
        self.playerOne = None
        self.playerTwo = None
        self.rememberedAuthor = None
        self.isGameRunning = False

    async def on_ready(self):
        print('Logged on as', self.user)
        print('ID is', self.user.id)
        await self.initializate()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong!')
            

client = MyClient()
client.run(tokenFile.token)
