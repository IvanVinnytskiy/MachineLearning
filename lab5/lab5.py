import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion_data=tf.keras.datasets.fashion_mnist

(inp_train, out_train),(inp_test, out_test) = fashion_data.load_data()

inp_train = inp_train/255.0
inp_test = inp_test/255.0

plt.figure(figsize = (10,10))
for i in range(100):
    plt.subplot(10,10,i+1)
    plt.imshow(inp_train[i])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(out_train[i])
    plt.tight_layout()
plt.show()

Labels=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure(figsize=(10,10))
for i in range(100):
    plt.subplot(10,10,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(inp_train[i], cmap=plt.cm.binary)
    plt.xlabel(Labels[out_train[i]])
    plt.tight_layout()
plt.show()

my_model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# sigmoid
# softmax
# softplus
# softsign
# tanh
# selu
# elu
# exponential

my_model.compile(optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'])
my_model.fit(inp_train, out_train, epochs=10)

loss, accuracy = my_model.evaluate(inp_test, out_test, verbose=2)
print('\nAccuracy:', accuracy * 100)

prob=tf.keras.Sequential([my_model,tf.keras.layers.Softmax()])
pred=prob.predict(inp_test)

plt.figure(figsize = (10,10))
for i in range(20):
    true_label,image = out_test[i], inp_test[i]
    pred_label = np.argmax(pred[i])
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap=plt.cm.binary)
    if pred_label == true_label:
        color = 'green'
        label="Correct"
    else:
        color = 'red'
        label="Wrong"
    plt.tight_layout()
    plt.title(label,color=color)
    plt.xlabel(" {} -> {} ".format(Labels[true_label],Labels[pred_label]))
	
plt.show()

