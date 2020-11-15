def tasteRed(url):
    #loading dataset, no need to use dropna due to no na values
        reddf = (
            pd.read_excel(url)
           
        )

#method chain 2  dropping columns
        redf2 = (
                    reddf
                   
                    .drop(columns =['free sulfur dioxide','total sulfur dioxide','alcohol','sulphates', 'density'])
                    )
        return redf2