from flask import Flask, render_template, request, redirect, send_file, make_response
import csv
import os

app = Flask(__name__)

# Hardcoded Stock Prices (Task Requirement)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 3300,"NFLX": 500
}

@app.route('/')
def index():
    # Load current portfolio from CSV to display on the page
    rows = []
    total = 0
    if os.path.exists('portfolio.csv'):
        with open('portfolio.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
                total += float(row['Total'])
    return render_template('index.html', stocks=STOCK_PRICES, portfolio=rows, grand_total=total)

@app.route('/add', methods=['POST'])
def add_stock():
    symbol = request.form.get('symbol', '')
    quantity = int(request.form.get('quantity', 1))
    price = STOCK_PRICES.get(symbol, 0)
    subtotal = quantity * price

    file_exists = os.path.isfile('portfolio.csv')
    with open('portfolio.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Symbol', 'Quantity', 'Price', 'Total'])
        writer.writerow([symbol, quantity, price, subtotal])
    
    response = make_response(redirect('/'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/export')
def export_csv():
    path = "portfolio.csv"
    if os.path.exists(path):
        return send_file(path, 
                         mimetype='text/csv',
                         as_attachment=True,
                         download_name='my_portfolio.csv')
    else:
        return "No data to export yet!", 404

@app.route('/clear', methods=['POST'])
def clear_portfolio():
    if os.path.exists('portfolio.csv'):
        os.remove('portfolio.csv')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
