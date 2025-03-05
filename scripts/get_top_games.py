import pandas as pd


def top_n_games_to_csv(data_dir, n=10):
    games = pd.read_csv(data_dir + "games.csv").loc[:, ["app_id"]]
    spy = pd.read_csv(data_dir + "steamspy_insights.csv") .loc[:, ["app_id", "concurrent_users_yesterday"]]

    df = games.merge(spy.loc[:, ["app_id", "concurrent_users_yesterday"]], on="app_id", how="left").sort_values("concurrent_users_yesterday", ascending=False)

    df = df[df.concurrent_users_yesterday >= n].sort_values("concurrent_users_yesterday")

    df.app_id.to_csv(f"{data_dir}/ge-{n}_concurrent-users.csv", index=False)

if __name__ == "__main__":
    data_dir = "data/oct24_clean/"
    n = 10

    top_n_games_to_csv(data_dir, n)
