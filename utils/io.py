import pandas as pd

def load_data(path):
    columns = ["city","country"] + [f"x{i}" for i in range(1,56)] + ["data_quality"]
    df = pd.read_csv(path, header=None, names=columns)
    df["city"] = df["city"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.strip()


    for col in [f"x{i}" for i in range(1,56)]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

        

    return df





