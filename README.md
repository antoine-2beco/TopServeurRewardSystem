# ENGLISH
## TopServeurRewardSystem
Reward system on Garry's Mod claimable thanks to a Discord bot following a vote on https://top-serveurs.net.

## How to use ?
- Configure ts_config_bot;
- Place the money-manager.lua file in your Garry's Mod server;
- Install the Python modules present in requirements.txt;
- Launch the Discord bot.

## How does it work ?
To claim a reward, the user must execute the command designated in ts_config_bot in the Discord channel designated in ts_config_bot followed by the Steam ID 64 of the voting user. The user must have logged into Top Servers through Steam!
Following the sending of the command, the program queries the API of Top Servers concerning the claimability of the vote then if it is positive, an SSH request containing a command which calls the money-manager.lua script is sent to the Garry's server. Mod which allows the sending of the defined money, whether the player is connected or not. The system only works with DarkRP game mode.


# FRANCAIS
## TopServeurRewardSystem
Système de récompense sur Garry's Mod réclamable grâce à un bot Discord suite à un vote sur https://top-servers.net.

## Comment utiliser?
- Configurer ts_config_bot;
- Placez le fichier money-manager.lua dans votre serveur Garry's Mod;
- Installer les modules Python présents dans requirements.txt;
- Lancer le bot Discord.

## Comment ça marche?
Pour réclamer une récompense, l'utilisateur doit exécuter la commande désignée dans ts_config_bot dans le canal Discord désigné dans ts_config_bot suivi du Steam ID 64 de l'utilisateur votant. L'utilisateur doit s'être connecté à Top Servers via Steam!
Suite à l'envoi de la commande, le programme interroge l'API des Top Servers concernant la réclamation du vote puis s'il est positif, une requête SSH contenant une commande qui appelle le script money-manager.lua est envoyée au serveur de Garry. Mod qui permet l'envoi de l'argent défini, que le joueur soit connecté ou non. Le système fonctionne uniquement avec le mode de jeu DarkRP.
