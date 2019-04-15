import pandas as pd

data = pd.read_csv(
        "pses_data/2018_PSES_open_dataset_Ensemble_de_données_ouvertes_du_SAFF_2018.csv",
        engine = "python",
        sep = ","
        )