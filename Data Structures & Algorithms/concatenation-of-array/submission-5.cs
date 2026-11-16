public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int length = nums.Length;
        int[] result = new int[length * 2];
        for (int i = 0; i < length; i++)
        {
            result[i] = nums[i];
            result[length + i] = nums[i];
        }
        return result;
    }
}