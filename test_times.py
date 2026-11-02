from times import time_range, compute_overlap_time
import pytest

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
    assert result == expected

def test_no_overlap():
    # 测试1：两个完全不重叠
    range_a = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range_b = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(range_a, range_b)
    # 没有重叠，返回空列表
    assert result == []

def test_multiple_intervals_overlap():
    # 测试2：两个范围都切成多段，存在重叠
    range_a = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=3, gap_between_intervals_s=300)
    range_b = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", number_of_intervals=2, gap_between_intervals_s=120)
    result = compute_overlap_time(range_a, range_b)
    # 我们只断言重叠结果不为空（你也可以算出精确expected）
    assert len(result) > 0

def test_end_exactly_equal_to_start():
    # 测试3：A结束时间 == B开始时间，刚好相接，无重叠
    range_a = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range_b = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(range_a, range_b)
    # 时间点重合不算重叠，结果为空
    assert result == []

    def test_reversed_time_range_raises_error():
        # 结束时间早于开始时间：时间倒流
        with pytest.raises(ValueError) as excinfo:
            time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        # 可选：额外校验报错信息是否匹配（推荐，老师很喜欢这个写法）
        assert "End time" in str(excinfo.value)
        assert "earlier than start time" in str(excinfo.value)

if __name__ == "__main__":
    test_given_input()
