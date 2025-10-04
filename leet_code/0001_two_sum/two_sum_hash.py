#!/usr/bin/env python3

target = 9
nums = [2,7,10,13,15,22,45]

def hash_table_algorithm(tgt, nms):
    d = {}

    for i in nums:
        compliment = tgt - i
        if i in d:
            return(i,compliment)
        else:
            d[compliment] = i


def main():
    answer = hash_table_algorithm(target, nums)
    print(answer)

if __name__ == "__main__":
    main()
