import gc
import torch

def get_tensors_in_memory():
    tensor_count = 0
    total_size = 0
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
                total_size += obj.size()
                tensor_count += 1
        except:
            pass
    return tensor_count, total_size


def softmax(t):
    return t.exp() / t.exp().sum(-1).unsqueeze(-1)


def roc_auc_compute_fn(y_preds, y_targets):
    try:
        from sklearn.metrics import roc_auc_score
    except ImportError:
        raise RuntimeError("This contrib module requires sklearn to be installed.")

    y_true = y_targets.detach().numpy()
    y_pred = y_preds.detach().numpy()
    return roc_auc_score(y_true, y_pred)

