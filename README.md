# chinaholiday
单文件版中国节假日, 支持2007-2019, python3

## 快速上手
```python
#引入包
from chinaholiday import ChinaHoliday
ch = ChinaHoliday()

ch.get_info("20190427")
#返回: 
# {
# 'day': datetime.date(2019, 4, 27),
# 'is_public_holiday': False,
# 'public_holiday_name': '非法定节假日',
# 'is_holiday': True,
# 'holiday_name': '周末'
# }

import datetime
ch.get_info(datetime.date(2019, 4, 28))
#返回:
#{
# 'day': datetime.date(2019, 4, 28),
# 'is_public_holiday': False,
# 'public_holiday_name': '工作日(劳动节调休)',
# 'is_holiday': False,
# 'holiday_name': '工作日(劳动节调休)'
# }

ch.is_public_holiday("today")
# 返回: True公共节假日, False周末调为上班, None非公共节假日

ch.is_holiday("tomorrow")
# 返回: True放假, False不放假
```


## 详细使用
使用`print(ChinaHoliday.__doc__)`查看详细文档
```python
# 判断某天是否是公共节假日/休息日/工作日 (支持2007年-2019年)
# e.g.
day = "20180101" # or datatime.day(2018, 1, 1), or 'today'/'tomorrow'/'yesterday'
ch = ChinaHoliday()
# methods
ch.get_info(day) #获取完整信息
ch.is_public_holiday(day) # True公共节假日, False周末调为上班, None非公共节假日
ch.is_holiday(day) # True放假, False不放假
ch.is_workday(day) # is_holiday(day)反过来
# properties
ch.public_holidays #所有公共节假日和调休, 格式(day, is_public_holiday, name)
ch.today #今天(type datatime.date)
```

## 修改
原始数据在python中, 以ini方式整理, 非常方便修改