from discord.ext import commands
import os
import traceback

bot = commands.Bot
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
    
@bot.command()
async def Pちゃん(ctx):
    await ctx.send('うんち！')
    
    
    
@bot.command()
async def おやすみ！(ctx):
    await ctx.send('はよねろよ！')    



bot.run(token)
