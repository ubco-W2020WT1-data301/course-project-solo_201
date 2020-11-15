def noTasteWhite(url):
    #loading dataset, no need to use dropna due to no na values
        whitedf = (
            pd.read_excel(url)
           
        )

#method chain 2  dropping columns
        whitedf2 = (
                    whitedf
                   
                    .drop(columns =['fixed acidity','volatile acidity','citric acid','residual sugar','chloride','pH'])
                    )
        return whitedf2
    