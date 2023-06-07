import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Carregar o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Pré-processamento dos dados
x_train = x_train / 255.0
x_test = x_test / 255.0

# Criar o modelo da rede neural
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compilar o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)

# Avaliar o modelo
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print('Acurácia no conjunto de teste:', accuracy)

