import tensorflow as tf

# Ingreso de dimensiones por el usuario
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Creación de matrices aleatorias con valores entre 1 y 20
A = tf.random.uniform(shape=(filas, columnas), minval=1, maxval=21, dtype=tf.int32)
B = tf.random.uniform(shape=(filas, columnas), minval=1, maxval=21, dtype=tf.int32)

print("\nMatriz A:")
print(A.numpy())

print("\nMatriz B:")
print(B.numpy())

# Suma de Matrices
suma = tf.add(A, B)
print("\nSuma A + B:")
print(suma.numpy())

# Multiplicación de Matrices
if columnas == filas:
    producto = tf.matmul(A, B)
    print("\nMultiplicación A * B:")
    print(producto.numpy())
else:
    print("\nNo se puede multiplicar A * B: las dimensiones no son compatibles.")
