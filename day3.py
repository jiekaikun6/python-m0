from utils import build_messages

def sum_amounts()->float:
    total=0.0

    while True:
        s=input("请输入金额（直接回车结束）：")
        if s=="":
            break
        try:
            amount=float(s)
        except ValueError:
            print ("输入的不是数字，请重新输入。")
            continue
        total += amount

    return total

if __name__=="__main__":
    print("==测试buila_messages==")
    print("无 system:",build_messages("你好"))
    print("有system:",build_messages("你好",system="你是一个财务助手"))

    print()
    print("==测试sum_amouts==")
    total = sum_amounts()
    print(f"合计金额:{total}")


#1.放while外面才能累计，放里面就每次清零，只会输出最后一个
#2.转化为小数，其他格式不能转化的，执行下一条让用户重新输入，避免奔溃或者结束
#3.返回一条，因为空值为假，不返回
#4.自己文件下执行，被其他文件调用后不执行
#5.
          
