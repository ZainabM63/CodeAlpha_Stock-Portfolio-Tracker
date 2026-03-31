# Stock Portfolio Tracker

A simple pyhton-Flask web application for tracking stock portfolio holdings with CSV export functionality.

## Features

- **Add Stocks**: Select from predefined stocks and specify quantity
- **View Portfolio**: Display current holdings with quantities and subtotals
- **Total Calculation**: Automatic grand total of all holdings
- **Export to CSV**: Download portfolio data as CSV file
- **Reset Portfolio**: Clear all holdings

## Predefined Stocks

| Symbol | Price |
|--------|-------|
| AAPL   | $180  |
| TSLA   | $250  |
| GOOGL  | $140  |
| MSFT   | $400  |
| AMZN   | $3300 |
| NFLX   | $500  |

## Installation

```bash
pip install flask
```

## Usage

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Project Structure

```
├── app.py              # Python-Flask backend
├── portfolio.csv       # Data storage (auto-created)
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```