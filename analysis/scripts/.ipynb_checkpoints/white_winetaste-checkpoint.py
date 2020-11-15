#method contains all the columns that have a effect on wine taste 
def tasteWhite(url):
#loading dataset, no need to use dropna due to no na values
        whitedf = (
            pd.read_excel(url)
           
        )

#method chain 2  dropping columns
        whitedf2 = (
                    whitedf
                   
                    .drop(columns =['free sulfur dioxide','total sulfur dioxide','alcohol','sulphates', 'density'])
                    )
        return whitedf2
