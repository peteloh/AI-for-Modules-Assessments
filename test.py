
def main():
    from sklearn.linear_model import Ridge
    import numpy as np
    n_samples, n_features = 10, 5
    rng = np.random.RandomState(0)
    y = rng.randn(n_samples)
    X = rng.randn(n_samples, n_features)
    clf = Ridge(alpha=1.0)
    clf.fit(X, y)
    print(clf)








if __name__ == '__main__':
    # python3 tests/test_scoss.py 
    # 1. url variable will be empty if userid is invalid
    # userid should be 5-digit long, e.g. 13579
    # 2. maybe moss server takes forever to return
    main()
