class Bottleneck(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  cv1 : __torch__.models.common.___torch_mangle_106.Conv
  cv2 : __torch__.models.common.___torch_mangle_110.Conv
  def forward(self: __torch__.models.common.___torch_mangle_111.Bottleneck,
    argument_1: Tensor) -> Tensor:
    _0 = (self.cv2).forward((self.cv1).forward(argument_1, ), )
    return torch.add(argument_1, _0, alpha=1)
