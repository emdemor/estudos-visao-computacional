# Lista de Exercícios 1 - Desafio

A função de quantização está definida no arquivo `quantization.py` e é definida como:

```python
def gray_quantization(data: np.array, b: int):
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
```

Temos em `images` uma figura chama `tucano.png` que serve para testar a função. Para isso, basta rodar:

```bash
python3 quantization.py 3
```

onde o último número indica quantidade desejada de bits. O resultado estará dentro da pasta `images`. Uma alternativa é trabalhar no notebook Jupyter `image-quantization.py`. 