from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import asyncio
from typing import List
import aiohttp
from typing import Dict

from ..player import Player
from ..settings import Settings
from ..MarkerSet import MarkerSet
from ..Collections import MarkerCollection, PlayerCollection, Collection


class AsyncClient:
    def __init__(self, base_url:str):
        self._session = aiohttp.ClientSession()
        self._base_url = base_url

    async def _get_markers_json(self, world:str) -> Dict:
        markers_link = f"{self._base_url}/maps/{world}/live/markers.json"
        markers_response = await self._get_json(markers_link)
        return markers_response

    async def _get_players_json(self, world:str) -> Dict:
        players_link = f"{self._base_url}/maps/{world}/live/players.json"
        players_response = await self._get_json(players_link)
        return players_response

    async def fetch_maps(self):
        settings_link = f"{self._base_url}/settings.json"
        settings_response = await self._get_json(settings_link)
        settings = Settings.from_response(settings_response)
        return settings.maps

    async def fetch_marker_collection(self, world:str) -> MarkerCollection:
        markers_response = await self._get_markers_json(world)
        marker_collection = MarkerCollection._from_response(markers_response)
        return marker_collection

    async def fetch_players_collection(self, world:str) -> PlayerCollection:
        players_response = await self._get_players_json(world)
        players_collection = PlayerCollection._from_response(players_response)
        return players_collection

    async def fetch_collection(self, world:str) -> Collection:
        with ThreadPoolExecutor(max_workers=2) as executor:
            markers = executor.submit(self.fetch_marker_collection, world)
            players = executor.submit(self.fetch_players_collection, world)
        collection = Collection(await markers.result(), await players.result())
        return collection


    async def close(self):
        await self._session.close()

    async def _get_json(self, url:str, headers:dict=None, json:dict=None) -> Dict:
        async with self._session.get(url, headers=headers, json=json) as response:
            response.raise_for_status()
            return await response.json()
