from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd


def code_name(df):
      """Returns a dictionary, linking the code of the product with its name"""

      rel = zip(df["CODIGO"].tolist(), df["PRODUCTO"].tolist())
      return {x[0]:x[1] for x in rel}


def sample(df):
      """Returns  a sample of the predicted purchases"""

      df = df.groupby(["CODIGO"]).apply(lambda x: x.reset_index(drop=True))
      df = df[df["CODIGO"]=="B41691"]  
      df = df[df["MONTH"]=="02"]  
      print(df)


def modelate(df):
      """Creates a model that fits the past data and predicts the 2023 purchases"""

      codenames = code_name(df)
      X = pd.get_dummies(df[["HOSPITAL","DAY","MONTH","YEAR","CODIGO"]], columns=["CODIGO"], prefix="CODIGO")
      y = df["CANTIDADCOMPRA"]
      train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.4, random_state=42)
      model = RandomForestRegressor(n_estimators=100, random_state=100)    
      model.fit(train_X, train_y)
      #predictions = model.predict(val_X)


      df2 = df[df["YEAR"]=="23"] #we get the 2023 dates to predict how many items need to be purchased
      X2 = pd.get_dummies(df2[["HOSPITAL","DAY","MONTH","YEAR","CODIGO"]], columns=["CODIGO"], prefix="CODIGO")
      y2 = df2["CANTIDADCOMPRA"]

      missing = set(X.columns) - set(X2.columns)
      for column in missing:
            X2[column] = False
      X2 = X2[X.columns]

      future_prediction = model.predict(X2)
      predframe = pd.DataFrame({
            "HOSPITAL": X2["HOSPITAL"], 
            "DAY": X2["DAY"],  
            "MONTH": X2["MONTH"],
            "AMOUNT": y2,
            "PREDICTEDAMOUNT": future_prediction
      })

      predframe = pd.concat([predframe, val_X.filter(like="CODIGO")], axis=1)
      predicted = predframe.groupby(["HOSPITAL"]).apply(lambda x: x.reset_index(drop=True))

      p = predicted.copy()
      p= p.drop(columns=["HOSPITAL","DAY","MONTH","AMOUNT", "PREDICTEDAMOUNT"])
      predicted["CODIGO"] = ((p == True).idxmax(axis=1))
      predicted = predicted[["CODIGO","DAY","MONTH","AMOUNT","PREDICTEDAMOUNT"]]
      predicted["CODIGO"] = predicted["CODIGO"].str.replace("CODIGO_","")
      predicted["PRODUCTO"] = [codenames[code] for code in predicted["CODIGO"].tolist()]
      predicted = predicted.sort_values(by=["HOSPITAL","CODIGO", "MONTH", "DAY"])
      
      return predicted


def plot_differences(df):
      df["ACC"] = df["AMOUNT"] - df["PREDICTEDAMOUNT"]
      dif = df["ACC"].to_list()
      #print(sum(dif)/len(dif)) #mean of the error
      fig, ax = plt.subplots()
      ax.plot(dif, linestyle='-', color='b', label='Prediction Errors')

      ax.set_title('Prediction Errors')
      ax.set_xlabel('Data Points')
      ax.set_ylabel('Error Values')

      plt.show()