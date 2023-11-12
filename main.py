import pandas as pd
from lm import *


def read():
    """Reads the data from the dataset and returns a dataframe with the information"""

    path = "C:\\Users\\arnau\\DADES\\datathon\\Datathon23\\consumo_material_clean.xlsx" #Warnign! Must modify path
    return pd.read_excel(path)    


def filterxhospital(df):
    """Returns a dictionary with the dataframes filtered by each hospital"""

    codes = df["ORIGEN"].unique().tolist()
    codes = [code.split("-") for code in codes]
    codes = set([code[0]+"-"+code[1] for code in codes])
    df[["REGION", "HOSPITAL", "DEPARTAMENTO", "NONE"]] = df["ORIGEN"].str.split("-",expand=True)
    df[["DAY", "MONTH", "YEAR"]] = df["FECHAPEDIDO"].str.split("/",expand=True)
    df=df.drop(columns=["DEPARTAMENTO","NONE","REFERENCIA","PRECIO","TIPOCOMPRA", "TGL", "ORIGEN","FECHAPEDIDO","NUMERO"])
    return df  


def main():
    df = read()
    codenames = code_name(df)
    df = filterxhospital(df)
    predicted_purchases = modelate(df)
    #predicted_purchases.to_excel("Predicted_purchases.xlsx") #save predicted purchases to excel
    #plot_differences(predicted_purchases) #get the plot
    #sample(predicted_purchases) #uncomment for getting precise data (filtered by hospital and item)

if __name__ == "__main__":
    main()