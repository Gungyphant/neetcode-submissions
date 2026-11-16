public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int length = nums.Length;
        int[] result = new int[length * 2];
        for (int i = 0; i < length; i++)
        {
            int val = nums[i];
            result[i] = val;
            result[length + i] = val;
        }
        return result;
    }
}