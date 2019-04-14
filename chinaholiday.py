'''
chinaholiday
https://github.com/qinst64/chinaholiday
'''
import re
import configparser
import datetime

__version__ = '1.0'

PH = '''
[note]
name: china public holidyas
url: http://www.gov.cn/zhengce/index.htm
note: 为方便检查节假日命名和书写严格按照官网,!表示周末调为上班 

[2019]
元旦: 1月1日
春节: 2月4日-10日, !2月2日, !2月3日
清明节: 4月5日
劳动节: 5月1日-4日, !4月28日, !5月5日
端午节: 6月7日
中秋节: 9月13日
国庆节: 10月1日-7日, !9月29日, !10月12日

[2018]
元旦: 1月1日
春节: 2月15日-21日, !2月11日, !2月24日
清明节: 4月5日-7日, !4月8日
劳动节: 4月29日-5月1日, !4月28日
端午节: 6月18日
中秋节: 9月24日
国庆节: 10月1日-7日, !9月29日, !9月30日
元旦2019: 12月30日-31日, !12月29日

[2017]
元旦: 1月1日, 1月2日 
春节: 1月27日-2月2日, !1月2日, !2月4日
清明节: 4月2日-4日, !4月1日
劳动节: 5月1日
端午节: 5月28日-30日, !5月27日
中秋节、国庆节: 10月1日-8日, !9月30日

[2016]
元旦: 1月1日 
春节: 2月7日-2月13日, !2月6日, !2月14日
清明节: 4月4日
劳动节: 5月1日, 5月2日
端午节: 6月9日-11日, !6月12日
中秋节: 9月15日-17日, !9月18日
国庆节: 10月1日-7日, !10月8日, !10月9日

[2015]
元旦: 1月1日-3日, !1月4日
春节: 2月18日-24日, !2月15日, !2月28日
清明节: 4月5日, 4月6日
劳动节: 5月1日
端午节: 6月20日, 6月22日
中秋节: 9月27日
国庆节: 10月1日-7日, !10月10日
中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日: 9月3日-5日, !9月6日

[2014]
元旦: 1月1日
春节: 1月31日-2月6日, !1月26日, !2月8日
清明节: 4月5日, 4月7日
劳动节: 5月1日-3日, !5月4日
端午节: 6月2日
中秋节: 9月8日
国庆节: 10月1日-7日, !9月28日, !10月11日

[2013]
元旦: 1月1日-3日, !1月5日，!1月6日
春节: 2月9日-15日, !2月16日, !2月17日
清明节: 4月4日-6日, !4月7日
劳动节: 4月29日-5月1日, !4月27日, !4月28日
端午节: 6月10日-12日, !6月8日, !6月9日
中秋节: 9月19日-21日, !9月22日
国庆节: 10月1日-7日, !9月29日, !10月12日

[2012]
元旦: 1月1日-3日
春节: 1月22日-28日, !1月21日, !1月29日
清明节: 4月2日-4日, !3月31日, !4月1日
劳动节: 4月29日-5月1日, !4月28日
端午节: 6月22日-24日
中秋节、国庆节: 9月30日-10月7日, !9月29日

[2011]
元旦: 1月1日-3日
春节: 2月2日-8日, !1月30日, !2月12日
清明节: 4月3日-5日, !4月2日
劳动节: 4月30日-5月2日
端午节: 6月4日-6月6日
中秋节: 9月10日-12日
国庆节: 10月1日-7日, !10月8日, !10月9日
2012元旦: !12月31日

[2010]
元旦: 1月1日-3日
春节: 2月13日-19日, !2月20日, !2月21日
清明节: 4月3日-5日
劳动节: 5月1日-5月3日
端午节: 6月14日-16日, !6月12日, !6月13日
中秋节: 9月22日-24日, !9月19日, !9月25日
国庆节: 10月1日-7日, !9月26日, !10月9日

[2009]
元旦: 1月1日-3日, !1月4日
春节: 1月25日-31日, !1月24日, !2月1日
清明节: 4月4日-6日
劳动节: 5月1日-5月3日
端午节: 5月28日-30日, !5月31日
国庆节、中秋节: 10月1日-8日, !9月27日, !10月10日

[2008]
元旦: 1月1日
春节: 2月6日-12日, !2月2日, !2月3日
清明节: 4月4日-6日
五一国际劳动节: 5月1日-3日, !5月4日
端午节: 6月7日-9日
中秋节: 9月13日-15日
国庆节: 9月29日-10月5日, !9月27日, !9月28日

[2007]
元旦: 1月1日-3日
春节: 2月18日-24日, !2月17日, !2月25日
五一: 5月1日-7日, !4月28日, !4月29日
十一: 10月1日-7日, !9月29日, !9月30日
元旦2: !12月29日, 12月30日-31日 

[2006]
元旦2007: !12月30日, !12月31日
'''


class ChinaHoliday:
    '''
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
    '''

    def __init__(self):
        self.public_holidays = []
        self._load()

    @staticmethod
    def _parse_day(string: str) -> list:
        '''
        转换
        "4月30日" -> True, [4, 30, 4, 30]
        "4月30日-31日" -> True, [4, 30, 4, 31]
        "4月30日-5月1日" -> True, [4, 30, 5, 1]
        "!4月30日" -> False, [4, 30, 4, 30]
        '''
        is_ph = not string.strip().startswith('!')
        m = re.match(r"(\d+月)(\d+日)-(\d+月)?(\d+日)", string.strip())
        if m:
            res = m.groups(default=m.groups()[0])
        else:
            m = re.search(r"(\d+)月(\d+)日", string)
            res = m.groups() * 2
        return is_ph, [int(x.replace("月", "").replace("日", "")) for x in res]

    def _load(self, ph=PH):
        config = configparser.ConfigParser()
        config.read_string(ph.replace(" ", ""))
        for year in (y for y in config.sections() if y.isdigit()):
            for name, desc in config[year].items():
                for x in desc.split(','):
                    is_ph, p = self._parse_day(x)
                    start = datetime.date(int(year), p[0], p[1])
                    end = datetime.date(int(year), p[2], p[3])
                    self.public_holidays.extend(
                        [(start + datetime.timedelta(n), is_ph, name)
                         for n in range(int((end - start).days) + 1)])

    def _to_datetime(self, day) -> datetime.date:
        '''转换day为datetime.date'''
        if isinstance(day, datetime.date):
            pass
        elif isinstance(day, str):
            if day.isdigit() and len(day) == 8:
                day = datetime.date(
                    int(day[0:4]), int(day[4:6]), int(day[6:8]))
            elif day == "today":
                day = self.today
            elif day == "tomorrow":
                day = self.today + datetime.timedelta(1)
            elif day == "yesterday":
                day = self.today - datetime.timedelta(1)
            else:
                raise Exception("wrong input format")
        else:
            raise Exception("wrong input format")
        return day

    @property
    def today(self):
        '''return today'''
        return datetime.date.today()

    def get_info(self, day):
        '''
        day: 日期格式见 print(ChinaHoliday.__doc__)
        return: {
            day: datetime格式,
            is_public_holiday: 是否法定节假日,
            public_holiday_name: 法定节假日名字,
            is_holiday: 是否节假日,
            holiday_name: 节假日名字
        }
        '''
        res = {
            "day": self._to_datetime(day)
        }
        for x in self.public_holidays:
            if x[0] == res["day"]:
                res["is_public_holiday"] = x[1]
                res["public_holiday_name"] = "工作日(" + \
                    x[2]+"调休)" if x[1] is False else x[2]
                res["is_holiday"] = res["is_public_holiday"]
                res["holiday_name"] = res["public_holiday_name"]
                break
        else:
            res["is_public_holiday"] = None
            res["public_holiday_name"] = "非法定节假日"
            res["is_holiday"] = res["day"].weekday() >= 5
            res["holiday_name"] = "周末" if res["day"].weekday() >= 5 else "工作日"
        return res

    def is_public_holiday(self, day):
        '''是否是法定节假日, day日期格式见 print(ChinaHoliday.__doc__)'''
        return self.get_info(day)["is_public_holiday"]

    def is_holiday(self, day):
        '''是否是节假日, day日期格式见 print(ChinaHoliday.__doc__)'''
        return self.get_info(day)["is_holiday"]

    def is_workday(self, day):
        '''是否是工作日, 与self.is_holiday相反, day日期格式见 print(ChinaHoliday.__doc__)'''
        return not self.get_info(day)["is_holiday"]


if __name__ == "__main__":
    ch = ChinaHoliday()
    assert ch.is_holiday("20190404") is False
    assert ch.is_holiday("20190405") is True
