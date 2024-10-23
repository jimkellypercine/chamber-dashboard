from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import glob

# Load and combine multiple CSV files
path = "/Users/jimkellypercine/Desktop/Chamber_Project/data/Event_Attendance_Members.csv"
all_files = glob.glob(path)

# Read all CSVs and concatenate them into a single DataFrame
df_list = [pd.read_csv(file) for file in all_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Sort by 'Fees' in descending order and select the top 10 members
top_10_df = combined_df.sort_values(by='Fees', ascending=False).head(10)

# Create a pie chart showing total fees by Member Name for the top 10 members
fig_pie = px.pie(top_10_df, names='Member Name', values='Fees', title='Top 10 Members by Total Fees', hole=0.3)

# Create a bar chart showing total fees by Member Name for the top 10 members
fig_bar = px.bar(top_10_df, x='Member Name', y='Fees', title='Top 10 Members by Total Fees')

fig_pie.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)',   
    font_color='#5C6A74',          
    width=600,                      
    height=400                      
)

fig_bar.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='#5C6A74',
    width=600,                      
    height=400                      
)

app = Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#FFFFFF',  
        'color': '#333333',            
        'padding': '20px',
        'font-family': "'Roboto', sans-serif"  
    },
    children=[
        html.H1(children='Chamber of Commerce Event Data', style={'textAlign': 'left', 'color': '#1C3D59'}),  

        html.Div(
            style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '40px'},
            children=[
                html.Div(
                    style={'width': '60%'},  
                    children=[
                        dcc.Graph(figure=fig_pie, style={'margin-bottom': '20px'}),
                    ]
                ),
                html.Div(
                    style={
                        'width': '35%',            
                        'backgroundColor': '#F5F5F5',  
                        'border-radius': '10px',
                        'padding': '20px'
                    },
                    children=[
                        html.H2('Insights: Top 10 Members by Total Fees', style={'color': '#1C3D59'}),
                        html.P('The pie chart visualizes the top 10 members based on the total event fees they paid. Each slice shows the relative contribution of each member.'),
                        html.P('This chart helps identify key contributors and their proportional influence on event revenue.')
                    ]
                )
            ]
        ),

        html.Div(
            style={'display': 'flex', 'justify-content': 'space-between'},
            children=[
                html.Div(
                    style={'width': '60%'},  
                    children=[
                        dcc.Graph(figure=fig_bar, style={'margin-bottom': '20px'}),
                    ]
                ),
                html.Div(
                    style={
                        'width': '35%',            
                        'backgroundColor': '#F5F5F5',  
                        'border-radius': '10px',
                        'padding': '20px'
                    },
                    children=[
                        html.H2('Insights: Total Fees Bar Chart', style={'color': '#1C3D59'}),
                        html.P('The bar chart provides a detailed look at the exact total fees paid by each of the top 10 members. The chart clearly displays the fees for easier comparison between members.'),
                        html.P('This chart helps with identifying the specific amounts paid by each member and understanding individual contributions.')
                    ]
                )
            ]
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
