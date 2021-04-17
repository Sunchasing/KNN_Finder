import random

from KNN_Finder.knn_finder import KNNFinder


def main(minval: int, maxval: int, pop_size: int, k_size: int):
    input_list = [random.randint(minval, maxval) for _ in range(pop_size)]
    knnf = KNNFinder(input_list)
    for v in random.sample(range(minval, maxval), 10):
        knn = knnf.find_knn(v, k_size)
        print(f'DATA: {input_list}\nVALUE: {v}\nINDICES: {knn}\nVALUES: {[input_list[i] for i in knn]}\n\n')


if __name__ == '__main__':
    main(
        minval=-1000,
        maxval=1000,
        pop_size=2000,
        k_size=15
    )
