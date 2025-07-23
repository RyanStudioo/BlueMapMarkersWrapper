import asyncio
from BlueMapWrapper import AsyncClient

async def main():
    # Setting up Async Client
    client = AsyncClient(base_url='http://map.eldrath.com:20098')
    # Fetching Collection from map
    collection = await client.from_map('world')
    # Fetching 'lands' plugin MarkerSet
    lands_set = collection.from_key("me.angeschossen.lands")
    # Printing label
    print(lands_set.label)
    # Iterating through Markers in MarkerSet
    for i in lands_set.markers:
        # Printing key, label, and position of Marker
        print(f"{i.label}({i.key}): {i.position}")
    # Closing Client
    await client.close()

if __name__ == '__main__':
    asyncio.run(main())