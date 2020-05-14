import numpy as np

def dis(x,y):
    return np.sqrt(np.sum(np.power(x-y,2)))

def k_means(x, k=4, epochs=500, delta=1e-3):

    indices = np.random.randint(0,len(x),size=k)
    centers = x[indices]

    results = []
    for i in range(k):
        results.append([])

    step = 1
    flag = True
    while flag:
        if step>epochs:
            return centers,results
        else:
            for i in range(k):
                results[i] = []

        for i in range(len(x)):
            current = x[i]
            min_dis = np.inf

            for j in range(k):
                distance = dis(current,centers[j])
                if distance<min_dis:
                    min_dis = distance
                    tmp = j
                results[tmp].append(current)
        for i in range(k):
            old_center = centers[i]
            new_center = np.array(results[i]).mean(axis=0)
            if dis(old_center, new_center)>delta:
                centers[i] = new_center
                flag = False
        if flag:
            break
        else:
            flag = True
        step += 1
    return centers, results