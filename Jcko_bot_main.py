import hikari
import lightbulb


bot=lightbulb.BotApp(
    token='insert here',  
default_enabled_guilds=(guildnumber, guildnumber, guildnumber, guildnumber)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Initialzing Jcko')

@bot.command
@lightbulb.command('joke', 'tells a joke, ig???')
@lightbulb.implements(lightbulb.SlashCommand)

#funcheader
async def hi(ctx):
    await ctx.respond('YOU!!! HAHAHAHAHAHAHH XD XD XD LMAOOO ROFLROFLROFLL LOLOLOLOOL')


bot.run()

