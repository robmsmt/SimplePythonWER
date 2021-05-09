from typing import List


def levenshtein(ground_truth: List[str], result: List[str]) -> int:
    '''
    Calculates the Levenshtein distance between ground_truth and result.

    :param ground_truth: List[str]
    :param result: List[str]
    :return: edit_distance: int

    '''
    len_gt, len_res = len(ground_truth), len(result)
    if len_gt > len_res:
        # Make sure len_gt <= len_res, to use O(min(len_gt,len_res)) space
        ground_truth, result = result, ground_truth
        len_gt, len_res = len_res, len_gt

    fixed_zeros = [0]*len_gt
    current = list(range(len_gt+1))
    for i in range(1, len_res+1):
        previous, current = current, [i]+fixed_zeros  # reset score row all to zero's
        for j in range(1, len_gt+1):
            current[j] = min(previous[j]+1,  # add
                             current[j-1]+1,  # delete
                             previous[j-1]+1 if ground_truth[j-1] != result[i-1] else previous[j-1])  # sub
    return current[len_gt]


def wer(ground_truth: str, result: str) -> float:
    r"""
    The WER is defined as the editing/Levenshtein distance on word level
    divided by the amount of words in the original text.
    In case of the original having more words (N) than the result and both
    being totally different (all N words resulting in 1 edit operation each),
    the WER will always be 1 (N / N = 1).
    """
    # The WER is calculated on word (and NOT on character) level.
    # Therefore we split the strings into words first:
    original = ground_truth.split()
    result = result.split()
    return levenshtein(original, result) / float(len(original))


def ler(ground_truth: str, result: str) -> float:
    r"""
    as above but not splitting on word
    """
    return levenshtein(ground_truth, result) / float(len(ground_truth))

