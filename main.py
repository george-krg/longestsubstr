""" Defines the longest substring function and asserts the calculation with given examples """


def longest_match(string_1: str, string_2: str):
    """Gets as input 2 strings and calculates the longest substring common to both of them"""

    max_len = 0
    for i in range(len(string_1)):
        for j in range(len(string_1), i - 1, -1):
            if string_2.find(string_1[i:j]) != -1:
                cur_len = j - i
                if cur_len > max_len:
                    max_len = cur_len
                break
    return max_len


assert (
    longest_match(
        "AAAAAAAAAAAAAAAAAAAAACCCGGGGGGGGGGGGG",
        "AAAACCCGGGGGGGGGGGGGGGGTTTTTTTTTGGGGGGGGGGGG",
    )
    == 20
)
assert longest_match("CAT", "AT") == 2
assert (
    longest_match(
        "TCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTCTC",
        "GAGAGGAGAAAGAGAGAGAAGAGAGGAGGAAAGAGAGAGAAAAGAGGGAA",
    )
    == 0
)
assert (
    longest_match(
        "ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTAC",
        "GTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT",
    )
    == 48
)
assert longest_match("TC", "CATCAT") == 2
assert longest_match("CGCATTAGATTCAGAG", "CGCATGAGTAGATTC") == 7
assert longest_match("GCGACCC", "AGCGAA") == 4
assert longest_match("ABCD", "BC1234") == 2
assert longest_match("A", "AAAA") == 1
assert longest_match("12345", "5678901234") == 4
assert longest_match("ABBABBAABBAA", "BABA") == 3
