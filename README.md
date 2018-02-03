# CCN
Convolutional Capsule Network

## Requirements
* [Anaconda](https://www.anaconda.com/download/)
* PyTorch
```
conda install pytorch torchvision cuda90 -c pytorch
```
* PyTorchNet
```
pip install git+https://github.com/pytorch/tnt.git@master
```
* tqdm
```
conda install tqdm
```

## Usage
```
python -m visdom.server -logging_level WARNING & python main.py
optional arguments:
--data_type                   dataset type [default value is 'MNIST'](choices:['MNIST', 'FashionMNIST', 'SVHN', 'CIFAR10', 'CIFAR100', 'STL10'])
--use_data_augmentation       use data augmentation or not [default value is 'yes'](choices:['yes', 'no'])
--with_routing                use routing algorithm or not [default value is 'no'](choices:['yes', 'no'])
--batch_size                  train batch size [default value is 64]
--num_epochs                  train epochs number [default value is 100]
```
Visdom now can be accessed by going to `127.0.0.1:8097/env/$data_type` in your browser, `$data_type` means the dataset type which you are training.
