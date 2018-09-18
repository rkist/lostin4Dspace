from configurations import *



#define 
clf = svm.SVC(gamma=0.001, C=100., 
              cache_size=200, class_weight=None, coef0=0.0,
              decision_function_shape='ovr', degree=3, kernel='rbf',
              max_iter=-1, probability=True, random_state=None, shrinking=True,
              tol=0.001, verbose=False)




#train              
X = clean_df[['Density', 'GammaRay', 'PorosityTotal']]
Y = clean_df["Facies"]
clf.fit(X, Y)



#score
clf.score(X, Y)




