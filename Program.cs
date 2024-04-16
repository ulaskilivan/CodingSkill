using System;
/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 */
class Program
{
    public static int[] TwoSum(int []nums,int target)
    {
        int[] newArray = new int[2];
        for (int i = 0; i < nums.Length-1; i++)
            
        {
            if(nums[i] + nums[i + 1] == target)
            {
                nums[0] = nums[i];
                nums[1] = nums[i + 1];
                break;
                
            }
        }
        return nums;
    }
    public static void Main(String[] args)
    {
        int[] numbers=TwoSum(new int[]{4,3,7,9,2,1},16);

        Console.WriteLine(numbers[0]+" "+numbers[1]);
    }
}