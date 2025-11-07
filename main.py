# 在这个文件中编写代码
def has_duplicates(lst):
   return len(lst) !=len(sat()lst)
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],          # 无重复
        [1, 2, 2],          # 有重复
        ["a", "b", "a"],    # 字符串重复
        []                   # 空列表
    ]
   for i, case in enumerate(test_cases):
         result = has_duplicates(case)
         print("测试用例 {i + 1}: {case}，有重复元素：{result}")
