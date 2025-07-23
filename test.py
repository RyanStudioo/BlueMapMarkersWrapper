import asyncio
from asyncclient import AsyncClient

async def main():
    client = AsyncClient(base_url='http://map.eldrath.com:20098')
    maps = await client.fetch_markers('world')
    for i in maps:
        print(i.key)
        for item in i.markers:
            print(f"{item.label}")
    await client.close()

if __name__ == '__main__':
    asyncio.run(main())