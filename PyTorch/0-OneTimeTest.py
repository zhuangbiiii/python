# Some one time test python functions
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt

funcindex = 4

# function 1, test the torch.nn.conv2d
if funcindex == 1:
    x = torch.nn.Conv2d(2, 8, 3, 1)
    random_data = torch.rand((1, 2, 5, 7))
    print(random_data)
    x = x(random_data)
    print(x)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Input")
    plt.imshow(random_data[0, 0].detach().numpy(), cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("Output")
    plt.imshow(x[0, 0].detach().numpy(), cmap='gray')
    plt.show()
    ## summary:conv2d.parameter.1 == input data.parameter.2, the rest is just like intuition

# function 2, see what is the device
if funcindex == 2:
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"Using {device} device")

# function 3, get pytorch
if funcindex == 3:
    import requests
    def get_torch_packages(url):
        response = requests.get(url)
        if response.status_code != 200:
            print(
                f"Failed to retrieve the page. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        torch_packages = []
        for link in links:
            href = link.get('href')
            if href and 'torch' in href:
                torch_packages.append(href)

        return torch_packages


    url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
    torch_packages = get_torch_packages(url)

    print("Packages related to torch:")
    for package in torch_packages:
        print(package)

# function 4, see can we load deepseek model
if funcindex == 4:
    import transformers
    # model path
    model_path = "deepset/sentence_bert"