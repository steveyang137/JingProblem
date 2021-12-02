import random

times = input("times: ")
for i in range(int(times)):
    pTree = round(random.random() * 2, 1) * 10 ** 3
    pMetal = round(random.random() * 20, 1) * 10 ** 3 + pTree
    vTree = round(random.random() * 10, 1)
    mTree = pTree * vTree
    mMetal = random.randint(2 * 10 ** 4 + 5, 10 * 10 ** 5) - mTree
    vMetal = mMetal / pMetal
    print("一只鲸鱼总容积为 {} 立方米，所能承载的物质质量最大为 {} 千克，现在要用树和金属放满整只鲸鱼。已知树的密度为 {} 千克每立方米，金属的密度为 {} 千克每立方米，求应放质量为多少的树和金属。"
          .format(vTree + vMetal, mTree + mMetal, pTree, pMetal))
    print("参考答案：树质量为{:2f}千克，金属质量为{:2f}千克，树体积为{:2f}立方米，金属体积为{:2f}立方米。".format(mTree, mMetal, vTree, vMetal))

print("Done.")
