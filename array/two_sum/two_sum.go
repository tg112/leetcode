func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int) // value -> index

    for i, num := range nums {
        diff := target - num

        if idx, ok := numMap[diff]; ok {
            return []int{i, idx}
        }

        numMap[num] = i
    }

    return []int{}
}

