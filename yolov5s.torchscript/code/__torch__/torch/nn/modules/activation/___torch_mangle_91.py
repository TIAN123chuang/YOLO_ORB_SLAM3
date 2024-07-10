class LeakyReLU(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  def forward(self: __torch__.torch.nn.modules.activation.___torch_mangle_91.LeakyReLU,
    argument_1: Tensor) -> Tensor:
    _0 = torch.leaky_relu_(argument_1, 0.10000000000000001)
    return _0
