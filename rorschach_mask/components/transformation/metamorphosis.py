import pandas as pd
from ..mutation.mapping import validate
from .chrysalis import Chrysalis

class Metamorphosis:
    def __init__(
        self,
        df: pd.DataFrame,
        transformations: dict,
        column_mapping: dict | None = None,
    ) -> None:
        self.transformations = transformations
        self.column_mapping = column_mapping
        self.breed = df
    
    @classmethod
    def from_pandas(cls, df, topic, mapping: dict | None = None) -> "Metamorphosis":
        df = df.drop_duplicates()
        df_transform = Chrysalis(df, topic).df
        if not mapping:
            return cls(df_transform, validate)
        else:
            return cls(df_transform, validate, column_mapping = mapping)
