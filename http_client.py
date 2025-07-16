from dataclasses import dataclass

from aiohttp import ClientSession

@dataclass
class HTTPClient:

    def __init__(self, base_url: str,api_key: str,):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,

            }
        )

class CMCHTTPClient(HTTPClient):

    async def bitcoin_dominance(self):
        async with self._session.get("/v1/global-metrics/quotes/latest")as resp:
            result = await resp.json()
            return str(result["data"]["btc_dominance"])
