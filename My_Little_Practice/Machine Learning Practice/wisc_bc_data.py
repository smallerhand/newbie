import tensorflow as tf
tf.reset_default_graph()     #그래프 초기화
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA as sklearnPCA
data = np.genfromtxt('/Users/kimseunghyuck/desktop/wisc_bc_data.csv', dtype=(str), delimiter=',', skip_header=1, encoding='euc-kr')
data2 = np.genfromtxt('/Users/kimseunghyuck/desktop/wisc_bc_data.csv', dtype=(float), delimiter=',', skip_header=1, encoding='euc-kr')
def logical(x):
    if x == "M":
        return 1
    else:
        return 0
label=np.array([logical(i) for i in data[:,1]]).reshape(-1,1)
print("malign counted ", sum(label), "not malign counted ", len(label)-sum(label))
traindata=data2[:,2:]
traindata = preprocessing.scale(traindata)
sklearn_pca = sklearnPCA(n_components=16)
traindata = sklearn_pca.fit_transform(traindata)
datamerge=np.concatenate((label, traindata), axis=1)
from sklearn.model_selection import train_test_split
trains, validates = train_test_split(datamerge, test_size = 0.3)
train_data = trains[:,1:]
validate_data = validates[:,1:]
train_label = trains[:,0].reshape(-1,1)
validate_label = validates[:,0].reshape(-1,1)
#label=1, validate_data[validate_label==1]
v1data=validates[validates[:,0]==1, 1:]
v2data=validates[validates[:,0]==0, 1:]
v1label=np.array(np.repeat(1, v1data.shape[0])).reshape(-1, 1)
v2label=np.array(np.repeat(0, v2data.shape[0])).reshape(-1, 1)

X=tf.placeholder(tf.float32, [None, 16])
Y=tf.placeholder(tf.float32, [None, 1])
w1=tf.Variable(tf.random_normal([16, 32]))
b1=tf.Variable(tf.random_normal([32]))
l1=tf.nn.sigmoid(tf.matmul(X, w1)+b1)
w2=tf.Variable(tf.random_normal([32, 64]))
b2=tf.Variable(tf.random_normal([64]))
l2=tf.nn.sigmoid(tf.matmul(l1, w2)+b2)
w3=tf.Variable(tf.random_normal([64, 128]))
b3=tf.Variable(tf.random_normal([128]))
l3=tf.nn.sigmoid(tf.matmul(l2, w3)+b3)
w4=tf.Variable(tf.random_normal([128, 1]))
b4=tf.Variable(tf.random_normal([1]))
h=tf.nn.sigmoid(tf.matmul(l3, w4)+b4)
"""
cost = -tf.reduce_mean(Y * tf.log(h) + (1 - Y) * tf.log(1 - h))
cost=tf.reduce_mean((Y-h)**2)
cost=tf.reduce_mean(tf.reduce_sum((-Y * tf.log(h)) - ((1 - Y) * tf.log(1 - h)), reduction_indices=[1]))
"""
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=h)) 
train= tf.train.RMSPropOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(h > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1501):
        _, c=sess.run([train, cost], feed_dict={X:train_data, Y:train_label})
        if i%100==0:
            a, c=sess.run([accuracy * 100, cost], feed_dict={X:validate_data, Y:validate_label})
            print(i, "Accuracy: %.2f%%, Cost : %.4f"%(a, c))
    print("The last Accuracy: %.2f%%, Cost : %.4f"%(a, c))
    a1=sess.run(accuracy * 100, feed_dict={X:v1data, Y:v1label})
    a2=sess.run(accuracy * 100, feed_dict={X:v2data, Y:v2label})
    print("When it's Malignity: %.2f%%"%a1)
    print("When it's not Malignity: %.2f%%"%a2)

