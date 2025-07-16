from datetime import datetime
import csv

from fastapi import FastAPI

from config import settings

from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from init import cmc_client


async def update_bitcoin_dominance():

    dominance_data = str(await cmc_client.bitcoin_dominance())
    print(dominance_data)
    with open(settings.DOMINANCE_STATISTIC_FILE, 'a') as fl:
        csv_writer = csv.writer(fl)
        time_now = datetime.now()
        row = [[time_now, dominance_data]]
        csv_writer.writerows(row)

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Настройка и запуск планировщика
        scheduler.add_job(
            update_bitcoin_dominance,
            trigger=IntervalTrigger(hours=1),
            id='updater_bitcoin_dominance',
            replace_existing=True
        )
        scheduler.start()
        yield
    except Exception as e:
        pass
    finally:
        scheduler.shutdown()