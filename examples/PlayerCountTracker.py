import bluemap_wrapper
import datetime
import time
import asyncio

async def main():
    client = bluemap_wrapper.AsyncClient('http://map.eldrath.com:20098')   # Initialise Client
    logged_players = []
    while True:
        start = time.time()
        maps = await client.fetch_maps()   # Fetch list of available maps
        players_collection = await client.fetch_player_collection(maps[0]) # Get Player Collection obj of online players

        if players_collection.length == 0:
            print(f"{datetime.datetime.now()} No players found.")
        player_names = [i.name for i in players_collection.players]   # Get list of player names

        for i in player_names:
            if i not in logged_players:   # Check if player was in game when last logged
                print(f"[{datetime.datetime.now()}] Player {i} joined the game")   # Print current time and player

        for i in logged_players:
            if i not in player_names:   # Check if any player in logged players left the game/went invisible
                print(f"[{datetime.datetime.now()}] Player {i} left the game/went invisible")

        logged_players = player_names   # Log current players available for next minute
        seconds_until_next_minute = start+60 - time.time()   # Calculate time until next minute from starting
        await asyncio.sleep(seconds_until_next_minute)   # Wait until 1 minute from loop start

asyncio.run(main())