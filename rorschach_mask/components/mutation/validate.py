import pandas as pd
import numpy as np
from pandas import NaT


class Validate:
    @staticmethod
    def to_str(series) -> str:
        return series.fillna("").astype(str)
    
    @staticmethod
    def to_id_str(series) -> pd.Series:
        def convert(value) -> str:
            if isinstance(value, str):
                return value
            if isinstance(value, float) and np.nan:
                return ""
            if isinstance(value, int) and value == 0:
                return ""
            return str(value)
        return series.apply(convert)

    @staticmethod
    def to_id_int(series) -> pd.Series:
        def convert(value) -> int:
            if isinstance(value, str) and value == "":
                return 0
            if isinstance(value, str) and value.isnumeric():
                return int(value)
            if isinstance(value, float) and np.nan:
                return 0
            return int(value)
        return series.apply(convert)

    @staticmethod
    def to_datetime(series) -> pd.Series:
        def convert(value) -> pd.Timestamp | str :
            date = pd.to_datetime(value, errors='coerce')
            return date.strftime("%m-%d-%Y") if pd.notnull(date) else ""
        return series.apply(convert)

    @staticmethod
    def to_int(series) -> int:
        def convert(value) -> int:
            value_float = float(value) if str(value).isnumeric() else 0
            if np.isnan(value_float):
                return 0
            else:
                return int(value_float)

        return series.apply(convert)
    
    @staticmethod
    def to_bigint(series) -> int:
        def convert(value) -> int:
            value_float = float(value) if str(value).isnumeric() else 0
            if np.isnan(value_float):
                return 0
            else:
                return int(value_float)

        return series.apply(convert)

    @staticmethod
    def to_int_last_4(series) -> int:
        return series.astype(str).apply(
            lambda x: int(x[-4:]) if x and x[-4:].isnumeric() else 0
        )

    @staticmethod
    def to_minus(series) -> str:
        return series.apply(
            lambda x: str(x).lower()
            if str(x).lower() not in ["nan", "None", ""]
            else ""
        )

    @staticmethod
    def to_boolean(series) -> bool:
        return series.astype(bool)

    @staticmethod
    def to_int_first_5(series):
        return series.apply(
            lambda x: int(str(x)[:5]) if x and str(x)[:5].isnumeric() else 0
        )

    @staticmethod
    def to_float(series):
        return series.astype(float)

    @staticmethod
    def to_float_deductible(series):
        return series.apply(
            lambda x: float(x) if isinstance(x, str) and x.isnumeric() else 0
        )

    @staticmethod
    def to_int_first_1(series):
        return series.astype(str).apply(
            lambda x: int(x[:1]) if x and x[:1] and x[:1].isnumeric() else 0
        )

    @staticmethod
    def to_int_last_1(series):
        return series.astype(str).apply(
            lambda x: int(x[-1:]) if x and x[-1:] and x[-1:].isnumeric() else 0
        )

    @staticmethod
    def to_company(series):
        series = series.astype(str)

        def extract_first_word(text):
            if text == "nan":
                return ""
            parts = text.split(" ")
            return str(parts[0]).lower() if len(parts) > 0 else ""

        return series.apply(extract_first_word)

    @staticmethod
    def to_npn(series):
        series = series.astype(str)

        def get_npn(text) -> int:
            if "beatriz sierra" in text.lower():
                return 8602276
            elif "ana" in text.lower() and "corrales" in text.lower():
                return 19011307
            elif "juan ramirez" in text.lower():
                return 20639288
            else:
                return 0

        return series.apply(get_npn).astype(int)

    @staticmethod
    def to_followup_docs(series):
        series = series.astype(str)

        def get_value_followup_docs(text) -> bool:
            if text in ["action_needed", "NOT"]:
                return False
            else:
                return True

        return series.apply(get_value_followup_docs).astype(bool)

    @staticmethod
    def to_zfill_10(series):
        def convert(value) -> str:
            value_float = float(value) if str(value).isnumeric() else 0
            if np.isnan(value_float):
                return ""
            elif isinstance(value, float):
                return str(int(value))
            else:
                return str(value)

        series = series.apply(convert)
        return series.str.zfill(10)

    @staticmethod
    def to_id_zfill_10(series) -> pd.Series:
        def convert(value) -> str:
            value = int(value) if str(value).isnumeric() else str(value).replace("'", "").replace('"', '')
            if isinstance(value, str) and (value == "" or value == "nan"):
                return ""
            if isinstance(value, float) and np.nan:
                return ""
            return str(value).zfill(10)

        return series.apply(convert)

    @staticmethod
    def to_status(series):
        series = series.astype(str).str.lower()

        def get_status(text) -> str:
            if text in ["active", "effectuated"]:
                return "active"
            elif text in ["initial enrollment", "pendingeffectuation"]:
                return "initial enrollment"
            else:
                return ""

        return series.apply(get_status).astype(str)

    @staticmethod
    def to_float_2(series):
        return series.apply(
            lambda x: round(float(x), 2)
            if (x and np.isreal(x)) or (isinstance(x, str) and np.isreal(float(x)))
            else 0
        )
