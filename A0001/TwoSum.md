# 1338 Easy-TwoSum
>Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## 解題:
*給一組陣列找出陣列中兩個數相加等於目標值。
而且剛好只有一個解，最後回傳兩數索引之陣列 ex:[0,1]。*

### **作法1:**
*使用兩個for回圈將每個陣列都加一次(時間過長)*
### **作法2:**
*Hash, 在python中可以用dict, 
在golang中可以用map(注意golang中為無序),
在每次map確認當下 target - num 是否在map中,
找到則return結果，沒找到則放入map中{num:index}。*