def longestConsecutive(nums: list[int]) -> int:
        # map = {}
        # set_nums = set(nums)
        # longest_length = 0
        # for num in set_nums:
        #     map[num] = False

        # for num in set_nums:
        #     current_length = 1

        #     next_num = num + 1
        #     while next_num in map and not map[next_num]:
        #         current_length += 1
        #         map[next_num] = True
        #         next_num += 1

        #     prev_num = num - 1
        #     while prev_num in map and not map[prev_num]:
        #         current_length += 1
        #         map[prev_num] = True
        #         prev_num -= 1
        #     longest_length = max(longest_length, current_length)

        # return longest_length

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 「連続のスタート」だけ処理する
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)
        return longest

