import pandas as pd

def load_penguin_data():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
    return df.shape

if __name__ == "__main__":
    shape = load_penguin_data()
    print(f"Penguin dataset shape: {shape}")

