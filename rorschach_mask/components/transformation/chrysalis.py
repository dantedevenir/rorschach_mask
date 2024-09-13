import pandas as pd
import toml
from utils.utils import Utils
from mapping import mapping_model
from ..mutation.mapping import validate
from os import getenv

class Chrysalis:
    def __init__(self, df, registry):
        self.column_mapping = None
        self.df = df
        self.registry = registry
        self.utils = Utils()
        self.config()

    def config(self):
        ENV_PATH = getenv('ENV_PATH')
        with open(f"{ENV_PATH}/rocky.toml", "r") as file:
            config_file = toml.load(file)
            print("Registry:",self.registry)
            try:
                if (
                    self.registry != "vtigercrm"
                    and self.registry != "healthsherpa"
                    and config_file[self.registry]
                ):
                    self.df['issuer'] = self.registry
                    if len(config_file[self.registry]["id"]) > 1 and isinstance(
                        config_file[self.registry]["id"], list
                    ):
                        id = config_file[self.registry]["id"]
                        self.df = self.df.query(f"{id[0]} == {id[1]}")
                        id = config_file[self.registry]["id"][0]
                    else:
                        id = config_file[self.registry]["id"]
                    if len(config_file[self.registry]["date"]) > 1 and isinstance(
                        config_file[self.registry]["date"], list
                    ):
                        column = config_file[self.registry]["date"][0]
                        values = config_file[self.registry]["date"][1:]
                        last_day_current_month = self.utils.last_day_current_month()
                        last_day_of_two_months_ago = (
                            self.utils.last_day_two_months_ago()
                        )
                        query = " or ".join(
                            f"{column} == '{value}'" for value in values
                        )
                        self.df = self.df.query(query)
                        df_copy = self.df.copy()
                        df_copy.loc[:, "Paid Through Date"] = df_copy.apply(
                            lambda row: last_day_current_month
                            if row[column[1:-1]] == values[0]
                            else (
                                last_day_of_two_months_ago
                                if row[column[1:-1]] == values[1]
                                else None
                            ),
                            axis=1,
                        )
                        date = "Paid Through Date"
                    else:
                        date = config_file[self.registry]["date"]
                    if conditions := config_file.get(self.registry, {}).get("condition"):
                        for condition in conditions:
                            field_date = condition['column']
                            if field_date == 'End_Date':
                                self.df[field_date] = self.df[field_date].replace({'1/1/2099': self.utils.last_day_last_month()})
                            elif field_date == 'Broker Term Date':
                                self.df[field_date] = self.df[field_date].replace({'12/31/9999': self.utils.last_day_last_month()})
                        
                        self.df = self.df.query(
                            " & ".join(
                                [
                                    self.utils.condition_str(self.df, condition)
                                    for condition in conditions
                                    if config_file[self.registry]["condition"]
                                ]
                            )
                        )
                    self.df = self.df.drop_duplicates(subset=[id])
                # self.salesOrder(registry, df[[id, date]], script)
                self.rename()
            except Exception as e:
                raise e

    def rename(self):
        df_copy_rename = self.df
        if isinstance(df_copy_rename, pd.DataFrame) and self.registry != "healthsherpa":
            df_copy_rename.rename(columns=mapping_model[self.registry], inplace=True)

        df_copy_rename = df_copy_rename.assign(
            **{
                k: pd.Series()
                for k in validate.keys()
                if k not in df_copy_rename.columns
            }
        )
        df_copy_rename[validate.keys()]
        self.validate(df_copy_rename[validate.keys()])

    def validate(self, df_copy):
        df_copy = df_copy.copy()
        for column, transformation in validate.items():
            df_copy[column] = transformation(df_copy[column])

        self.df = df_copy.reindex(columns={k: k for k in validate.keys()})
