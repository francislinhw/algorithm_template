import numpy as np
import matplotlib.pyplot as plt


class Solution:

    def kmeans(self, data, k):
        # 隨機選擇 k 個中心點
        centroids = data[np.random.choice(range(len(data)), k, replace=False)]

        # 迭代直到收斂
        while True:
            # It is not guaranteed to converge, so cluster is a NP hard problem

            # 分配數據到最近的中心點
            clusters = [[] for _ in range(k)]
            for point in data:
                distances = np.linalg.norm(point - centroids, axis=1)
                cluster_index = np.argmin(distances)
                clusters[cluster_index].append(point)

            # 更新中心點
            new_centroids = np.array([np.mean(cluster, axis=0) for cluster in clusters])

            # 檢查是否收斂
            if np.all(centroids == new_centroids):
                break

            # 更新中心點
            centroids = new_centroids

        return centroids, clusters


if __name__ == "__main__":
    data = np.array([[1, 2], [1, 3], [2, 1], [3, 1], [8, 7], [8, 8], [9, 7], [9, 8]])
    solution = Solution()
    centroids, clusters = solution.kmeans(data, 2)

    plt.scatter(data[:, 0], data[:, 1], c="gray", label="data")
    plt.scatter(centroids[:, 0], centroids[:, 1], c="red", label="centroids")
    plt.legend()
    plt.show()
