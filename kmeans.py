from random import randint

class KMeansClusterClassifier:

    def __init__(self, n_cluster):
        self.n_cluster = n_cluster
    
    def distance(self, point1, point2):
        dist = (((point1[0] - point2[0])**2)+((point1[1] - point2[1])**2)+((point1[2] - point2[2])**2)+((point1[3] - point2[3])**2))**0.5
        return dist
    
    def elbow(self):
        for self.n_cluster in range(10):
            clf = KMeansClusterClassifier(self.n_cluster)

    def fit(self,X,y):
        size_x = len(X)

        centroids = [0] * self.n_cluster
        dist_2_centroids = [0] * self.n_cluster

        for i in range(self.n_cluster):
            random_number = randint(0,size_x-1)
            centroids[i] = X[random_number]
        

        while 1:
            which_centoid = [0 for c in range(size_x)]
            for i in range(size_x):
                point = X[i]
                for j in range(self.n_cluster):
                    center = centroids[j]
                    dist_2_centroids[j] = self.distance(point,center)
                minimum_dist = min(dist_2_centroids)
              
                minimum_distance_class = dist_2_centroids.index(min(dist_2_centroids))

                which_centoid[i] = minimum_distance_class

            count_points = [0 for c in range(self.n_cluster)]

            for i in range(size_x):
                count_points[which_centoid[i]] = count_points[which_centoid[i]]+1

            new_centoids = [[0 for c in range(4)] for r in range(self.n_cluster)]

            for i in range(size_x):
                    new_centoids[which_centoid[i]] = new_centoids[which_centoid[i]] + X[i]

            for i in range(self.n_cluster):
                if(count_points[i] != 0):
                    new_centoids[i] = new_centoids[i] / count_points[i]
        
            isTrue = 1
            for i in range(self.n_cluster):
                for j in range(4):
                    if new_centoids[i][j] != centroids[i][j]:
                        isTrue = 0

            if isTrue == 1:
                break
            else:
                centroids = new_centoids
        
        #hangi centroid hangi class a ait ataması yap
        #iris setosa -- iris versicolour -- iris virginica

        which_class = [[0 for c in range(3)] for r in range(self.n_cluster)]

        for i in range(size_x):
            if y[i] == 'Iris-setosa':
                which_class[which_centoid[i]][0] = which_class[which_centoid[i]][0] + 1
            if y[i] == 'Iris-versicolor':
                which_class[which_centoid[i]][1] = which_class[which_centoid[i]][1] + 1
            if y[i] == 'Iris-virginica':
                which_class[which_centoid[i]][2] = which_class[which_centoid[i]][2] + 1

        X_son = centroids
        y_son = [[0 for c in range(1)] for r in range(self.n_cluster)]

        for i in range(self.n_cluster):
            max_num = max(which_class[i])
            for j in range(3):
                if max_num == which_class[i][j]:
                    if j==0:
                        y_son[i] = 'Iris-setosa'
                    elif j==1:
                        y_son[i] = 'Iris-versicolor'
                    elif j==2:
                        y_son[i] = 'Iris-virginica'

        
        return X_son,y_son

    def predict(self,X,centroids,labels):
        size_x = len(X)
        predictions = [0 for c in range(size_x)] 
       
        
        for i in range(size_x):
            point = X[i]
            dist = [0 for c in range(self.n_cluster)] 
            for j in range(self.n_cluster):
                dist[j] = self.distance(point,centroids[j])
            min_dist = min(dist)
            for k in range(self.n_cluster):
                if min_dist == dist[k]:
                    predictions[i] = labels[k]

        return predictions




        


        

        
