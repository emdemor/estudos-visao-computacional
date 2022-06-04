from PIL import Image, ImageOps
import numpy as np
import sys


def gray_quantization(data: np.array, b: int) -> np.array:
    """Quantiza uma imagem digital em escala de cinza
    para um número de bits especificado de acordo com
    o parâmetro b.

    Parameters
    ----------
    data : np.array
        Um array de numpy de shape (n,n), onde n é a amostragem da imagem
    b : int
        Um número inteiro especificando o número de bits

    Returns
    -------
    np.array
        Returna um array numpy de shape (n,n) com as cores quantizadas
    """
    i_min = data.min()
    i_max = data.max()
    step = (i_max - i_min) / (2 ** b - 1)
    q = (step * np.round((data - i_min) / step)).astype("uint8")
    return q


def main():
    """ Main function for application """

    # Recebendo o número de bits pela linha de comeando
    try:
        b = int(sys.argv[1])
    except:
        b = 2

    # Carrega a imagem
    image = Image.open("images/tucano.png")

    # Converte em escala de cinza
    gray_image = ImageOps.grayscale(image)

    # Converte em um array de numpy
    gray_image_array = np.asarray(gray_image)

    # Aplica a quantização
    quant_image_array = gray_quantization(gray_image_array, b)

    # Converte em um objeto PIL.Image.Image
    quant_image = Image.fromarray(quant_image_array)

    # Salva o resultado
    quant_image.save(f"images/quant_image_{b}_bits.png")


if __name__ == "__main__":

    main()
