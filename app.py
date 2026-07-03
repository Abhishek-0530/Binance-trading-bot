import argparse

from client import BinanceTrader


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)

    parser.add_argument("--side", required=True,
                        choices=["BUY", "SELL"])

    parser.add_argument("--type", required=True,
                        choices=["MARKET", "LIMIT"])

    parser.add_argument("--quantity", required=True,
                        type=float)

    parser.add_argument("--price",
                        type=float)

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        print("Price is required for LIMIT orders.")
        return

    trader = BinanceTrader()

    print("\n========== ORDER SUMMARY ==========")

    print(f"Symbol : {args.symbol}")
    print(f"Side   : {args.side}")
    print(f"Type   : {args.type}")
    print(f"Qty    : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price  : {args.price}")

    print("===================================\n")

    try:

        response = trader.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder Successful\n")

        print("Order ID :", response.get("orderId"))

        print("Status :", response.get("status"))

        print("Executed Qty :", response.get("executedQty"))

        print("Average Price :", response.get("avgPrice"))

    except Exception as e:

        print("\nOrder Failed")

        print(e)


if __name__ == "__main__":
    main()