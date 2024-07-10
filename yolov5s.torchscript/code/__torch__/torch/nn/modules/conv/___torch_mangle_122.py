class Conv2d(Module):
  __parameters__ = ["weight", ]
  __buffers__ = []
  weight : Tensor
  training : bool
  def forward(self: __torch__.torch.nn.modules.conv.___torch_mangle_122.Conv2d,
    input: Tensor) -> Tensor:
    input0 = torch._convolution(input, self.weight, None, [1, 1], [0, 0], [1, 1], False, [0, 0], 1, False, False, True)
    return input0
