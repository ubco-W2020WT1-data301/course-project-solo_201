def noTasteRed(url):
    #loading dataset, no need to use dropna due to no na values
        reddf = (
            pd.read_excel(url)
           
        )

#method chain 2  dropping columns
        reddf2 = (
                    reddf
                   
                    .drop(columns =['fixed acidity','volatile acidity','citric acid','residual sugar','chloride','pH'])
                    )
        return reddf2