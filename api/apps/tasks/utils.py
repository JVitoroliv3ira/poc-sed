from typing import List


def split_list_into_sublists(lst: List, x: int) -> List[List]:
    if x <= 0:
        raise ValueError("O valor de x deve ser maior que 0 e menor ou igual ao tamanho da lista.")

    if x > len(lst):
        x = len(lst)

    sublists = [lst[i:i + x] for i in range(0, len(lst), x)]

    return sublists
