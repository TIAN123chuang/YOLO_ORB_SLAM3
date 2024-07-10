class BottleneckCSP(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  cv1 : __torch__.models.common.___torch_mangle_187.Conv
  cv2 : __torch__.torch.nn.modules.conv.___torch_mangle_188.Conv2d
  cv3 : __torch__.torch.nn.modules.conv.___torch_mangle_189.Conv2d
  cv4 : __torch__.models.common.___torch_mangle_193.Conv
  bn : __torch__.torch.nn.modules.batchnorm.___torch_mangle_194.BatchNorm2d
  act : __torch__.torch.nn.modules.activation.___torch_mangle_195.LeakyReLU
  m : __torch__.torch.nn.modules.container.___torch_mangle_205.Sequential
  def forward(self: __torch__.models.common.___torch_mangle_206.BottleneckCSP,
    argument_1: Tensor) -> Tensor:
    _0 = self.cv4
    _1 = self.act
    _2 = self.bn
    _3 = self.cv2
    _4 = self.cv3
    _5 = (self.m).forward((self.cv1).forward(argument_1, ), )
    _6 = [(_4).forward(_5, ), (_3).forward(argument_1, )]
    input = torch.cat(_6, 1)
    _7 = (_1).forward((_2).forward(input, ), )
    return (_0).forward(_7, )
