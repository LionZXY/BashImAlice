import sqlite3

from aiohttp import web

from aioalice import Dispatcher, get_new_configured_app

DB_FILE = 'quotes.sqlite3'
WEBHOOK_URL_PATH = '/quote/'  # webhook endpoint

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001


class BashImQuoter:
    def __init__(self):
        self.db = sqlite3.connect(DB_FILE)

    def get_random_quote(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT text FROM quotes ORDER BY RANDOM() LIMIT 1;')
        quote_text = cursor.fetchone()[0]
        cursor.close()
        return quote_text


dp = Dispatcher()
quoter = BashImQuoter()


@dp.request_handler()
async def handle_all_requests(alice_request):
    return alice_request.response(quoter.get_random_quote(), end_session=True)


if __name__ == '__main__':
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
