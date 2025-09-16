import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# --- 1. Cargar y limpiar datos ---
df = pd.read_excel("prueba lstm.xlsx")

# Convertir fechas
df["MES"] = pd.to_datetime(df["MES"])
df = df.sort_values("MES")


# --- 2. Normalizar ---
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[prov_cols])

# --- 3. Crear secuencias para LSTM ---
def create_sequences(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

window_size = 12
X, y = create_sequences(scaled_data, window_size)

# Redimensionar X: (samples, time_steps, features)
X = X.reshape((X.shape[0], window_size, len(prov_cols)))

# --- 4. Modelo LSTM multisalida ---
model = Sequential([
    LSTM(100, activation='relu', input_shape=(window_size, len(prov_cols))),
    Dense(len(prov_cols))  # salida por cada provincia
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=32)

# --- 5. Predicción de 120 meses hacia el futuro ---
last_seq = scaled_data[-window_size:]
input_seq = last_seq.reshape(1, window_size, len(prov_cols))

future_preds = []

for _ in range(120):
    next_pred = model.predict(input_seq)[0]
    future_preds.append(next_pred)
    input_seq = np.append(input_seq[:, 1:, :], [[next_pred]], axis=1)

# Desnormalizar predicciones
future_preds_inv = scaler.inverse_transform(future_preds)

# Crear DataFrame con fechas futuras
last_date = df["MES"].iloc[-1]
future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=120, freq='MS')
forecast_df = pd.DataFrame(future_preds_inv, columns=prov_cols)
forecast_df.insert(0, "MES", future_dates)

# --- 6. (Opcional) Graficar una provincia ---


provincia = "ALMERIA"  # cambia según prefieras

plt.figure(figsize=(12, 6))
plt.plot(df["MES"], df[provincia], label="Histórico")
plt.plot(forecast_df["MES"], forecast_df[provincia], label="Predicción", linestyle='--')
plt.title(f"Predicción de €/m² para {provincia}")
plt.xlabel("Fecha")
plt.ylabel("€/m²")
plt.legend()
plt.grid()
plt.show()
