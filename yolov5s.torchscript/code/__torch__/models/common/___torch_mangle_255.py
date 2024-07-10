class Conv(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  conv : __torch__.torch.nn.modules.conv.___torch_mangle_252.Conv2d
  bn : __torch__.torch.nn.modules.batchnorm.___torch_mangle_253.BatchNorm2d
  act : __torch__.torch.nn.modules.activation.___torch_mangle_254.LeakyReLU
  def forward(self: __torch__.models.common.___torch_mangle_255.Conv,
    argument_1: Tensor) -> Tensor:
    _0 = self.act
    _1 = (self.bn).forward((self.conv).forward(argument_1, ), )
    return (_0).forward(_1, )
