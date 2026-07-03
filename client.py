from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, BASE_URL
from logger_config import logger


class BinanceTrader:

    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL

    def place_order(
            self,
            symbol,
            side,
            order_type,
            quantity,
            price=None):

        try:

            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }

            if order_type.upper() == "LIMIT":

                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"Order Request : {params}")

            response = self.client.futures_create_order(**params)

            logger.info(f"Order Response : {response}")

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise

        except Exception as e:

            logger.error(e)

            raise