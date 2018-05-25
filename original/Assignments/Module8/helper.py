from sklearn.neighbors import KernelDensity

def gsd(X, n_samples=100, random_state=0):
    kde = KernelDensity()
    kde.fit(X)
    sample_data = kde.sample(n_samples=n_samples,random_state=random_state)
    return sample_data