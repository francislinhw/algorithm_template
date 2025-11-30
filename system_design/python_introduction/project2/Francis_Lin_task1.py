import backtrader as bt
import pandas as pd


class FlexibleCSVFeed(bt.feeds.GenericCSVData):

    def __init__(self, dataname, **kwargs):
        super().__init__(dataname=dataname, **kwargs)
        self.path = dataname
        self.csv_format = self._identify_format()

    # -----------------------------------------------------------
    # Identify CSV type
    # -----------------------------------------------------------
    def _identify_format(self):
        preview = pd.read_csv(self.path, nrows=5)

        if "Unnamed: 0" in preview.columns:
            # Example: 002054.XSHE.csv
            return "type_1"

        if "Date" in preview.columns and "High" in preview.columns:
            # Example: aapl.csv
            return "type_2"

        if "Date" in preview.columns and "Hour_of_Day" in preview.columns:
            # Example: ERCOTDA_price.csv
            return "type_3"

        raise ValueError("Unrecognized CSV schema. Unable to classify input file.")

    # -----------------------------------------------------------
    # Load data based on CSV type
    # -----------------------------------------------------------
    def load_preprocessed(self):
        if self.csv_format == "type_1":
            # Format: Unnamed:0 used as datetime
            df = pd.read_csv(self.path, parse_dates=["Unnamed: 0"])
            df.rename(columns={"Unnamed: 0": "datetime"}, inplace=True)

        elif self.csv_format == "type_2":
            # Standard OHLCV data with Date column
            df = pd.read_csv(self.path, parse_dates=["Date"])
            df.rename(columns={"Date": "datetime"}, inplace=True)

        elif self.csv_format == "type_3":
            # ERCOT hourly pricing data (Date + Hour_of_Day)
            df = pd.read_csv(self.path)
            df["datetime"] = pd.to_datetime(
                df["Date"]
                + " "
                + df["Hour_of_Day"].astype(str).replace("24", "0")
                + ":00:00"
            )
            df.loc[df["Hour_of_Day"] == 24, "datetime"] += pd.Timedelta(days=1)

        else:
            raise ValueError("Unsupported CSV format detected.")

        # Sorting and preparing dataframe
        df.sort_values("datetime", inplace=True)
        df.set_index("datetime", inplace=True)
        return df


file_to_test = "system_design/python_introduction/project2/ERCOTDA_price.csv"

feed = FlexibleCSVFeed(dataname=file_to_test)
processed_df = feed.load_preprocessed()

print(processed_df.head())
