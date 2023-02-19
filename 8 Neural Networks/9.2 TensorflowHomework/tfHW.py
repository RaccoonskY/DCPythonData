import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = tf.divide(x_train,255)
x_test = tf.divide(x_test,255)

y_train = tf.keras.utils.to_categorical()


