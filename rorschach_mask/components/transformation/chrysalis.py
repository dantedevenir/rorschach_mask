import pandas as pd
from mapping import mapping_model
from ..mutation.mapping import validate
from os import getenv

class Chrysalis:
    def __init__(self, df, registry):
        self.column_mapping = None
        self.df = df
        self.registry = registry
        
        self.rename()

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
