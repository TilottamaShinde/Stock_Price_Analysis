This project analyzes historical stock price data using Python.
It fetches stock prices using the yfinance library, processes the data, and prepares it for further analysis or visualization.

***Features***

Fetch historical stock prices from Yahoo Finance

Analyze multiple stocks over a specific date range

Clean and structured code using modular Python files

Easy to extend for visualization or machine learning

***Technologies Used***

Python 3.x

pandas

yfinance

matplotlib (optional for plotting)

PyCharm (IDE)

***Installation Steps***

1. Clone Repositiry
      git clone https://github.com/your-username/stock-price-analysis.git
   
      cd stock-price-analysis

2. Create Virtual Environment:

    python3 -m venv .venv
   
source .venv/bin/activate  # For Mac/Linux



3. Install Required Libraries:

     pip install -r requirements.txt


***Project Structure***


Stock Price Analysis/

│
├── fetch_data.py        # Code to fetch stock data

├── main.py              # Entry point of the project

├── requirements.txt     # Python dependencies

├── .gitignore           # Files/Folders ignored by Git

└── README.md            # Project documentation



***Usage***

python main.py


