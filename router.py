from fastapi import APIRouter
# from backend.src.init import cmc_client
from init import cmc_client
router = APIRouter(
    prefix="/cryptocurrencies",
)


@router.get("/cryptodominance")
async def cryptodominance():
    return await cmc_client.bitcoin_dominance()
