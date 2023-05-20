from data import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import statsmodels.api as sm


#Creating X and y
X, y = adv['TV'], adv['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42,
                                                   test_size = 0.3)
                                                   


#1. Statsmodel
def get_model_sm(X_train, y_train):
    
    #model
    lr = sm.OLS(y_train, sm.add_constant(X_train))
    
    model = lr.fit()
    
    #model param
    print(model.params)
    
    #model summary
    print(model.summary2())
    
    if input('Save model?\n(y/n) ').lower() == 'y':
        
        filename = input('Filename> ')
        pickle.dump(model, open(filename, 'wb'))
        
    else:
        pass  

    
    return model


#2. Sklearn
def get_model_sk(X_train, y_train):
    
    #creating lr object of class Linear regression
    lm = LinearRegression()
    
    #fitting the model
    model = lm.fit(X_train.values.reshape(-1,1), y_train)
    
    print('Corfficient: {}'.format(model.coef_))
    print('Intercept: {}'.format(model.intercept_))
    
    if input('Save model?\n(y/n) ').lower() == 'y':
        
        filename = input('Filename> ')
        pickle.dump(model, open(filename, 'wb'))
        
    else:
        pass
    
    return model


#3. Model evaluation
def model_eval(X_test, y_test, model):
    
    if input('Which model?\n(stats/sklearn) ').lower() == 'stats':
        
        y_test_pred = model.predict(sm.add_constant(X_test))
    
    else:
        
        y_test_pred = model.predict(X_test.values.reshape(-1,1))
        
        
    
    r2 = r2_score(y_true = y_test,
                  y_pred = y_test_pred)
    
    mse = mean_squared_error(y_true = y_test,
                             y_pred = y_test_pred )
    
    print('\nCoeff of determination, r2: {}'.format(r2))
    print('\nMean squared error, mse: {}'.format(mse))
    
    return r2, mse



