

def test1():

    from matplotlib import pyplot as plt

    x = range(2,26,2)
    y = range(12)

    # 1. 设置图片大小
    # 只需要实例化一次，后续plt 会根据这个配置生成图形
    plt.figure(figsize=(10,8),dpi=100)
    print(x)
    print(y)

    #plt.savefig("./ret.png")
    # # 保存为矢量格式
    #plt.savefig("./ret.svg")
    # 绘制x轴的刻度
    plt.plot(x,y)
    import numpy as np
    plt.xticks(range(2,30))

    plt.savefig("./ret.png")
    #plt.show()



if __name__ == '__main__':
    test1()