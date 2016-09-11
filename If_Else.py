# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#  低于18.5：过轻
#  18.5-25：正常
#  高于38：严重肥胖
str = input("请输入你的体重: ")
weight = float(str)
if weight < 18.5:
    print("你的体重过轻，请加强锻炼")
elif 18.5 <= weight and weight <= 25:
    print("你的体重正常")
else:
    print("你的体重过于肥胖")
