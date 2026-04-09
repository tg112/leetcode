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

        # ex) [1, 10, 5, 2 ,6, 7]
        set_nums = set(nums)
        longest = 0
        
        # num = 5
        for num in set_nums:
            # targetの1つ前の数字からcount upする
            if num - 1 not in set_nums: 
                current_num = num # 5
                length = 1

                while current_num + 1 in set_nums: # 6 -> 7
                    current_num += 1 # 6 -> 7
                    length += 1 # 2 -> 3

                longest = max(longest, length)

