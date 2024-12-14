
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score 



def predict(data):

	train_dataset=pd.read_csv('dataset.csv',nrows=10000)
	train_dataset['calories_burned'] = train_dataset['calories_burned'].fillna(0).astype(int)
	train_dataset['distance_km'] = train_dataset['distance_km'].fillna(0).astype(int)
	train_dataset['sleep_hours'] = train_dataset['sleep_hours'].fillna(0).astype(int)


	print(train_dataset)

	train_dataset=train_dataset.dropna()

	print("mood classes",train_dataset["mood"].unique())
	print("workout classes classes",train_dataset["workout_type"].unique())

	encoded_mood=LabelEncoder().fit_transform(y=train_dataset.mood)
	train_dataset.mood=encoded_mood

	encoded_workout_type=LabelEncoder().fit_transform(y=train_dataset.workout_type)
	train_dataset.workout_type=encoded_workout_type

	

	X=train_dataset.iloc[:,:-1]
	Y=train_dataset.iloc[:,-1]


	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)


	print(X)
	print(Y.head(100))
	model=RandomForestClassifier(n_estimators=100,criterion='entropy')

	

	model.fit(X_train,y_train)
	data = np.array(data).reshape(1, -1) 
	y_pred_test = model.predict(data)
	# print('Model Accuracy :',accuracy_score(y_test, y_pred_test))

	return y_pred_test[0]
# confusion=confusion_matrix(y_test, y_pred_test)

# roc_auc = roc_auc_score(y_test, y_pred_test) 
# print(classification_report(y_test, y_pred_test))
# y_pred_prob = model.predict_proba(X_test)[:, 1] 
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob, pos_label=1)
# # # import joblib
# # # joblib.dump(model, "RF_anomaly_model.joblib")
# cmap = sns.color_palette("Blues")

# matrix = confusion_matrix(y_test, y_pred_test)
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.heatmap(confusion,
#             cmap=cmap,
# 			annot=True,
# 			fmt='g',
# 			xticklabels=['Positive','Negative'],
# 			yticklabels=['Positive','Negative'])
# plt.ylabel('Prediction',fontsize=13)
# plt.xlabel('Actual',fontsize=13)
# plt.title('Confusion Matrix',fontsize=17)
# plt.show()



# # Plot the ROC curve 
# plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc) 
# # roc curve for tpr = fpr  
# plt.plot([0, 1], [0, 1], 'k--', label='Random classifier') 
# plt.xlabel('False Positive Rate') 
# plt.ylabel('True Positive Rate') 
# plt.title('ROC Curve') 
# plt.legend(loc="lower right") 
# plt.show()

