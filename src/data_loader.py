import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.dummy import DummyRegressor

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
                      'duration_ms', 'key', 'mode', 'loudness', 'liveness', 'instrumentalness', 'acousticness'])
    
    hit_threshold = get_hit_threshold(df)
    df["is_hit"] = df["track_popularity"] >= hit_threshold
    
    return df

def get_hit_threshold(df, quantile=0.95):
    return df["track_popularity"].quantile(quantile)

def calc_r2_scores(df):
    genres = df['playlist_genre'].unique()
    results = []

    for genre in genres:
        sub = df[df['playlist_genre'] == genre].dropna()
        X = sub[['danceability', 'energy', 'valence', 'tempo', 'speechiness']]
        y = sub['track_popularity']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = RandomForestRegressor(n_estimators=200, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        y_pred = model.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)

        dummy = DummyRegressor(strategy="mean")
        dummy.fit(X_train_scaled, y_train)
        dummy_r2 = r2_score(y_test, dummy.predict(X_test_scaled))
    
        results.append({'genre': genre, 'model': 'Random Forest', 'r2': r2})
        results.append({'genre': genre, 'model': 'Dummy', 'r2': dummy_r2})
    
    return pd.DataFrame(results)