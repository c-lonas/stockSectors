from django.shortcuts import render

# import numpy as np
# import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio
from pandas_datareader import data as pdr

#initalize base layout variable
layout = {
        "title": "Update Layout With Graph Title",
        "title_x": 0.5, 
        "paper_bgcolor": "rgba(44, 42, 39, 0.85)", 
        "plot_bgcolor" : "rgba(44, 42, 39, 0.01)",
        "font": {"family": "Raleway"},
        "font_color": "white",
        "font_size": 22,
        "width": 1000,
        "height": 650,
        "xaxis": {
            "type": "date", 
            "rangeslider": {"visible": True}, 
            "rangeselector": {"buttons": [
                {
                "step": "month", 
                "count": 1, 
                "label": "1m", 
                "stepmode": "backward",
                },
                {
                "step": "month", 
                "count": 3, 
                "label": "3m", 
                "stepmode": "backward",
                },  
                {
                "step": "month", 
                "count": 6, 
                "label": "6m", 
                "stepmode": "backward"
                }, 
                {
                "step": "year", 
                "count": 1, 
                "label": "1y", 
                "stepmode": "backward"
                },
                {
                "step": "year", 
                "count": 3, 
                "label": "3y", 
                "stepmode": "backward"
                },
                {
                "step": "year", 
                "count": 5, 
                "label": "5y", 
                "stepmode": "backward"
                },
                {
                "step": "year", 
                "count": 10, 
                "label": "10y", 
                "stepmode": "backward"
                },
                {
                "step": "year", 
                "count": 20, 
                "label": "20y", 
                "stepmode": "backward"
                },
                {
                "step": "year", 
                "count": 30, 
                "label": "30y", 
                "stepmode": "backward",
                },            
                {"step": "all"}
            ]},
            "rangeselector_bgcolor": "white",
            "rangeselector_activecolor": "rgb(241, 255, 41)",
            "rangeselector_font": {
                "color": "rgba(44, 42, 39, 0.9)",
                "size": 22,
            }

        },
    }



# Routing

def index(request):
    context = {
        "MainFigure": main_graph(),
    }
    return render(request, 'index.html', context)

def tech(request):
    context = {
        "TechFigure": techTrace(),
    }
    return render(request, 'techsector.html', context)

def fin(request):
    context = {
        "FinFigure": financeTrace(),
    }
    return render(request, 'finsector.html', context)

def real(request):
    context = {
        "RealFigure": realEstateTrace(),
    }
    return render(request, 'realsector.html', context)

def health(request):
    context = {
        "HealthFigure": healthCareTrace(),
    }
    return render(request, 'healthsector.html', context)

def industry(request):
    context = {
        "IndustryFigure": industryTrace(),
    }
    return render(request, 'industrysector.html', context)

def crypto(request):
    context = {
        "CryptoFigure": cryptoTrace(),
    }
    return render(request, 'cryptosector.html', context)


# Create Graphs

def main_graph():
    spData = yf.download(tickers='^GSPC', period='max', interval="1d")

    data = go.Scatter(
        type = "scatter",
        name = "S&P 500",
        # line = {"color": "rgb(239, 250, 92)"},
        y = spData["Adj Close"],
        x = spData["Adj Close"].index,
    )

    # Initialize Figure
    mainFig = go.Figure(data, layout)
    mainFig.update_layout({"title_text": "Indices"})

    # Update with traces from additional indexes
    mainFig = indexTraces(mainFig)

    mainFig = pio.to_html(
            mainFig, full_html=False,
            include_plotlyjs="cdn",
            )

    return mainFig


def indexTraces(fig):
    DJI = yf.download(tickers='^DJI', period='max', interval="1d")
    IXIC = yf.download(tickers='^IXIC', period='max', interval="1d")
    RUT = yf.download(tickers='^RUT', period='max', interval="1d")
    NYSE = yf.download(tickers='^NYA', period='max', interval="1d")

    fig.add_trace(go.Scatter(
        type = "scatter",
        name = "Dow 30",
        # line = {"color": ""},
        y = DJI["Adj Close"],
        x = DJI["Adj Close"].index,
    ))

    fig.add_trace(go.Scatter(
        type = "scatter",
        name = "Nasdaq",
        y = IXIC["Adj Close"],
        x = IXIC["Adj Close"].index,
    ))

    fig.add_trace(go.Scatter(
        type = "scatter",
        name = "Russel 2000",
        y = RUT["Adj Close"],
        x = RUT["Adj Close"].index,
    ))

    fig.add_trace(go.Scatter(
        type = "scatter",
        name = "NYSE",
        y = NYSE["Adj Close"],
        x = NYSE["Adj Close"].index,
    ))

    return (fig)


def techTrace():

    AAPL = yf.download(tickers='AAPL', period='max', interval="1d")
    GOOG = yf.download(tickers='GOOG', period='max', interval="1d")
    AMZN = yf.download(tickers='AMZN', period='max', interval="1d")
    TSLA = yf.download(tickers='TSLA', period='max', interval="1d")
    FB = yf.download(tickers='FB', period='max', interval="1d")
    NVDA = yf.download(tickers='NVDA', period='max', interval="1d")
    IBM = yf.download(tickers='IBM', period='max', interval="1d")
    MSFT = yf.download(tickers='MSFT', period='max', interval="1d")
    ADBE = yf.download(tickers='ADBE', period='max', interval="1d")
    INTC = yf.download(tickers='INTC', period='max', interval="1d")


    # Trace 0
    googData = go.Scatter(
        type = "scatter",
        name = "Google",
        y = GOOG["Adj Close"],
        x = GOOG["Adj Close"].index,
    )

    TechFigure = go.Figure(googData, layout)

    # Trace 1
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Apple",
        y = AAPL["Adj Close"],
        x = AAPL["Adj Close"].index,
    ))

    # Trace 2
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Amazon",
        y = AMZN["Adj Close"],
        x = AMZN["Adj Close"].index,
    ))

    # Trace 3
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Tesla",
        y = TSLA["Adj Close"],
        x = TSLA["Adj Close"].index,
    ))

    # Trace 4
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Facebook",
        y = FB["Adj Close"],
        x = FB["Adj Close"].index,
    ))

    # Trace 5
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Nvidia",
        y = NVDA["Adj Close"],
        x = NVDA["Adj Close"].index,
    ))

    # Trace 6
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "IBM",
        y = IBM["Adj Close"],
        x = IBM["Adj Close"].index,
    ))

    # Trace 7
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Microsoft",
        y = MSFT["Adj Close"],
        x = MSFT["Adj Close"].index,
    ))

    # Trace 8
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Adobe",
        y = ADBE["Adj Close"],
        x = ADBE["Adj Close"].index,
    ))

    # Trace 9
    TechFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Intel",
        y = INTC["Adj Close"],
        x = INTC["Adj Close"].index,
    ))

    TechFigure.update_layout({"title_text": "Tech"})

    TechFigure = pio.to_html(
            TechFigure, full_html=False,
            include_plotlyjs="cdn",
            )

    return TechFigure



def realEstateTrace():
    AMT = yf.download(tickers='AMT', period='max', interval="1d")
    ARE = yf.download(tickers='ARE', period='max', interval="1d")
    EXR = yf.download(tickers='EXR', period='max', interval="1d")
    CUBE = yf.download(tickers='CUBE', period='max', interval="1d")
    INVH = yf.download(tickers='INVH', period='max', interval="1d")
    REG = yf.download(tickers='REG', period='max', interval="1d")
    SPG = yf.download(tickers='SPG', period='max', interval="1d")
    DLR = yf.download(tickers='DLR', period='max', interval="1d")
    PLD = yf.download(tickers='PLD', period='max', interval="1d")
    JLL = yf.download(tickers='JLL', period='max', interval="1d")

    # Trace 0
    data = go.Scatter(
        type = "scatter",
        name = "American Tower Corp",
        y = AMT["Adj Close"],
        x = AMT["Adj Close"].index,
    )

    RealFigure = go.Figure(data, layout)

    # Trace 1
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Alexandria",
        y = ARE["Adj Close"],
        x = ARE["Adj Close"].index,
    ))

    # Trace 2
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Extra Space Storage",
        y = EXR["Adj Close"],
        x = EXR["Adj Close"].index,
    ))

    # Trace 3
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "CubeSmart",
        y = CUBE["Adj Close"],
        x = CUBE["Adj Close"].index,
    ))

    # Trace 4
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Invitation Homes",
        y = INVH["Adj Close"],
        x = INVH["Adj Close"].index,
    ))

    # Trace 5
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Regency Centers",
        y = REG["Adj Close"],
        x = REG["Adj Close"].index,
    ))

    # Trace 6
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Simon Property Group",
        y = SPG["Adj Close"],
        x = SPG["Adj Close"].index,
    ))

    # Trace 7
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Digital Realty Trust",
        y = DLR["Adj Close"],
        x = DLR["Adj Close"].index,
    ))

    # Trace 8
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Prologis",
        y = PLD["Adj Close"],
        x = PLD["Adj Close"].index,
    ))

    # Trace 9
    RealFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Jones Lang LaSalle",
        y = JLL["Adj Close"],
        x = JLL["Adj Close"].index,
    ))

    RealFigure.update_layout({"title_text": "Real Estate"})

    RealFigure = pio.to_html(
            RealFigure, full_html=False,
            include_plotlyjs="cdn",
            )

    return RealFigure


def healthCareTrace():

    UNH = yf.download(tickers='UNH', period='max', interval="1d")
    VRTX = yf.download(tickers='VRTX', period='max', interval="1d")
    PFE = yf.download(tickers='PFE', period='max', interval="1d")
    MRK = yf.download(tickers='MRK', period='max', interval="1d")
    INCY = yf.download(tickers='INCY', period='max', interval="1d")
    SGEN = yf.download(tickers='SGEN', period='max', interval="1d")
    TMO = yf.download(tickers='TMO', period='max', interval="1d")
    TDOC = yf.download(tickers='TDOC', period='max', interval="1d")
    ANTM = yf.download(tickers='ANTM', period='max', interval="1d")
    CVS = yf.download(tickers='CVS', period='max', interval="1d")

    # Trace 0
    data = go.Scatter(
        type = "scatter",
        name = "UnitedHealth Group",
        y = UNH["Adj Close"],
        x = UNH["Adj Close"].index,
    )

    HealthFigure = go.Figure(data, layout)

    # Trace 1
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Vertex",
        y = VRTX["Adj Close"],
        x = VRTX["Adj Close"].index,
    ))

    # Trace 2
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Pfizer",
        y = PFE["Adj Close"],
        x = PFE["Adj Close"].index,
    ))

    # Trace 3
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Merck & Co.",
        y = MRK["Adj Close"],
        x = MRK["Adj Close"].index,
    ))

    # Trace 4
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Incyte Corp",
        y = INCY["Adj Close"],
        x = INCY["Adj Close"].index,
    ))

    # Trace 5
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Seagen",
        y = SGEN["Adj Close"],
        x = SGEN["Adj Close"].index,
    ))

    # Trace 6
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Thermo Fisher Scientific",
        y = TMO["Adj Close"],
        x = TMO["Adj Close"].index,
    ))

    # Trace 7
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Teladoc",
        y = TDOC["Adj Close"],
        x = TDOC["Adj Close"].index,
    ))

    # Trace 8
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Anthem",
        y = ANTM["Adj Close"],
        x = ANTM["Adj Close"].index,
    ))

    # Trace 9
    HealthFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "CVS",
        y = CVS["Adj Close"],
        x = CVS["Adj Close"].index,
    ))

    HealthFigure.update_layout({"title_text": "Health Care"})

    HealthFigure = pio.to_html(
            HealthFigure, full_html=False,
            include_plotlyjs="cdn",
            )

    return HealthFigure

def financeTrace():

    VOO = yf.download(tickers='VOO', period='max', interval="1d")
    VISA = yf.download(tickers='V', period='max', interval="1d")
    MA = yf.download(tickers='MA', period='max', interval="1d")
    JPM = yf.download(tickers='JPM', period='max', interval="1d")
    PYPL = yf.download(tickers='PYPL', period='max', interval="1d")
    BRKB = yf.download(tickers='BRK-B', period='max', interval="1d")
    SQSP = yf.download(tickers='SQSP', period='max', interval="1d")
    HOOD = yf.download(tickers='HOOD', period='max', interval="1d")
    BTC = yf.download(tickers='BTC-USD', period='max', interval="1d")
    ETH = yf.download(tickers='ETH-USD', period='max', interval="1d")


    # Trace 0
    vooData = go.Scatter(
        type = "scatter",
        name = "Vanguard ETF",
        y = VOO["Adj Close"],
        x = VOO["Adj Close"].index,
    )

    FinFigure = go.Figure(vooData, layout)


    FinFigure.update_layout({"title_text": "Finance"})

    # Trace 1
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Mastercard",
        y = MA["Adj Close"],
        x = MA["Adj Close"].index,
    ))

    # Trace 2
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Visa",
        y = VISA["Adj Close"],
        x = VISA["Adj Close"].index,
    ))

    # Trace 3
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "JPMorgan Chase",
        y = JPM["Adj Close"],
        x = JPM["Adj Close"].index,
    ))

    # Trace 4
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "PayPal",
        y = PYPL["Adj Close"],
        x = PYPL["Adj Close"].index,
    ))

    # Trace 5
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Berkshire Hathaway (B)",
        y = BRKB["Adj Close"],
        x = BRKB["Adj Close"].index,
    ))

    # Trace 6
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Squarespace",
        y = SQSP["Adj Close"],
        x = SQSP["Adj Close"].index,
    ))

    # Trace 7
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Robinhood",
        y = HOOD["Adj Close"],
        x = HOOD["Adj Close"].index,
    ))

    # Trace 8
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Bitcoin",
        y = BTC["Adj Close"],
        x = BTC["Adj Close"].index,
        visible = "legendonly",
    ))

    # Trace 9
    FinFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Etherium",
        y = ETH["Adj Close"],
        x = ETH["Adj Close"].index,
        visible = "legendonly",
    ))


    FinFigure = pio.to_html(
            FinFigure, full_html=False,
            include_plotlyjs="cdn",
            )
    return FinFigure

def industryTrace():

    AIT = yf.download(tickers='AIT', period='max', interval="1d")
    RTX = yf.download(tickers='RTX', period='max', interval="1d")
    LMT = yf.download(tickers='LMT', period='max', interval="1d")
    PCAR = yf.download(tickers='PCAR', period='max', interval="1d")
    GE = yf.download(tickers='GE', period='max', interval="1d")
    TEX = yf.download(tickers='TEX', period='max', interval="1d")
    GNRC = yf.download(tickers='GNRC', period='max', interval="1d")
    ACM = yf.download(tickers='ACM', period='max', interval="1d")
    J = yf.download(tickers='J', period='max', interval="1d")
    MTZ = yf.download(tickers='MTZ', period='max', interval="1d")


    # Trace 0
    aitData = go.Scatter(
        type = "scatter",
        name = "Applied Industrial Tech",
        y = AIT["Adj Close"],
        x = AIT["Adj Close"].index,
    )

    IndustryFigure = go.Figure(aitData, layout)


    IndustryFigure.update_layout({"title_text": "Industry"})

    # Trace 1
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Raytheon",
        y = RTX["Adj Close"],
        x = RTX["Adj Close"].index,
    ))

    # Trace 2
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Lockheed Martin",
        y = LMT["Adj Close"],
        x = LMT["Adj Close"].index,
    ))

    # Trace 3
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Paccar",
        y = PCAR["Adj Close"],
        x = PCAR["Adj Close"].index,
    ))

    # Trace 4
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "General Electric",
        y = GE["Adj Close"],
        x = GE["Adj Close"].index,
    ))

    # Trace 5
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Terex",
        y = TEX["Adj Close"],
        x = TEX["Adj Close"].index,
    ))

    # Trace 6
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Generac",
        y = GNRC["Adj Close"],
        x = GNRC["Adj Close"].index,
    ))

    # Trace 7
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Aecom",
        y = ACM["Adj Close"],
        x = ACM["Adj Close"].index,
    ))

    # Trace 8
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Jacobs Engineering Group",
        y = J["Adj Close"],
        x = J["Adj Close"].index,
    ))

    # Trace 9
    IndustryFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "MasTec",
        y = MTZ["Adj Close"],
        x = MTZ["Adj Close"].index,
    ))

    IndustryFigure = pio.to_html(
            IndustryFigure, full_html=False,
            include_plotlyjs="cdn",
            )

    return IndustryFigure

def communicationsTrace():
    #function here
    return

def consumersTrace():
    #function here
    return

def cryptoTrace():
    #function here
    BTC = yf.download(tickers='BTC-USD', period='max', interval="1d")
    ETH = yf.download(tickers='ETH-USD', period='max', interval="1d")
    BNB = yf.download(tickers='BNB-USD', period='max', interval="1d")
    SOL = yf.download(tickers='SOL-USD', period='max', interval="1d")
    LUNA = yf.download(tickers='LUNA-USD', period='max', interval="1d")
    AVAX = yf.download(tickers='AVAX-USD', period='max', interval="1d")
    DOGE = yf.download(tickers='DOGE-USD', period='max', interval="1d")
    
    

    # Trace 0
    btcData = go.Scatter(
        type = "scatter",
        name = "Bitcoin",
        y = BTC["Adj Close"],
        x = BTC["Adj Close"].index,
    )

    CryptoFigure = go.Figure(btcData, layout)


    CryptoFigure.update_layout({"title_text": "Cryptocurrencies"})

    # Trace 1
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Etherium",
        y = ETH["Adj Close"],
        x = ETH["Adj Close"].index,
    ))

    # Trace 2
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Binance",
        y = BNB["Adj Close"],
        x = BNB["Adj Close"].index,
    ))

    # Trace 3
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Solana",
        y = SOL["Adj Close"],
        x = SOL["Adj Close"].index,
    ))

    # Trace 4
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Terra",
        y = LUNA["Adj Close"],
        x = LUNA["Adj Close"].index,
    ))

    # Trace 5
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Avalanche",
        y = AVAX["Adj Close"],
        x = AVAX["Adj Close"].index,
    ))

    # Trace 6
    CryptoFigure.add_trace(go.Scatter(
        type = "scatter",
        name = "Dogecoin",
        y = DOGE["Adj Close"],
        x = DOGE["Adj Close"].index,
    ))

    CryptoFigure = pio.to_html(
            CryptoFigure, full_html=False,
            include_plotlyjs="cdn",
            )
    return CryptoFigure