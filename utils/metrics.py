from sklearn.metrics import accuracy_score, mean_squared_error

def compute_accuracy(y_true, y_pred):
    """compute accuracy"""
    return accuracy_score(y_true, y_pred)

def compute_mse(y_true, y_pred):
    """compute mse"""
    return mean_squared_error(y_true, y_pred)