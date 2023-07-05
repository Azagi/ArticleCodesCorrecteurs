from math import ceil, log


def text_to_binary(text: str) -> list[int]:
    """Conversion d'un text en sa representation binaire en UTF-8."""
    chars = bytes(text, 'UTF-8')
    result = []
    for c in chars:
        n = format(c, '08b')
        for i in n:
            result.append(1 if i == '1' else 0)
    return result


def required_parity_bits(length: int) -> int:
    """Calcule le nombre de bits de parité requis encodée des données de longueur length."""
    b = ceil(log(length, 2))
    n = 2 ** b
    while (n - b) < length:
        b += 1
        n *= 2
    return b


def text_to_hamming(text: str) -> list[int]:
    """Convertie un text en sa representation binaire en UTF-8 avec les bits de parité correspondants."""
    data = text_to_binary(text)
    length = len(data)
    b = required_parity_bits(len(data))

    code = [0] * (length + b)
    bits = [0] + [1 << i for i in range(b - 1)]
    j = 0
    for i in range(0, len(code)):
        if i not in bits:  # Place only data bits
            code[i] = data[j]
            j += 1
            for b in bits:  # Update parity bits
                if b == 0 or (i & b) != 0:
                    code[b] ^= code[i]
    return code


def find_error(data: list[int]) -> int:
    """Trouve l'erreur dans un code de Hamming, si aucune erreur n'est trouvée retourne 0."""
    res = 0
    for (i, b) in enumerate(data):
        if b == 1:
            res ^= i
    return res


def correct_errors(data: list[int]) -> list[int]:
    """Corrige les erreurs dans un code de Hamming, si aucune erreur n'est trouvée retourne le même code."""
    error = find_error(data)
    while error != 0:
        data[error] ^= 1
        error = find_error(data)
    return data


def remove_parity_bits(data: list[int]) -> list[int]:
    """Enlève les bits de parité d'un code de Hamming."""
    b = required_parity_bits(len(data))
    bits = [0] + [1 << i for i in range(b - 1)]
    return [data[i] for i in range(len(data)) if i not in bits]


def hamming_code_to_text(code: list[int]) -> str:
    """Convertie un code de Hamming en un text, le text doit avoir été encodé en UTF-8."""
    code = correct_errors(code)
    data = remove_parity_bits(code)

    octets = []
    i, length = 0, len(data)
    while i < length:
        c, j = 0, 0
        while j < 8 and i < length:
            c = (c << 1) | data[i]
            i += 1
            j += 1
        octets.append(c)
    return bytes(octets).decode('UTF-8')
