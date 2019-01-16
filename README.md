# CapsGCNN
A PyTorch implementation of Capsule Graph Convolutional Neural Network based on the paper 
[Capsule Graph Convolutional Neural Network For Graph Classification]().

## Requirements
* [Anaconda](https://www.anaconda.com/download/)
* PyTorch
```
conda install pytorch torchvision -c pytorch
```
* PyTorchNet
```
pip install git+https://github.com/pytorch/tnt.git@master
```
* capsule-layer
```
pip install git+https://github.com/leftthomas/CapsuleLayer.git@master
```

## Datasets

The datasets are collected from [perceptual-reflection-removal](https://github.com/ceciliavision/perceptual-reflection-removal)
and [CEILNet](https://github.com/fqnchina/CEILNet).
Download the datasets from [BaiduYun](https://pan.baidu.com/s/1PJuEvmFdpuJIZwtNU6NgtQ) 
or [GoogleDrive](https://drive.google.com/open?id=1abYah24PZKQS8K9G3Xsd_6a8Raptp30a), and extract them into `data` directory.

## Usage
### Train Model
```
python -m visdom.server -logging_level WARNING & python main.py --data_type FashionMNIST --use_da --num_epochs 300
optional arguments:
--data_type                   dataset type [default value is 'MNIST'](choices:['MNIST', 'FashionMNIST', 'SVHN', 'CIFAR10', 'CIFAR100', 'STL10'])
--use_da                      use data augmentation or not [default value is False]
--num_iterations              routing iterations number [default value is 3]
--batch_size                  train batch size [default value is 100]
--num_epochs                  train epochs number [default value is 100]
```
Visdom now can be accessed by going to `127.0.0.1:8097/env/$data_type` in your browser, `$data_type` means the dataset type which you are training.
