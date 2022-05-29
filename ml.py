import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import main


def analyse(df):
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.model_selection import RepeatedKFold
    from sklearn.model_selection import cross_val_score
    
    # Single Variable
    ## Count Operator
    ## Set Operator
    ## Hash Operator
    ## Unified Difference
    ## Tree Difference

    # SCOSS_count
    # SCOSS_set
    # SCOSS_hash
    # unified_diff
    # tree_diff

    method = ['SCOSS_count', 'SCOSS_set', 'SCOSS_hash', 'unified_diff', 'tree_diff']



    # X = [df["SCOSS_count"].tolist(), df["SCOSS_set"].tolist(), df["SCOSS_hash"].tolist(), df["unified_diff"].tolist(), df["tree_diff"].tolist()]
    # X = X[0:3] # first 3 features
    # y = df['real_percentage'].tolist()

    X_list = [
        ['SCOSS_count'],
        ['SCOSS_set'],
        ['SCOSS_hash'],
        ['unified_diff'], 
        ['tree_diff'],

        # ['SCOSS_count','SCOSS_set'],
        # ['SCOSS_count','SCOSS_hash'],
        # ['SCOSS_count','unified_diff'],
        # ['SCOSS_count','tree_diff'],
        # ['SCOSS_set','SCOSS_hash'],
        # ['SCOSS_set','unified_diff'],
        # ['SCOSS_set','tree_diff'],
        # ['SCOSS_hash','unified_diff'],
        # ['SCOSS_set','tree_diff'],
        # ['unified_diff','tree_diff']
    ]




    y = df.loc[:,['real_percentage']]

    result = []

    for col_name in X_list:
        if len(col_name) == 1:
            X = df.loc[:,[col_name[0]]]
        else:
            X = []
            for col in col_name:
                X += [df.loc[:,[col]]]

        cv = RepeatedKFold(n_splits=5, n_repeats=2, random_state=2652124)
        lreg = LinearRegression()

        result += [[
            col_name,
            np.mean(cross_val_score(lreg, X, y, scoring='r2', cv=cv, n_jobs=-1)), 
            np.std(cross_val_score(lreg, X, y, scoring='r2', cv=cv, n_jobs=-1)),
            np.mean(cross_val_score(lreg, X, y, scoring='neg_root_mean_squared_error', cv=cv, n_jobs=-1)),
            np.std(cross_val_score(lreg, X, y, scoring='neg_root_mean_squared_error', cv=cv, n_jobs=-1))
        ]]
        

    columns = ["Model", "R2_mean", "R2_std", "RMSE_mean", "RMSE_std"]
    df = pd.DataFrame(result, columns=columns)
    print(df)
    # x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8)


    # maxdegree=7 # The maximum degree we would like to test
    # training_error=[]
    # cross_validation_error=[]
    # for d in range(1,maxdegree):
    #     x_poly_train=PolynomialFeatures(degree=d).fit_transform(x_train)
    #     x_poly_test=PolynomialFeatures(degree=d).fit_transform(x_test)
    #     lr=LinearRegression(fit_intercept=False)
    #     model=lr.fit(x_poly_train,y_train)
    #     y_train_pred=model.predict(x_poly_train)
    #     mse_train=mean_squared_error(y_train,y_train_pred)
    #     cve=cross_validate(lr,x_poly_train,y_train,scoring='neg_mean_squared_error',cv=5,return_train_score=True)
    #     training_error.append(mse_train)
    #     cross_validation_error.append(np.mean(np.absolute(cve['test_score'])))
    # fig,ax=plt.subplots(figsize=(6,6))
    # ax.plot(range(1,maxdegree),cross_validation_error)
    # ax.set_xlabel('Degree',fontsize=20)
    # ax.set_ylabel('MSE',fontsize=20)
    # ax.set_title('MSE VS Degree',fontsize=25)
    # plt.show()

    


def section1():
    # st.title("Code Score Prediction - Training")

    data = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", \
                     "C16", "C17", "C18", "C19", "C20", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30",
                     "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"]

    # st.header("Exercise A")
    dfA = main.analyse("ExA", data)
    dfB = main.analyse("ExB", data)
    dfC = main.analyse("ExC", data)
    dfD = main.analyse("ExD", data)
    df  = pd.concat([dfA, dfB, dfC, dfD])

    analyse(dfB)


if __name__ == '__main__':
    section1()