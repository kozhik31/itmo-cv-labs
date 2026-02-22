import matplotlib.pyplot as plt


def plot_two_img(img1, img2, cmap='viridis'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 6))
    ax[0].imshow(img1, cmap=cmap)
    ax[0].set_title("My")
    ax[0].axis("off")
    ax[1].imshow(img2, cmap=cmap)
    ax[1].set_title("CV")
    ax[1].axis("off")
    plt.show()