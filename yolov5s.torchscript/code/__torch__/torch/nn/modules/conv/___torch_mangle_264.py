class Conv2d(Module):
  __parameters__ = ["weight", "bias", ]
  __buffers__ = []
  weight : Tensor
  bias : Tensor
  training : bool
  def forward(self: __torch__.torch.nn.modules.conv.___torch_mangle_264.Conv2d,
    argument_1: Tensor) -> Tensor:
    _0 = self.bias
    _1 = torch._convolution(argument_1, self.weight, _0, [1, 1], [0, 0], [1, 1], False, [0, 0], 1, False, False, True)
    return _1
