import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def loadWine(url):
#loading dataset, no need to use dropna due to no na values
        whitedf = (
            pd.read_excel(url)
           
        )
    
        return whitedf
#removes outliers using IQR
def removeOut(whitedf):
    Q1 = whitedf.quantile(0.25)
    Q3 = whitedf.quantile(0.75)
    IQR = Q3 - Q1
    whitedfout = whitedf[~((whitedf < (Q1 - 1.5 * IQR)) |(whitedf > (Q3 + 1.5 * IQR))).any(axis=1)] 
    return whitedfout

