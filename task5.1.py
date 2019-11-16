def solution(A, B):
    lst_alive = []
    alive =0
    for index in range(len(A)):
        if B[index] == 0:
            if lst_alive == []:
                alive += 1
            elif lst_alive[-1] > A[index]:
                continue
            else:
                active = True
                while active:
                    lst_alive.pop()
                    if lst_alive == []:
                        alive += 1
                        active = False
                    elif lst_alive[-1] > A[index]:
                        active = False

        if B[index] == 1:
            lst_alive.append(A[index])

    res = len(lst_alive) + alive
    return res