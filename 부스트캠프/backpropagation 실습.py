import numpy as np
np.random.seed(seed=1)

# 샘플 개수
n_samples = 100
# 시퀀스 길이
len_sequence = 10
# 시퀀스 생성
X = np.zeros((n_samples, len_sequence))
for row_idx in range(n_samples):
    X[row_idx,:] = np.around(np.random.rand(len_sequence)).astype(int)
# 각 시퀀스의 타겟 생성
t = np.sum(X, axis=1)

def update_state(xk, sk, wx, wRec):
    return xk * wx + sk * wRec

def forward_states(X, wx, wRec):
    # 모든 input 시퀀스 X 들에 대한 상태를 담고 있는 행렬 S 초기화
    S = np.zeros((X.shape[0], X.shape[1]+1))
    for k in range(0, X.shape[1]):
        # S[k] = S[k-1] * wRec + X[k] * wx
        S[:,k+1] = update_state(X[:,k], S[:,k], wx, wRec)
    return S

def loss(y, t): 
    return np.mean((t - y)**2)# MSE, (벡터차 제곱)에서 모든 벡터원소합/벡터개수100개


def output_gradient(y, t):
    return 2. * (y - t)

def backward_gradient(X, S, grad_out, wRec):
    """
    X: input
    S: 모든 input 시퀀스에 대한 상태를 담고 있는 행렬
    grad_out: output의 gradient
    wRec: 재귀적으로 사용되는 학습 파라미터
    """
    # grad_over_time: loss의 state 에 대한 gradient 
    # 초기화
    grad_over_time = np.zeros((X.shape[0], X.shape[1]+1))
    grad_over_time[:, -1] = grad_out
    # gradient accumulations 초기화
    wx_grad = 0
    wRec_grad = 0
    wRecAcc = 1
    '''
    TODO
    '''
    for k in range(1,X.shape[1]+1):
        wx_grad+=wRecAcc*X[:,X.shape[1]-k]
        wRec_grad+=wRecAcc*S[:,S.shape[1]-k-1]
        wRecAcc*=wRec
        
    wx_grad = sum(grad_out*wx_grad)/n_samples
    wRec_grad = sum(grad_out*wRec_grad)/n_samples
    return (wx_grad, wRec_grad), grad_over_time

params = [1.2, 1.2]  # [wx, wRec]
eps = 1e-7
S = forward_states(X, params[0], params[1])
grad_out = output_gradient(S[:,-1], t)
backprop_grads, grad_over_time = backward_gradient(X, S, grad_out, params[1])
for p_idx, _ in enumerate(params):
    grad_backprop = backprop_grads[p_idx]
    params[p_idx] += eps
    plus_loss = loss(forward_states(X, params[0], params[1])[:,-1], t)
    params[p_idx] -= 2 * eps
    min_loss = loss(forward_states(X, params[0], params[1])[:,-1], t)
    params[p_idx] += eps
    grad_num = (plus_loss - min_loss) / (2*eps)
    if not np.isclose(grad_num, grad_backprop):
        raise ValueError((
            f'Numerical gradient of {grad_num:.6f} is not close to '
            f'the backpropagation gradient of {grad_backprop:.6f}!'))
print('No gradient errors found')