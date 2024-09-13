from datetime import date, datetime, timedelta
from pandas import to_datetime


class Utils:
    def __init__(self):
        self.today = date.today()

    def last_day_two_months_ago(self) -> str:
        today_before_month = self.today.replace(day=1) - timedelta(days=1)
        last_day_of_two_months_ago = datetime(
            today_before_month.year, today_before_month.month, 1
        ) + timedelta(days=32)
        last_day_of_two_months_ago = last_day_of_two_months_ago.replace(
            day=1
        ) - timedelta(days=1)
        return last_day_of_two_months_ago.strftime("%Y-%m-%d")

    def last_day_current_month(self) -> str:
        last_day_current_month = datetime(
            self.today.year, self.today.month, 1
        ) + timedelta(days=32)
        last_day_current_month = last_day_current_month.replace(day=1) - timedelta(
            days=1
        )
        last_day_current_month_str = last_day_current_month.strftime("%Y-%m-%d")
        return last_day_current_month_str

    def last_day_last_month(self) -> str:
        year = self.today.year
        return f'12/31/{year}'

    def current_day(self, format) -> str:
        return self.today.strftime(format)

    def condition_str(self, df, condition):
        if not hasattr(globals().get("Utils"), condition["value"][:-2]):
            return f"`{condition['column']}` {condition['condition']} '{condition['value']}'"
        else:
            df[condition["column"]] = to_datetime(
                df[condition["column"]], format=condition["format"], errors="coerce"
            )
            date = self.__getattribute__(condition["value"][:-2])
            return f"`{condition['column']}` {condition['condition']} '{date(condition['format'])}' | `{condition['column']}`.isnull()"
