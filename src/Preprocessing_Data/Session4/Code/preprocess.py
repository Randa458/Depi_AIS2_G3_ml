import pandas as pd
import numpy as np
def chk_types(data):
    dtypes = data.dtypes
    n_uniques = data.nunique()
    return pd.DataFrame({"Dtype":dtypes, "Num_Uniques":n_uniques}).T


def chk_null(data):
    null = data.isnull().sum()
    ratio = (null / data.shape[0]) * 100
    return pd.DataFrame({"Null Count": null,"Null %": ratio.round(2)}).T