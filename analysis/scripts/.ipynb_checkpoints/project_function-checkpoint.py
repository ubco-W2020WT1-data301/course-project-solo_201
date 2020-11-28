import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def loadWine(url):
#loading dataset, no need to use dropna due to no na values
#Removing any duplicate rows 
        whitedf = (
            pd.read_excel(url)
            )
        whitedf = (
            whitedf
            .drop_duplicates()
            .reset_index(drop = True)
         )
        return whitedf
#removes outliers using IQR

def newDF(df):
    
        df['fixed_citric'] = df['fixed acidity']*0.5 + df['citric acid']*0.5
        df['volatile_totalSulfur'] = df['volatile acidity']*0.5 + df['total sulfur dioxide']*0.5
        df['residual_density'] = df['residual sugar']*0.5 + df['density']*0.5
        df['chlorides_density'] = df['chlorides']*0.5 + df['density']*0.5
        df['freeSulfur_totalSulfur'] = df['free sulfur dioxide']*0.5 + df['total sulfur dioxide']*0.5
        df['pH_sulphates'] = df['pH']*0.5 + df['sulphates']*0.5
        df['sulphates_totalSulfur'] = df['sulphates']*0.5 + df['total sulfur dioxide']*0.5
        df['alcohol_volatile'] = df['alcohol']*0.5 + df['volatile acidity']*0.5
        
        return df

    





def removeOut(whitedf):
    Q1 = whitedf.quantile(0.25)
    Q3 = whitedf.quantile(0.75)
    IQR = Q3 - Q1
    whitedfout = whitedf[~((whitedf < (Q1 - 1.5 * IQR)) |(whitedf > (Q3 + 1.5 * IQR))).any(axis=1)] 
    whitedfout = whitedfout.reset_index(drop = True)
    return whitedfout

