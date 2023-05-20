#Functions for various analysis

from model import *

#1. get distribution plots
def dist_plots(data):
    
    for i in data.columns:
        
        plt.figure(figsize = (10, 10))
        
        plt.subplot(2, 2, 2)
        sns.boxplot(data = data, x = i, color = 'C2' )
        
        plt.subplot(2, 2, 1)
        sns.kdeplot(x = data[i], color = 'C0')
        
        plt.subplot(2, 2, 4)
        sns.scatterplot(data = data, x = i, y = 'Sales')
        
        plt.subplot(2, 2, 3)
        sns.histplot(data = data, x = i, color = 'C3')
        
        
        if input("Save image?\n(y/n): ").lower() == 'y':
            plt.savefig(f'Distribution plot  of {i}')
        else:
            plt.show()

#2. get regression plot
def regression_plot(X_train, y_train, model):
    
    #checking which model we are using
    if input('Which model?\n(stats/sklearn) ').lower() == 'stats':
        
        sns.scatterplot(x = X_train,
                        y = y_train)
        plt.plot(X_train,
                 model.params[0] + model.params[1] * X_train,
                 'C1')
    
    else:
        sns.scatterplot(x = X_train, 
                        y = y_train)
        plt.plot(X_train,
                 model.intercept_ + model.coef_[0] * X_train,
                 'C1')
    
    #checking if we want to save
    if input('\nSave regression line?\n(y/n) ').lower() == 'y':
        plt.savefig(fname = input('File_name> '), dpi = 500)
    
    else:
        plt.show()


#3. get residual plots
def residual_analysis(X_train, y_train, model):
    
    if input('Which model?\n(stats/sklearn) ').lower() == 'stats':
        
        y_train_pred = model.predict(sm.add_constant(X_train))
    
    else:
        
        y_train_pred = model.predict(X_train.values.reshape(-1, 1))

    
    res = y_train - y_train_pred
    
    plt.figure(figsize = (10, 5))    
    plt.subplot(1, 2, 1)
    sns.distplot(x = res, color = 'C3')
    
    plt.subplot(1, 2, 2)
    sns.scatterplot(x = X_train, y = res)
    
    if input('Save residual analysis?\n(y/n) ').lower() == 'y':
        plt.savefig(input('File name> '), dpi = 500)
    
    else:
        plt.show() 






        

    
  