from BlueMapWrapper import AsyncClient, KEYS
import asyncio

async def main():
    async with AsyncClient(base_url='http://map.eldrath.com:20098') as client:   # Initialise Client, and automatically close if finished
        marker = await client.fetch_marker_collection("world")   # Get MarkerCollection object of "world"
        markerSet = marker.from_key(KEYS.LANDS)# Get MarkerSet for "LANDS" Plugin

        for i in markerSet:   # Iterate through MarkerSet class
            print(f"{i.key}, {i.label}")
        for i in markerSet.markers: # Alternatively if you want to use list methods, you can access the list directly
            print(f"{i.key}, {i.label}")



asyncio.run(main())