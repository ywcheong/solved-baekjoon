def make_permutation(n):
    pass

def next_permutation(sequence):
    # 당연종료: 자명한 수열
    if len(sequence) == 1:
        return None

    dec_index = len(sequence) - 1
    while 0 <= dec_index:
        pass

    # 순열이 뒤에서부터 단조증가라는 것은 마지막 순열이라는 것
    if dec_index == -1:
        return None
    
    # [dec_index - 1]과 [dec_index]를 swap
    sequence[dec_index - 1]