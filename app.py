import pandas as pd
import dash
from dash import Dash, dcc, html
import plotly.express as plt

#Convert CSV to DataFrame
msf_genai = pd.read_csv("market_size_forecasting_generative_ai.csv")
gi = pd.read_csv('global_investments.csv')
rv_fc_sa = pd.read_csv('revenue_forecast_it_south_africa.csv', index_col='Area')
cssa = pd.read_csv('company_shares_in_south_africa.csv')

#Convert rows and columns to list
year1 = msf_genai.columns.to_list()
forecast = msf_genai.loc['GenAI'].to_list()

year2 = gi['year'].to_list()
inv = gi['total_investment'].to_list()


year3 = rv_fc_sa.columns.to_list()
it_adm_out = rv_fc_sa.loc['IT-Administration Outsourcing'].to_list()
it_app_out = rv_fc_sa.loc['IT-Application Outsourcing'].to_list()
it_oth_out = rv_fc_sa.loc['IT-Other IT Outsourcing'].to_list()
it_web_host = rv_fc_sa.loc['IT-Web Hosting'].to_list()

rv_fc_df = pd.DataFrame()
rv_fc_df["IT-Administration Outsouring"]=it_adm_out
rv_fc_df["IT-Application Outsourcing"]=it_app_out
rv_fc_df["IT-Other IT Outsourcing"]=it_oth_out
rv_fc_df["IT-Web Hosting"]=it_web_host
rv_fc_df["Year"]=year3

rv_fc_df.set_index("Year", inplace = True)

it_service = pd.DataFrame(cssa.loc[:8])
gentext = pd.DataFrame(cssa.loc[9:17])
genimage = pd.DataFrame(cssa.loc[18:])


#Remove unwanted data
year1.pop(0)
forecast.pop(0)

#Plot the graph 
fig1 = plt.line(x = year1, y = forecast, title = 'Market Size Forecasting for Generative AI', labels = {'x': 'Year', 'y': "GenAI Forecast"}, width = 500, height = 500)

fig2 = plt.line(x = year2, y = inv, title = 'Global Investments in Generative AI', labels = {'x':'Year', "y":'Total Investment'}, width = 500, height = 500)

fig3 = plt.line(rv_fc_df, title = 'Revenue Forecast for the IT Sector in SA', labels={'value':'Revenue Forecast', 'variable':'Areas'})

fig4 = plt.pie(it_service, values = 'share in percent', title = 'Company Shares in the IT Services Market in SA', names = 'brand', labels={'brand':'Brand', 'share in percent':'Shares in Percent'})

fig5 = plt.pie(gentext, values = 'share in percent', names = 'brand', title = 'Company Shares in the Text Generation AI Market in SA', labels={'brand':'Brand', 'share in percent':'Shares in Percent'})

fig6 = plt.pie(genimage, values = 'share in percent', names = 'brand', title = 'Company Shares in the Image Generation AI Market in SA', labels={'brand':'Brand', 'share in percent':'Shares in Percent'})

g1 = dcc.Graph(figure=fig1)
g2 = dcc.Graph(figure=fig2)
g3 = dcc.Graph(figure=fig3) 
g4 = dcc.Graph(figure=fig4)
g5 = dcc.Graph(figure=fig5)
g6 = dcc.Graph(figure=fig6)

app = dash.Dash()

app.layout = html.Div([html.H1('AI Market Analysus', style={'textAlign': 'center', 'color': '#034694'}), 
                       g1, 
                       g2,
                       g3, 
                       g4,
                       g5,
                       g6
                       
])

if __name__ == '__main__':
     app.run_server(port="8091")

