class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路1：这就好比狼人杀猎人死前要带走一个，为了使整体损失最小，那么就带走和它最相近的一个：
        #       取小必然牺牲一个大的数，希望牺牲的这个数不要太大，那这个“较大数”自然就是每一对中和较小数差值最小的数
        return sum(sorted(nums)[::2])
