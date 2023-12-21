import pandas as pd


infected_df = pd.read_csv(r"C:\Users\bett0\Desktop\miuul\Ada_Lovelace_Homework\time_series_covid19_confirmed_global.csv")

recovered_df = pd.read_csv(r"C:\Users\bett0\Desktop\miuul\Ada_Lovelace_Homework\time_series_covid19_recovered_global.csv")

deaths_df = pd.read_csv(r"C:\Users\bett0\Desktop\miuul\Ada_Lovelace_Homework\time_series_covid19_deaths_global.csv")

pd.set_option("display.max_columns", None)
pd.set_option("display.width" ,500)
def check_df(dataframe, head = 5):
    print("######################################  Shape  ##################################")
    print(dataframe.shape)
    print("######################################  Types  ##################################")
    print(dataframe.dtypes)
    print("######################################  Head  ###################################")
    print(dataframe.head(head))
    print("######################################  Tail  ###################################")
    print(dataframe.tail(head))
    print("#######################################  NA  ####################################")
    print(dataframe.isnull().sum())
    print(dataframe.isnull().sum().sum())


check_df(infected_df)

check_df(recovered_df)

check_df(deaths_df)

infected_df.dropna(inplace = True)

recovered_df.dropna(inplace = True)

deaths_df.dropna(inplace = True)

total_list = [col for col in infected_df.columns if col not in ['Province/State', 'Country/Region', 'Lat', 'Long']]
#sütunları aynı verilerin o yüzden tek total_list tanımladım

infected_df["province_total_infected"] = infected_df[total_list].sum(axis = 1)

recovered_df["province_total_recovered"] = infected_df[total_list].sum(axis = 1)

deaths_df["province_total_death"] = infected_df[total_list].sum(axis = 1)

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN" : dataframe.groupby(categorical_col)[target].mean()}) ,end = "\n\n\n")

target_summary_with_cat(infected_df, "province_total_infected", "Province/State")


def make_frame(country : str):
    df = pd.DataFrame({
        "infected" : infected_df.loc[country],
        "rcovered": recovered_df.loc[country],
        "deaths": deaths_df_df.loc[country],

    })
    df.index = pd.to_datetime()

    make_frame("US")