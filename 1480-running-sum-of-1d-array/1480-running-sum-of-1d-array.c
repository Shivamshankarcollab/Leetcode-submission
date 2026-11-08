/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* arr = malloc((numsSize+1) * sizeof(int));
    for (int i = 0; i < numsSize ; i++)
    {
        if ( i==0  )
        {
            arr[0] = nums[i];
        }
        else
        {
            arr[i] = nums[i] + arr[i-1];
        }
    }
    *returnSize = numsSize;
    return arr;
    
}