from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go

def gerar_previsao(df, dias):
    df_prophet = df.rename(columns={"data": "ds", "vendas": "y"})
    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=dias)
    forecast = model.predict(future)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prophet['ds'], y=df_prophet['y'],
                             name="Vendas Reais", mode="lines+markers",
                             line=dict(color="blue", width=2)))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'],
                             name="Previsão da IA", mode="lines",
                             line=dict(color="orange", width=2, dash="dash")))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'],
                             name="Limite Superior", mode="lines",
                             line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'],
                             name="Limite Inferior", mode="lines",
                             fill='tonexty', fillcolor='rgba(255,165,0,0.2)',
                             line=dict(width=0), showlegend=True))

    fig.update_layout(title="📈 Previsão de Vendas com IA",
                      xaxis_title="Data", yaxis_title="Quantidade de Vendas",
                      legend_title="Legenda", hovermode="x unified",
                      template="plotly_white")

    forecast_result = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(dias)
    return fig, forecast_result
