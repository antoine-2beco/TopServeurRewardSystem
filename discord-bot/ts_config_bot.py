# coding:utf-8
from datetime import datetime
from pytz import timezone
import discord

# Général
bot_token = ""  # Token du Bot Discord
embed_color = discord.Color.from_rgb(47, 49, 54)  # Couleur des embeds
timezone = "Europe/Brussels"  # Timezone des embeds

# Get Reward
reward_command = "ts!reward"
reward_channels_ids = []  # Canaux dans lequel on peut exécuter la commande
reward_necessary_roles_ids = []  # Rôles nécessaires pour exécuter la commande
reward_amount = '500'  # Total d'argent donné pour la récompense

# Top Serveur
ts_server_token = ''  # Identifiant API du serveur sur Top Serveur


# SSH Connection
host = ''  # Host SSH
port = 0  # Port SSH
username = ''  # Username SSH
password = ''  # Mot de passe SSH
