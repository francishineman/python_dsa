#!/usr/bin/env python3

target = 9
nums = [2,7,10,13,15,22,45]

def brute_force_solution(tgt, nms):
    for i in nms:
        for j in nms:
            if i + j == tgt:
                return([i, j])

def main():
    answer = brute_force_solution(target, nums)
    print(answer)

if __name__ == "__main__":
    main()
