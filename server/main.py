from ibapi.client import EClient  # needs to be inherited
from ibapi.wrapper import EWrapper  # needs to be inherited
from ibapi.contract import Contract
from ibapi.order import Order

import os
from dotenv import load_dotenv
import pandas as pd
import time
load_dotenv()

class PortfolioApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.pos_df = pd.DataFrame(
            columns=[
                "Account",
                "Symbol",
                "SecType",
                "Currency",
                "Position",
                "Avg cost",
                "ConId",
                "ReqId",
                "UnrealizedPnL",
            ]
        )
    def get_all_positions_with_pnl(self, account_number, connection_port):
        position_df_pnl = pd.DataFrame(
            columns=[
                "Account",
                "Symbol",
                "SecType",
                "Currency",
                "Position",
                "Avg cost",
                "ConId",
                "ReqId",
                "UnrealizedPnL",
            ]
        )
        self.connect(host='127.0.1.1' , port=7496, clientId=0)

        if not self.isConnected():
            print('Connection failed')
        else:
            print('connection successful')
            self.reqPositions()
            time.sleep(2)
            position_df_pnl = self.pos_df
            print(position_df_pnl)


def main():
    ACCOUNT_NUMBER = os.environ.get("ACCOUNT_NUMBER")
    CONNECTION_PORT = os.environ.get("CONNECTION_PORT")

    app = PortfolioApp()
    app.get_all_positions_with_pnl(ACCOUNT_NUMBER, CONNECTION_PORT)



if __name__ == "__main__":
  	main()