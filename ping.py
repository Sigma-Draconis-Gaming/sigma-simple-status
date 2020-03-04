import datetime
import time

import requests
from discord_webhooks import DiscordWebhooks

web_hook_url = ""



def check_and_ping():
    r = requests.get("https://api.sigmadraconis.games/servers/se")
    servers = r.json()["servers"]
    webhook = DiscordWebhooks(web_hook_url)
    t = sum([int(x['players']) for x in servers])
    webhook.set_content(
        description=f"Total Players: {t}",
        timestamp=str(datetime.datetime.now()),
        color=0xF58CBA)
    try:
        webhook.send()
    except Exception as x:
        print(x)
    time.sleep(4)
    for server in servers:
        if server["status"] != "ok":
            webhook.set_content(
                content="@everyone <@508798592681508877>\n"
                        "p.s DONT DELETE THIS WEBHOOK, MUTE THE CHANNEL, IF YOU DELETE IT YOU WILL DIE",
                title="Something died i think?",
                description=f"Hey, {server['name']} is dead? fix it",
                timestamp=str(datetime.datetime.now()),
                color=0xF58CBA)
            time.sleep(4)
            try:
                webhook.send()
            except Exception as x:
                print(x)
        else:
            webhook.set_content(
                description=f"{server['name']} is online\nPing : {server['ping']}\nPlayers: {server['players']}",
                timestamp=str(datetime.datetime.now()),
                color=0xF58CBA)
            try:
                webhook.send()
            except Exception as x:
                print(x)
            time.sleep(4)
            print(server)


if __name__ == "__main__":
    while True:
        check_and_ping()
        time.sleep(300)
