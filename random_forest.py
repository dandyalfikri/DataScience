import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

def load_data():

    df = pd.read_csv("update_mar_2021_kedaton.csv")
    #df.info()
    df['Umur'].fillna((df['Umur'].mean()), inplace=True)

    #Feature Engineering (Normalisasi)
    X = np.array(df['Budget_Rumah']).reshape(-1,1)
    scaling = MinMaxScaler()
    scaling.fit(X)
    X_scaled = scaling.transform(X)
    df['Budget_Rumah_Normalised'] = X_scaled.reshape(1,-1)[0]

    #Mengubah dtype object menjadi int64
    df.replace({'Rencana_Pembelian':{'Investasi':1,'Tinggal':2,'None':3}},inplace=True) 
    df.replace({'Metode_Pembayaran': {'Cash Bertahap':2,
                                  'KPR_Konfensional':1,'Cash Keras':3,'KPR_Syariah':4}},inplace=True)
    df.replace({'Nama_Cluster':{'Kedaton Terrace':1,'Kedaton Park':2,'Kedaton Pavilliun':3}},inplace=True)



    data = df[['Umur','Rencana_Pembelian','Luas_Tanah','Luas_Bangunan','Jumlah_Lantai','Budget_Rumah_Normalised','Metode_Pembayaran','Nama_Cluster']].copy()
    X = data.drop(['Nama_Cluster'],axis=1).copy()
    y = data['Nama_Cluster'].copy()
    budget_norm=df['Budget_Rumah']

    return X, y,budget_norm


def fitting(data):
    X,y,budget_norm = load_data()
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,
                                                    random_state=90)
    clf = RandomForestClassifier(max_depth=None,max_features=4,
                                min_samples_leaf=1,min_samples_split=5,
                                n_estimators=10, random_state=90)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
   # print("Accuracy: ",metrics.accuracy_score(y_test, y_pred)*100)
   # print(confusion_matrix(y_test, y_pred))
   # print(classification_report(y_test, y_pred))

    new_input=data 
  
  #  '''
    print("Data yang di input")
    print(new_input)
    
    br_s = np.array(budget_norm).reshape(-1,1)
    X_scaled_new = np.append(br_s,new_input[0][6]).reshape(-1,1)
    scaling = MinMaxScaler()
    scaling.fit(X_scaled_new)
    X_scaled = scaling.transform(X_scaled_new)
    len(X_scaled)
    new_input[0][6] = str(float(X_scaled[-1]))

    print("new input = ",new_input)

    new_output = clf.predict(new_input).tolist()
    print("Rumah yang cocok untuk anda:")
    print(new_output)
    data = {
        'input':new_input,
        'output':new_output
    }
   # '''
    return data
#data=[]
#fitting(data)


