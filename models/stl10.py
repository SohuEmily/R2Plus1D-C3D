from capsule_layer import CapsuleLinear
from torch import nn

from resnet import resnet20


class STL10CapsuleNet(nn.Module):
    def __init__(self, num_iterations=3):
        super(STL10CapsuleNet, self).__init__()

        self.conv1 = nn.Conv2d(3, 16, kernel_size=7, stride=2, padding=3, bias=False)
        layers = []
        for name, module in resnet20().named_children():
            if name == 'conv1' or isinstance(module, nn.AvgPool2d) or isinstance(module, nn.Linear):
                continue
            layers.append(module)
        self.features = nn.Sequential(*layers)
        self.classifier = nn.Sequential(CapsuleLinear(out_capsules=10, in_length=64, out_length=16, in_capsules=12 * 12,
                                                      share_weight=False, routing_type='contract',
                                                      num_iterations=num_iterations))

    def forward(self, x):
        out = self.conv1(x)
        out = self.features(out)

        out = out.permute(0, 2, 3, 1)
        out = out.contiguous().view(out.size(0), -1, 64)

        out = self.classifier(out)
        classes = out.sum(dim=-1)
        return classes


if __name__ == '__main__':
    model = STL10CapsuleNet()
    for m in model.named_children():
        print(m)
