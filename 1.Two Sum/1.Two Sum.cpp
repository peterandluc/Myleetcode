class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        /*
        same idea with python version
        */
        std::unordered_map<int, int> hash_map;
        std::vector<int> result(2);

        for(int i=0; i<nums.size(); i++)
        {
            int value = target - nums[i];
            if(hash_map.find(value) != hash_map.end())
            {
                result[0] = hash_map[value];
                result[1] = i;
                return result;
            }
            hash_map[nums[i]] = i;

        }
        return result;
    }
};
