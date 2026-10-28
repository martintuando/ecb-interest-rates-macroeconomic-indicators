# ECB Interest Rates and Macroeconomic Indicators

Economic models such as the Phillips curve and the Taylor rule describe relationships between inflation, economic activity and monetary policy. I wanted to explore these relationships using real-world data and see how different macroeconomic indicators are statistically related to the ECB deposit facility rate.

## Analysis

Using monthly data from the ECB and FRED, I examined the relationships between the deposit facility rate and seven macroeconomic indicators:

- HICP and core inflation
- Unemployment
- Industrial production
- Brent crude oil prices
- EUR/USD exchange rate
- Economic sentiment

The analysis includes time-series visualizations, correlation matrices, correlations across different time horizons, and a multiple OLS regression. I also compared correlations in data levels with correlations in monthly changes and used HAC/Newey-West standard errors for the regression.

## Key Results

### Time-Series Visualizations

The development of selected macroeconomic indicators over time, normalized to the first observation.

![Inflation, Unemployment and EUR/USD](images/inflation_unemployment_eurusd.png)

### Lagged Correlations

Correlation heatmaps comparing relationships in data levels and monthly changes across different time horizons.

![Lagged Correlations in Levels](images/lag_correlations_levels.png)

![Lagged Correlations in Monthly Changes](images/lag_correlations_changes.png)

### OLS Regression

Regression results for the ECB deposit facility rate using seven macroeconomic indicators, with HAC/Newey-West standard errors.
![OLS Regression with HAC Standard Errors](images/ols_hac_results.png)

### Interest Rate Persistence

The ECB deposit facility rate exhibits strong temporal persistence. Across the sample, 82.3% of monthly observations show no change from the previous month. The autocorrelation is 0.994 at a one-month lag and remains high at 0.970 over three months, before declining to 0.904 at six months and 0.729 at twelve months. These results highlight the gradual adjustment of the policy rate and the importance of accounting for its historical level when analyzing its relationship with macroeconomic indicators. While inflation, unemployment and other indicators provide relevant economic context, their ability to explain the rate is limited by the persistence of monetary policy and other factors not captured by the model. This also motivates the subsequent forecasting project, which examines whether including the current interest rate improves predictions beyond what macroeconomic indicators alone can achieve.
## Project Structure

```text
├── raw_data/                  # Original datasets
├── data/                      # Processed datasets and macro_data.csv
├── images/                    # Figures used in the README
├── 01_data_preparation.py     # Data cleaning and preparation
├── 02_analysis.py             # Visualizations and empirical analysis
└── README.md
```

## Data Sources

- [ECB Data Portal](https://data.ecb.europa.eu/)
- [FRED – Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/)

## Tools

Python · pandas · Matplotlib · statsmodels · NumPy