import statistics
def bubble(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
 

a = [float(i) for i in input().split()]
N = len(a)
bubble(a)
print("Объем ряда: ", len(a))
print("Среднее: ", statistics.mean(a))
print("Упорядочить: ", a)
print("Размах: ", max(a), "-", min(a), "=", max(a)-min(a))
print("Мода: ", statistics.mode(a))
print("Медиана: ", statistics.median(a))

