class Conv2d(Module):
  __parameters__ = ["weight", ]
  __buffers__ = []
  weight : Tensor
  training : bool
  def forward(self: __torch__.torch.nn.modules.conv.___torch_mangle_114.Conv2d,
    argument_1: Tensor) -> Tensor:
    input = torch._convolution(argument_1, self.weight, None, [2, 2], [1, 1], [1, 1], False, [0, 0], 1, False, False, True)
    return input
