import yfinance as yf
from datetime import date, timedelta
import PySimpleGUI as sg

def fetch_stock_data(tickerSymbol):
    today = date.today()
    week = today - timedelta(days=7)
    week_str = week.strftime('%Y-%m-%d')

    # Get data for this ticker
    tickerData = yf.Ticker(tickerSymbol)
    
    tickerDf = tickerData.history(period='7d', start=week_str, end=today)

    # Calculate the percentage difference between the open and close prices of the most recent data point
    latest_open = tickerDf['Open'][-1]
    latest_close = tickerDf['Close'][-1]
    percentage_diff = (latest_close - latest_open) / latest_open * 100

    # Format the percentage difference to 2 decimal places
    formatted_diff = '{:.2f}'.format(percentage_diff)

    # Return the formatted percentage difference
    return formatted_diff

formatted_diff = fetch_stock_data('^FTSE')
print(formatted_diff)

#image path logic
if float(formatted_diff) > 0.2:
    image_path = r"images/happydog.png"
    text_data = f"Hell yes the index has gone up by {formatted_diff}%"
elif float(formatted_diff) < -0.2:
    image_path = "images/saddog.png"
    text_data = f"Mannn the index changed by {formatted_diff}%"
else:
    image_path = "images/dog.png"
    text_data = f"The index didnt change much today only {formatted_diff}%"


#gui
image_element = sg.Image(filename=image_path)

# Define the layout of your GUI using a list of lists
layout = [
    [image_element],
    [sg.Text(text_data,font=('Helvetica', 15), justification='center')]
]

# Create a window object using the sg.Window() method and pass in the layout you defined
window = sg.Window('Index Dog', layout, size=(500, 300), element_justification='center')

# Use a loop to read events from the window and respond to them
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
# Close the window when you're done with it
window.close()