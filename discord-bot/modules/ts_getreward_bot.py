# coding:utf-8
import discord
import requests
import json
import paramiko
from datetime import datetime
from pytz import timezone

import ts_config_bot
import modules.ts_getreward_bot


async def get_reward(message, args):
    # ---# CONFIG #---#
    error_channel_embed = discord.Embed(title="Erreur de l\'exécution de la commande",
                                        description="Vous ne pouvez pas exécuter cette commande dans ce channel.",
                                        color=ts_config_bot.embed_color,
                                        timestamp=datetime.now(tz=timezone(ts_config_bot.timezone)))
    error_role_embed = discord.Embed(title="Erreur de l\'exécution de la commande",
                                     description="Vous n\'avez pas les rôles nécessaires pour exécuter cette commande.",
                                     color=ts_config_bot.embed_color,
                                     timestamp=datetime.now(tz=timezone(ts_config_bot.timezone)))
    vote_not_found = f"{message.author.mention} Le vote n\'a pas été trouvé."
    already_reclamed = f"{message.author.mention} Ce vote a déjà été réclamé."
    reward_gived = f"{message.author.mention} Vous avez reçu votre gain en jeu."
    # ---# CONFIG #---#

    await message.delete(delay=2)

    channel_tryed = role_tryed = 0

    if len(ts_config_bot.reward_channels_ids) != 0:
        for channel in ts_config_bot.reward_channels_ids:
            if channel == message.channel.id:
                break
            else:
                channel_tryed = channel_tryed + 1
                if channel_tryed == len(ts_config_bot.reward_channels_ids):
                    await message.channel.send(embed=error_channel_embed)
                    return

    if len(ts_config_bot.reward_necessary_roles_ids) != 0:
        for necessary_role in ts_config_bot.reward_necessary_roles_ids:
            for member_role in message.author.roles:
                if member_role.id == necessary_role:
                    break
                else:
                    role_tryed = role_tryed + 1
                    max_role_tryed = len(ts_config_bot.reward_necessary_roles_ids) * len(message.author.roles)
                    if role_tryed == max_role_tryed:
                        await message.channel.send(embed=error_role_embed)
                        return

    dict_reponse = json.loads(requests.get(url=f"https://api.top-serveurs.net/v1/votes/claim-steam?server_token={ts_config_bot.ts_server_token}&steam_id={args[1]}").text)

    # Vote Not Found
    if dict_reponse.get("claimed") == 0:
        await message.channel.send(content=vote_not_found)
        return

    # Already Claimed
    if dict_reponse.get("claimed") == 2:
        await message.channel.send(content=already_reclamed)
        return

    # Vote Found - Not Claimed Vote - Give Reward
    if dict_reponse.get("claimed") == 1:
        print("GG")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ts_config_bot.host, ts_config_bot.port, ts_config_bot.username, ts_config_bot.password)

        ssh.exec_command(f"mm addmoney {args[1]} {ts_config_bot.reward_amount}")
        await message.channel.send(content=reward_gived)
        return
