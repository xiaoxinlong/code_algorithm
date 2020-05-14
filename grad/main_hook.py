import torch
def hook_y(grad):
    print("the grad of y:")
    print(grad)
    grad.zero_()


x = torch.rand((2,2))
t = torch.ones((2,2),requires_grad=True)

y = x*t + 2
z = y * y * 3

import pdb

# y.register_hook(hook_y)

out = z.mean()
print(t.grad)
out.backward(retain_graph=True)

out.backward()
# out.backward(retain_graph=True)
print(t.grad)
print(y.grad)