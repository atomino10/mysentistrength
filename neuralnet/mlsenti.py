import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

dataset='reviewstarsbin.csv'

df=pd.read_csv(dataset)



print(df.head(20))


X=df['reviews'].values
Y=df['sentiment'].values

#script to normalize sentiment values to be equal
#pos and neg sentiment are counted and their diff
#is removed from X in pos reviews

Z=len(df.loc[df['sentiment'] == 0])
W=len(df.loc[df['sentiment'] == 1])

length=W-Z
cnt=0;
for i in range(0,len(X)):
	if Y[i]==1:
		Y=np.delete(Y,i,0)
		X=np.delete(X,i,0)
		cnt=cnt+1;
	if cnt==length:
		break;

#################################################
# sns.countplot(Y)
# plt.show(sns)

# X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.3)

# vec = CountVectorizer()
# vec.fit(X_train.astype('U'))
# x_train=vec.transform(X_train.astype('U'))
# x_test=vec.transform(X_test.astype('U'))


# model = Sequential()
# model.add(Dense(16, input_dim=x_train.shape[1], activation='relu'))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
# model.summary()
# history = model.fit(x_train, Y_train,validation_data=(x_test, Y_test),epochs=100,verbose=True,batch_size=16)

# model.save('savedmodel')
# np.save('savedmodel/savedmodel.npy',history.history)



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#plotsssssssssss
model = tf.keras.models.load_model('savedmodel')
history=np.load('savedmodel/savedmodel.npy',allow_pickle='TRUE').item()

# list all data in history

# summarize history for accuracy
plt.plot(history['accuracy'])
plt.plot(history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()