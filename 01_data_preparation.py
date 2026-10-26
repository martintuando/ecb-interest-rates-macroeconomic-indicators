"""
01_data_preparation.py

Prepares monthly macroeconomic datasets for the ECB Interest Rate Decisions project.
"""

from pathlib import Path
import pandas as pd

RAW = Path("data/raw_data")
PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)

# ============================================================
# Brent Oil Price
# ============================================================

brent = pd.read_csv(RAW / "DCOILBRENTEU.csv")
brent["observation_date"] = pd.to_datetime(brent["observation_date"])
brent["month"] = brent["observation_date"].dt.to_period("M")

brent_monthly = (
    brent.groupby("month")["DCOILBRENTEU"]
    .mean()
    .reset_index()
    .rename(columns={"month": "date", "DCOILBRENTEU": "Brent_Oil_Price"})
)

brent_monthly.to_csv(PROCESSED / "brent_monthly.csv", index=False)

# ============================================================
# EUR/USD Exchange Rate
# ============================================================

exchange_rate = pd.read_csv(RAW / "DEXUSEU.csv")
exchange_rate["observation_date"] = pd.to_datetime(exchange_rate["observation_date"])
exchange_rate["month"] = exchange_rate["observation_date"].dt.to_period("M")

exchange_rate_monthly = (
    exchange_rate.groupby("month")["DEXUSEU"]
    .mean()
    .reset_index()
    .rename(columns={"month": "date", "DEXUSEU": "EUR_USD"})
)

exchange_rate_monthly.to_csv(PROCESSED / "exchange_rate.csv", index=False)

# ============================================================
# ECB Deposit Facility Rate
# ============================================================

ecb_rate = pd.read_csv(RAW / "ECB Data Portal_20260727113020.csv")

ecb_rate = ecb_rate[[
    "DATE",
    "Deposit facility - date of changes (raw data) - Level (FM.B.U2.EUR.4F.KR.DFR.LEV)"
]]

ecb_rate = ecb_rate.rename(columns={
    "DATE": "date",
    "Deposit facility - date of changes (raw data) - Level (FM.B.U2.EUR.4F.KR.DFR.LEV)": "ECB_Deposit_Rate"
})

ecb_rate["date"] = pd.to_datetime(ecb_rate["date"])
ecb_rate["month"] = ecb_rate["date"].dt.to_period("M")
ecb_rate = ecb_rate.sort_values("date")

ecb_rate = (
    ecb_rate.groupby("month")["ECB_Deposit_Rate"]
    .last()
    .to_frame()
)

all_months = pd.period_range(
    ecb_rate.index.min(),
    ecb_rate.index.max(),
    freq="M"
)

ecb_rate = ecb_rate.reindex(all_months)
ecb_rate["ECB_Deposit_Rate"] = ecb_rate["ECB_Deposit_Rate"].ffill()

ecb_rate = ecb_rate.reset_index().rename(columns={"index": "date"})

ecb_rate.to_csv(PROCESSED / "ecb_rate.csv", index=False)

# ============================================================
# Inflation
# ============================================================

inflation = pd.read_csv(RAW / "ECB Data Portal_20260727160328.csv")

inflation = inflation.drop(columns=["TIME PERIOD"])
inflation = inflation.iloc[37:].reset_index(drop=True)

inflation = inflation.rename(columns={
    "DATE": "date",
    "HICP Inflation rate - Total - Annual rate of change (HICP.M.U2.N.000000.4D0.ANR)": "Inflation_HICP",
    "HICP Inflation rate - Total excluding energy, food, alcohol and tobacco - Annual rate of change (HICP.M.U2.N.XEF000.4D0.ANR)": "Core_Inflation"
})

inflation["date"] = pd.to_datetime(inflation["date"])

inflation.to_csv(PROCESSED / "inflation.csv", index=False)

# ============================================================
# Industrial Production
# ============================================================

industrial = pd.read_csv(
    RAW / "ECB Data Portal_20260727172824.csv"
)

industrial = industrial.drop(columns=["TIME PERIOD"])

industrial = industrial.rename(columns={
    "Total industrial production (excluding construction) - Working day and seasonally adjusted (STBS.M.I10.Y.PROD.NS0020.4D0.N.IX)": "Industrial"
})

industrial["DATE"] = pd.to_datetime(industrial["DATE"])

industrial = industrial.rename(columns={
    "DATE": "date"
})

# Remove metadata/empty rows before actual observations
industrial = industrial.iloc[108:]

industrial.to_csv(
    PROCESSED / "industrial.csv",
    index=False
)

# ============================================================
# Unemployment Rate
# ============================================================

unemployment = pd.read_csv(
    RAW / "ECB Data Portal_20260727165304.csv"
)

unemployment = unemployment.drop(columns=["TIME PERIOD"])

unemployment = unemployment.rename(columns={
    "Unemployment rate, age 15 to 74, total (LFSI.M.I10.S.UNEHRT.TOTAL0.15_74.T)": "Unemployment"
})

unemployment["DATE"] = pd.to_datetime(unemployment["DATE"])

unemployment = unemployment.rename(columns={
    "DATE": "date"
})

unemployment.to_csv(
    PROCESSED / "unemployment.csv",
    index=False
)

# ============================================================
# Economic Sentiment Indicator
# ============================================================

economic_sentiment = pd.read_csv(
    RAW / "economic_sentiment.csv"
)

economic_sentiment = economic_sentiment[
    ["TIME_PERIOD", "OBS_VALUE"]
]

economic_sentiment = economic_sentiment.rename(columns={
    "TIME_PERIOD": "date",
    "OBS_VALUE": "Economic_Sentiment"
})

economic_sentiment["date"] = pd.to_datetime(economic_sentiment["date"])

economic_sentiment.to_csv(
    PROCESSED / "economic_sentiment.csv",
    index=False
)