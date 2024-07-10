class Focus(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  conv : __torch__.models.common.Conv
  def forward(self: __torch__.models.common.Focus,
    x: Tensor) -> Tensor:
    _0 = self.conv
    _1 = torch.slice(x, 2, 0, 9223372036854775807, 2)
    _2 = torch.slice(_1, 3, 0, 9223372036854775807, 2)
    _3 = torch.slice(x, 2, 1, 9223372036854775807, 2)
    _4 = torch.slice(_3, 3, 0, 9223372036854775807, 2)
    _5 = torch.slice(x, 2, 0, 9223372036854775807, 2)
    _6 = torch.slice(_5, 3, 1, 9223372036854775807, 2)
    _7 = torch.slice(x, 2, 1, 9223372036854775807, 2)
    _8 = torch.slice(_7, 3, 1, 9223372036854775807, 2)
    input = torch.cat([_2, _4, _6, _8], 1)
    return (_0).forward(input, )
class Conv(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  conv : __torch__.torch.nn.modules.conv.Conv2d
  bn : __torch__.torch.nn.modules.batchnorm.BatchNorm2d
  act : __torch__.torch.nn.modules.activation.LeakyReLU
  def forward(self: __torch__.models.common.Conv,
    input: Tensor) -> Tensor:
    _9 = self.act
    _10 = (self.bn).forward((self.conv).forward(input, ), )
    return (_9).forward(_10, )
class BottleneckCSP(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  cv1 : __torch__.models.common.___torch_mangle_7.Conv
  cv2 : __torch__.torch.nn.modules.conv.___torch_mangle_8.Conv2d
  cv3 : __torch__.torch.nn.modules.conv.___torch_mangle_9.Conv2d
  cv4 : __torch__.models.common.___torch_mangle_13.Conv
  bn : __torch__.torch.nn.modules.batchnorm.___torch_mangle_14.BatchNorm2d
  act : __torch__.torch.nn.modules.activation.___torch_mangle_15.LeakyReLU
  m : __torch__.torch.nn.modules.container.Sequential
  def forward(self: __torch__.models.common.BottleneckCSP,
    argument_1: Tensor) -> Tensor:
    _11 = self.cv4
    _12 = self.act
    _13 = self.bn
    _14 = self.cv2
    _15 = self.cv3
    _16 = (self.m).forward((self.cv1).forward(argument_1, ), )
    _17 = [(_15).forward(_16, ), (_14).forward(argument_1, )]
    input = torch.cat(_17, 1)
    _18 = (_12).forward((_13).forward(input, ), )
    return (_11).forward(_18, )
class Bottleneck(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  cv1 : __torch__.models.common.___torch_mangle_19.Conv
  cv2 : __torch__.models.common.___torch_mangle_23.Conv
  def forward(self: __torch__.models.common.Bottleneck,
    argument_1: Tensor) -> Tensor:
    _19 = (self.cv2).forward((self.cv1).forward(argument_1, ), )
    return torch.add(argument_1, _19, alpha=1)
class SPP(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  cv1 : __torch__.models.common.___torch_mangle_121.Conv
  cv2 : __torch__.models.common.___torch_mangle_125.Conv
  m : __torch__.torch.nn.modules.container.ModuleList
  def forward(self: __torch__.models.common.SPP,
    argument_1: Tensor) -> Tensor:
    _20 = self.cv2
    _21 = getattr(self.m, "2")
    _22 = getattr(self.m, "1")
    _23 = getattr(self.m, "0")
    _24 = (self.cv1).forward(argument_1, )
    _25 = [_24, (_23).forward(_24, ), (_22).forward(_24, ), (_21).forward(_24, )]
    input = torch.cat(_25, 1)
    return (_20).forward(input, )
class Concat(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  def forward(self: __torch__.models.common.Concat,
    argument_1: Tensor,
    argument_2: Tensor) -> Tensor:
    input = torch.cat([argument_1, argument_2], 1)
    return input
