import pandas as pd

def load_dataframe():
    df = pd.read_csv('data/spotify_songs.csv')

    # Remove duplicate entries from multiple playlists
    df = df.drop_duplicates(subset=["track_id"]).reset_index(drop=True)

    # Drop rows with NaN values
    df = df.dropna(subset=["track_popularity", "track_name", "track_artist"])

    # Cleanup
    df["track_name"] = df["track_name"].str.strip()
    df["track_artist"] = df["track_artist"].str.strip()

    # Drop unnecessary columns
    df = df.drop(columns=['track_id', 'track_album_id', 'track_album_name', 'playlist_id',\
                      'duration_ms', 'key', 'mode', 'loudness', 'liveness'])
    
    hit_threshold = get_hit_threshold(df)
    df["is_hit"] = df["track_popularity"] >= hit_threshold
    
    return df

def get_hit_threshold(df, quantile=0.95):
    return df["track_popularity"].quantile(quantile)