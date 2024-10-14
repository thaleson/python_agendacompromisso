import os
import sys
from redis import Redis
from rq import Worker, Queue, Connection
from app.tasks import enviar_email_lembrete
from config import Config

listen = ['default']

redis_conn = Redis.from_url(Config.REDIS_URL)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()
