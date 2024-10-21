#Interactive graph

import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'
# Sample data (replace this with your actual df_2)
# df_2 = pd.DataFrame({
#     'Name': ['Player A', 'Player B', 'Player C', 'Player D'],
#     'On': [15, 25, 35, 45],
#     'Off': [10, 20, 30, 40]
# })

#keep the names for the graphs
stat_sig_p_values = pvalues_df['Stat'][pvalues_df['P-Value']<0.1].values

for stat in stat_sig_p_values:
    df_2 = dataframes_3[stat]
    df_2 = df_2[(df_2['MinutesOn']>150)&(df_2['MinutesOff']>150)]
    # Function to plot using Plotly
    def plot_on_off_barplot_interactive(df_2):
        # Create a bar chart for "On" and "Off"
        fig = go.Figure()

        # Add bars for "On"
        fig.add_trace(go.Bar(
            x=df_2['Name'], 
            y=df_2['On'], 
            name='On', 
            marker_color='blue',
            hoverinfo='text',
            text=[f"Player: {name}<br>On Points: {points}" for name, points in zip(df_2['Name'], df_2['On'])]
        ))

        # Add bars for "Off"
        fig.add_trace(go.Bar(
            x=df_2['Name'], 
            y=df_2['Off'], 
            name='Off', 
            marker_color='red',
            hoverinfo='text',
            text=[f"Player: {name}<br>Off Points: {points}" for name, points in zip(df_2['Name'], df_2['Off'])]
        ))

        # Update layout for the plot
        player_name = player_ids[''][player_ids['']['PLAYER_ID'] == pd.to_numeric(params['PlayerId'])]['PLAYER_NAME'].values[0]
        fig.update_layout(
            title=f'{stat} When {player_name} Is On vs Off',
            xaxis_title='Player',
            yaxis_title='Points Scored',
            barmode='group',  # This puts bars side by side
            hovermode="x"      # Makes hover info appear for both bars when mouse hovers over a player's name
        )

        # Show the interactive plot
        fig.show()

    # Call the function with your dataset
    plot_on_off_barplot_interactive(df_2)
# Function to plot using Plotly
def plot_on_off_barplot_interactive(df_2):
    # Create a bar chart for "On" and "Off"
    fig = go.Figure()

    # Add bars for "On"
    fig.add_trace(go.Bar(
        x=df_2['Name'], 
        y=df_2['On'], 
        name='On', 
        marker_color='blue',
        hoverinfo='text',
        text=[f"Player: {name}<br>On Points: {points}" for name, points in zip(df_2['Name'], df_2['On'])]
    ))

    # Add bars for "Off"
    fig.add_trace(go.Bar(
        x=df_2['Name'], 
        y=df_2['Off'], 
        name='Off', 
        marker_color='red',
        hoverinfo='text',
        text=[f"Player: {name}<br>Off Points: {points}" for name, points in zip(df_2['Name'], df_2['Off'])]
    ))

    # Update layout for the plot
    fig.update_layout(
        title=f'{stat_key} When {player_name} Is On vs Off',
        xaxis_title='Player',
        yaxis_title='Points Scored',
        barmode='group',  # This puts bars side by side
        hovermode="x"      # Makes hover info appear for both bars when mouse hovers over a player's name
    )

    # Show the interactive plot
    fig.show()

# Call the function with your dataset
plot_on_off_barplot_interactive(df_2)
