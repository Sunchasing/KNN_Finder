class KNNFinder:

    def __init__(self, data: list):
        self._data = data

    def find_knn(self, value: int, k_size: int) -> list:
        updated_data = self._data[1:]
        max_diff = abs(value - self._data[0])
        ret = [(0, max_diff)]
        for idx, elem in enumerate(updated_data):
            diff = abs(value - elem)
            if diff <= max_diff:
                if len(ret) == k_size:
                    ret.pop(-1)
                for ind in range(len(ret)):
                    if ret[ind][1] > diff or ind == len(ret) - 1:
                        ret.insert(ind, (idx + 1, diff))
                        break
            else:
                if len(ret) < k_size:
                    ret.append((idx + 1, diff))
            max_diff = ret[-1][1]

        return [x[0] for x in ret]
