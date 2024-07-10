class Upsample(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  def forward(self: __torch__.torch.nn.modules.upsampling.Upsample,
    argument_1: Tensor) -> Tensor:
    _0 = ops.prim.NumToTensor(torch.size(argument_1, 2))
    _1 = torch.to(_0, 6, False, False, None)
    _2 = torch.to(CONSTANTS.c0, torch.device("cpu"), 6, False, False, None)
    _3 = torch.to(torch.mul(_1, torch.detach(_2)), 6, False, False, None)
    _4 = int(torch.floor(_3))
    _5 = ops.prim.NumToTensor(torch.size(argument_1, 3))
    _6 = torch.to(_5, 6, False, False, None)
    _7 = torch.to(CONSTANTS.c0, torch.device("cpu"), 6, False, False, None)
    _8 = torch.to(torch.mul(_6, torch.detach(_7)), 6, False, False, None)
    _9 = torch.upsample_nearest2d(argument_1, [_4, int(torch.floor(_8))], 2., 2.)
    return _9
