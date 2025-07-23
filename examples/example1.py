import asyncio
from BlueMapWrapper import AsyncClient, marker_keys

async def main():
    # printing out all players and lands plugin markers
    client = AsyncClient(base_url='http://map.eldrath.com:20098')   # Setting up Async Client, AsyncClient Object
    collection = await client.fetch_collection('world')   # Fetching player and marker Collection from map, Collection Object
    for player in collection.player_collection.players:   # Iterate through all players
        print(f"Player: {player.name}\nPosition: {player.position}")
    marker_collection = collection.marker_collection   # Getting MarkerCollection Object from Collection
    lands = marker_collection.from_key(marker_keys.LANDS)   # Getting Marker for Lands Plugin
    for marker in lands.markers:   # Iterate though markers in lands
        print(f"Name: {marker.label}\nPosition: {marker.position}")
    await client.close()   # Close client after use


if __name__ == '__main__':
    asyncio.run(main())