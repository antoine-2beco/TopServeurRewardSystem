# coding:utf-8
import discord
import ts_config_bot
import modules.ts_getreward_bot

bot = discord.Client(intents=discord.Intents.all())


# Launch
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print("Bot opérationnel !")


# Get Reward Command
@bot.event
async def on_message(message):
    splited_message = message.content.split(' ')
    command = splited_message[0]

    args = []
    for arg in splited_message:
        args.append(arg)

    if command == ts_config_bot.reward_command:
        if not len(args) != 2:
            await modules.ts_getreward_bot.get_reward(message, args)
        else:
            await message.channel.send(f"{message.author.mention} Vous n\'avez pas exécuter la commande correctement.")

print("Lancement du bot...")
bot.run(ts_config_bot.bot_token)
