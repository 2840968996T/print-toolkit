import sys

def split_pages(start, end):
    """
    将页码范围拆分为第一部和第二部分
    第一部：起始页所在的奇偶类别
    第二部：另一类别
    """
    first_is_odd = (start % 2 == 1)
    
    first_part = []
    second_part = []
    
    for page in range(start, end + 1):
        if (page % 2 == 1) == first_is_odd:
            first_part.append(page)
        else:
            second_part.append(page)
    
    return first_part, second_part

def main():
    if len(sys.argv) != 3:
        print("使用方法：python print_helper.py <起始页> <结束页>")
        print("示例：python print_helper.py 1 10")
        print("示例：python print_helper.py 27 50")
        return
    
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        if start > end:
            print("错误：起始页不能大于结束页")
            return
        
        first, second = split_pages(start, end)
        
        total_pages = end - start + 1
        first_count = len(first)
        second_count = len(second)
        
        print(f"\n页码范围：{start}-{end}（共{total_pages}页）")
        print("-" * 50)
        print(f"第一部分（先打）：{','.join(map(str, first))}")
        print(f"第二部分（翻面后打）：{','.join(map(str, second))}")
        print("-" * 50)
        
        if first_count > second_count:
            diff = first_count - second_count
            print(f"⚠️  提示：第一部分比第二部分多{diff}张纸")
            print(f"   翻面时，请从最下面抽出{diff}张纸（这些纸背面将是空白）")
            print(f"   把剩下的{second_count}张纸翻面放回，打印第二部分")
        else:
            print("✓ 两部分页数相等，整摞翻面即可")
            
    except ValueError:
        print("错误：请输入有效的数字")

if __name__ == "__main__":
    main()