from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    # 计算结果
    result = compute_overlap_time(large, short)

    # 运行原代码得到的输出，作为 expected
    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    print("Result:", result)
    print("Expected:", expected)
    print("Match:", result == expected)

if __name__ == "__main__":
    test_given_input()
