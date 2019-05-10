import pandas as pd
import lxml

global monthly_totals = pd.DataFrame()

def add_data (url, month):
    dfs = pd.read_html(url)
    units = dfs[1]["Est. units"].sum()
    df = pd.DataFrame({'Month': [month], 'Total Units': [units]})
    monthly_totals.append(df, ignore_index=True)
    print(monthly_totals)

add_data("https://www.comichron.com/monthlycomicssales/2008/2008-01.html", "January 2008")