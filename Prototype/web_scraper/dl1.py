# Mô hình 10 tham số - train thủ công
import math

# Khởi tạo
params = {
    'w1': 0.1, 'w2': -0.2, 'w3': 0.3,
    'b1': 0.0, 'b2': 0.0, 'b3': 0.0,
    'v1': 0.1, 'v2': 0.1, 'v3': 0.1,
    'c': 0.0
}

data = [(1,3), (2,5), (3,7)]
lr = 0.01

for epoch in range(1000):
    total_loss = 0
    grads = {k: 0 for k in params}
    
    for x, y_true in data:
        # Forward
        z1 = params['w1']*x + params['b1']
        z2 = params['w2']*x + params['b2']
        z3 = params['w3']*x + params['b3']
        a1, a2, a3 = max(0,z1), max(0,z2), max(0,z3)
        y_pred = params['v1']*a1 + params['v2']*a2 + params['v3']*a3 + params['c']
        
        loss = (y_true - y_pred)**2
        total_loss += loss
        
        # Backward (tính gradient)
        dL_dy = -2 * (y_true - y_pred)
        
        # Gradient cho lớp cuối
        grads['v1'] += dL_dy * a1
        grads['v2'] += dL_dy * a2
        grads['v3'] += dL_dy * a3
        grads['c']  += dL_dy
        
        # Gradient cho lớp đầu (chỉ neuron active)
        if z1 > 0: grads['w1'] += dL_dy * params['v1'] * x
        if z2 > 0: grads['w2'] += dL_dy * params['v2'] * x
        if z3 > 0: grads['w3'] += dL_dy * params['v3'] * x
        if z1 > 0: grads['b1'] += dL_dy * params['v1']
        if z2 > 0: grads['b2'] += dL_dy * params['v2']
        if z3 > 0: grads['b3'] += dL_dy * params['v3']
    
    # Cập nhật tham số
    for k in params:
        params[k] -= lr * grads[k] / len(data)
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss/len(data):.4f}")

print("Final params:", params)