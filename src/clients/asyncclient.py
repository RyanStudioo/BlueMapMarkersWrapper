from __future__ import annotations
from typing import List
import aiohttp
from typing import Dict
from src.settings import Settings
from src.MarkerSet import MarkerSet

class AsyncClient:
    def __init__(self, base_url:str):
        self._session = aiohttp.ClientSession()
        self._base_url = base_url

    async def fetch_maps(self):
        settings_link = f"{self._base_url}/settings.json"
        settings_response = await self._get_json(settings_link)
        settings = Settings._from_response(settings_response)
        return settings.maps

    async def fetch_markers(self, world) -> List[MarkerSet]:
        markers_link = f"{self._base_url}/maps/{world}/live/markers.json"
        markers_response = await self._get_json(markers_link)
        marker_sets = []
        for key, item in markers_response.items():
            marker_sets.append(MarkerSet._from_response(key=key, response_json=item))
        return marker_sets

    async def close(self):
        await self._session.close()

    async def _get_json(self, url:str, headers:dict=None, json:dict=None) -> Dict:
        async with self._session.get(url, headers=headers, json=json) as response:
            response.raise_for_status()
            return await response.json()
