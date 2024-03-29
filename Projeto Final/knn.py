from dataf import main
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import scikitplot as skplt
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_score
from sklearn.metrics import mean_absolute_error
import numpy as np
import warnings


def Roc(y_pred, y_test):
	skplt.metrics.plot_roc_curve(y_test, y_pred)
	plt.show()


def cross_v_train(x, y):

	floor = 0
	size = int(len(x) * 0.2)
	ceil = size
	avg, error, knn_list = [], [], []
	for i in range(0, 5):
		knn = KNeighborsClassifier(n_neighbors = 1)
		x_test = x[floor:ceil]
		x_train = x[:floor] + x[ceil:]

		y_test = y[floor:ceil]
		y_train = y[:floor] + y[ceil:]

		knn.fit(x_train, y_train)
		y_pred = knn.predict(x_train)


		pres = precision_score(y_train, y_pred, average='micro')
		err = mean_absolute_error(y_train, y_pred)

		avg.append(pres)
		error.append(err)
		knn_list.append(knn)

		y_probs = knn.predict_proba(x_train)
		cm = confusion_matrix(y_train, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])

		Roc(y_probs, y_train)
		print("Matriz de Confusão, iteração: " + str(i))
		print(cm)
		print("Precisão no split " + str(i) + " do k-fold cross-validation: "+ str(pres))
		print("Erro no split  "+ str(i)+ "do k-fold: " + str(err))

		floor = ceil
		ceil = ceil+size
		print('\n\n\n')

	max_precision = max(avg)
	index = avg.index(max_precision)
	knn = knn_list[index] #knn mais preciso
	return knn, np.mean(avg), np.mean(error)

if __name__ == "__main__":
	warnings.filterwarnings("ignore")
	x, y = main()

	print("----------------------Porção de Treino (80%)----------------------")

	#split dataset into train and test data
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, stratify=y)
	size_train = int(len(x_train) * 0.8)


	#treinamento do modelo Percentage Split
	knn = KNeighborsClassifier(n_neighbors = 1)
	knn.fit(x_train[:size_train],y_train[:size_train])
	y_pred = knn.predict(x_train[size_train:])
	y_probs = knn.predict_proba(x_train[size_train:])
	cm = confusion_matrix(y_train[size_train:], y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
	Roc(y_probs, y_train[size_train:])
	print("Matriz de Confusão porção de teste separada de 80%, treino Percentage Split: ")
	print(cm)
	print("Precisão na porção de teste separada de 80%, Percentage Split: "+ str(precision_score(y_train[size_train:], y_pred, average='micro')))
	print("Erro na porção de teste separada de 80, Percentage Split%: " + str(mean_absolute_error(y_train[size_train:], y_pred)), end='\n\n\n')
	

	
	#treinamento do modelo com Cross-Validation
	knn_cv, score, error = cross_v_train(x_train[:size_train],y_train[:size_train])
	print("Scores Médio teste K-fold: " + str(score), end='\n\n\n')




	print("-----------------------Porção de Testes (20%)----------------------")


#-----------------essa parte é os 20% separados para teste#----------------------------




	#teste do modelo Percentage Split
	y_pred = knn.predict(x_test)
	print("Precisão na porção de teste (20%), Treinamento Percentage Split" + str(precision_score(y_test, y_pred, average='micro')))
	print("Erro na porção de teste (20%), Treinamento Percentage Split" + str(mean_absolute_error(y_test, y_pred)))
	y_probs = knn.predict_proba(x_test)
	cm = confusion_matrix(y_test, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
	Roc(y_probs, y_test)
	print("Matriz de Confusão na porção de teste(20%), treino Percentage Split: ")
	print(cm, end='\n\n\n')
	




	#teste do modelo com cross-validation
	print('Matriz de Confusão K-Fold: ')
	y_pred = knn_cv.predict(x_test)
	cm = confusion_matrix(y_test, y_pred, labels = ['0','1','2','3','4','5','6','7','8'])
	print(cm) 	
	y_probs = knn_cv.predict_proba(x_test)
	Roc(y_probs, y_test)
	print("Precisão na porção de teste separada em 20% "+ str(precision_score(y_test, y_pred, average='micro')))
	print("Erro na porção de teste separada em 20%: " + str(mean_absolute_error(y_test, y_pred)))


	print('\n\n\n')