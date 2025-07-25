<h1><img alt="bluemap logo" src="Documentation/images/bluemap_logo.png" height=25px> BlueMapWrapper</h1>

An open-sourced API wrapper for BlueMap for Python!!

This wrapper is used for getting information from existing Blue Maps, NOT to create one.

# Installation
>## Windows
> pip install bluemap_wrapper
> ## Linux
> python -m pip install bluemap_wrapper

## Quick Example
```commandline
import asyncio
from bluemap_wrapper import AsyncClient, KEYS

async def main():
    # printing out all players and lands plugin markers
    
    # Setting up Async Client, AsyncClient Object
    client = AsyncClient(base_url='http://map.eldrath.com:20098')   
    
    # Fetching player and marker Collection from map, Collection Object
    collection = await client.fetch_collection('world')   
    
    for player in collection.player_collection:   # Iterate through all players
        print(f"Player: {player.name}\nPosition: {player.position}")
        
    # Getting MarkerCollection Object from Collection
    marker_collection = collection.marker_collection
    
    # Getting Marker for Lands Plugin   
    lands = marker_collection.from_key(KEYS.LANDS) 
    
    for marker in lands:   # Iterate though markers in lands
        print(f"Name: {marker.label}\nPosition: {marker.position}")
        
    await client.close()   # Close client after use


if __name__ == '__main__':
    asyncio.run(main())
```

# Documentation Contents
- ## [Clients](Documentation/Clients.md#clients)
    - [Client](Documentation/Clients.md#client)
    - [AsyncClient](Documentation/Clients.md#asyncclient)
- ## [Collections](Documentation/Collections.md#collections)
  - [Collection](Documentation/Collections.md#collection)
  - [MarkerCollection](Documentation/Collections.md#markercollection)
  - [PlayerCollection](Documentation/Collections.md#playercollection)