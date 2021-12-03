import random
import fractions

times = input("How many times do you wan to try: ")
for i in range(int(times)):
    print("\n", i + 1, ":", end='')
    pMetal = random.randint(20, 200) * 100
    pTree = random.randint(5, 15) * 100
    v = random.randint(1, 250)
    m = random.randint(int(pTree/100)*v, int(pMetal/100)*v) * 100
    vMetal = fractions.Fraction(m - pTree * v, pMetal - pTree)
    vTree = v - vMetal
    # if vMetal <= 0 or vTree <= 0:
    #     print("FAILED")
    #     continue
    mMetal = pMetal * vMetal
    mTree = pTree * vTree
    vMetalValue = round(vMetal.numerator/vMetal.denominator, 2)
    vTreeValue = round(vTree.numerator/vTree.denominator, 2)
    mMetalValue = round(mMetal.numerator/mMetal.denominator, 2)
    mTreeValue = round(mTree.numerator/vTree.denominator, 2)
    print("一只鲸鱼总容积为 {} 立方米，所能承载的物质质量最大为 {} 千克，现在要用树和金属放满整只鲸鱼。已知树的密度为 {} 千克每立方米，金属的密度为 {} 千克每立方米，求应放质量为多少的树和金属。"
          .format(v, m, pTree, pMetal))
    print("参考答案：树质量为{}千克，金属质量为{}千克，树体积为{}立方米，金属体积为{}立方米。".format(mTreeValue, mMetalValue, vTreeValue, vMetalValue))

print("Done.")
