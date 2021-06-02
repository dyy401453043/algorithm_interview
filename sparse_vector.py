# leetcode 1570 两个稀疏向量的点集

class SparseVector():
    def __init__(self, arr):
        self.arr = arr

    def dot_production(self, vec):
        result = 0
        i,j = 0,0
        while i < len(self.arr) and j < len(vec.arr):
            element1 = self.arr[i]
            element2 = vec.arr[j]
            if element1[0] < element2[0]:
                i+=1
            elif element1[0] > element2[0]:
                j+=1
            else:
                result += element1[1] * element2[1]
                i+=1
                j+=1
        return result

if __name__ == '__main__':
    arr1 = [(0,4),(7,6),(8,11),(15,5)]
    arr2 = [(8,12),(10,3),(15,10),(20,2)]
    vector1 = SparseVector(arr1)
    vector2 = SparseVector(arr2)
    print(vector1.dot_production(vector2))