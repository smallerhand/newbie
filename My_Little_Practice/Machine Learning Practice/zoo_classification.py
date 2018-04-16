"""
# http://archive.ics.uci.edu/ml/datasets/zoo
#   1. animal name
#   2. hair     Boolean"
#   3. feathers     Boolean"
#   4. eggs     Boolean"
#   5. milk     Boolean"
#   6. airborne     Boolean"
#   7. aquatic      Boolean"
#   8. predator     Boolean"
#   9. toothed      Boolean"
#  10. backbone     Boolean"
#  11. breathes     Boolean"
#  12. venomous     Boolean"
#  13. fins     Boolean"
#  14. legs     Numeric (set of values: {0",2,4,5,6,8})
#  15. tail     Boolean"
#  16. domestic     Boolean"
#  17. catsize      Boolean"
#  18. type     Numeric (integer values in range [0",6])
#      1 : 포유류, 2 : 조류, 3 : 파충류, 4 : 어류, 5 : 양서류, 6 : 곤충/거미류, 7 : 무척추동물
"""

import tensorflow as tf
import numpy as np
import pandas as pd
data = np.genfromtxt('/Users/kimseunghyuck/desktop/data_zoo.csv', delimiter=',', encoding='euc-kr')
x_data=data[:, :-1]
y_data=data[:,-1].reshape(-1,1)
X=tf.placeholder(tf.float32, [None, 16])
Y=tf.placeholder(tf.int32, [None, 1])
Y_onehot=tf.reshape(tf.one_hot(Y, 7), [-1, 7])
w1=tf.Variable(tf.random_normal([16,32]))
b1=tf.Variable(tf.random_normal([32]))
l1=tf.nn.relu(tf.matmul(X, w1)+b1)
w2=tf.Variable(tf.random_normal([32, 64]))
b2=tf.Variable(tf.random_normal([64]))
l2=tf.nn.relu(tf.matmul(l1, w2)+b2)
w3=tf.Variable(tf.random_normal([64, 7]))
b3=tf.Variable(tf.random_normal([7]))
h=tf.matmul(l2, w3)+b3

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=h, labels=Y_onehot))
train=tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(501):
        _, c= sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
        if i%50==0:
            print(i, c)
    p=sess.run(tf.arg_max(h, 1), feed_dict={X:x_data})
    print("Accuracy : {}".format(sum(p==y_data.astype(int).reshape(-1,))/101))



