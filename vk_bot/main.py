import logging
import threading

from const import longpoll
from handlers import db, vk, handle_update
from worker import newsletter


def main():
    logging.basicConfig(level=logging.INFO)
    threading.Thread(target=newsletter, args=(db, vk)).start()
    try:
        for event in longpoll.listen():
            threading.Thread(target=handle_update, args=(event,)).start()
    except Exception:
        pass
if __name__ == "__main__":
    main()
