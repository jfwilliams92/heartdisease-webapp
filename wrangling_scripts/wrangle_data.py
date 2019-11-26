import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

data = pd.read_csv('data\\heart.csv')

def plotly_corr_heatmap(df, show_diagonal=False):
    """
    Create a plotly heatmap of dataset features correlation
    """
    
    dff = df.corr()
    cols = list(dff.columns)
    z = dff.values
    if not show_diagonal:
      z[z==1.0] = np.nan
    z = z.tolist()
    
    fig = go.Figure(go.Heatmap(z=z, x=cols, y=cols))
    
    return fig

def return_figures():
  """Creates four plotly visualizations

  Args:
    None

    Returns:
      list (dict): list containing the four plotly visualizations

  """

  x0 = data.loc[data.target==0, 'age']
  x1 = data.loc[data.target==1, 'age']

  group_labels = ["No Heart Disease", "Heart Disease"]
  fig_one = ff.create_distplot([x0, x1], group_labels, bin_size=3, show_rug=False)
  fig_one.update_traces(opacity=0.55)
  fig_one.update_layout(
    title='Probability Density of Age versus Presence of Heart Disease',
    xaxis=dict(title='Age'),
    yaxis=dict(title='Probability Density')
  )


  fig_two = plotly_corr_heatmap(data, show_diagonal=False)
  fig_two.update_layout(
    title="Features Correlation Matrix"
  )

  graph_two = []
  graph_two.append(
      go.Scatter(
      x = [1,2,3,4],
      y = [1,3,5,7],
      mode = 'lines'
      )
  )

  layout_two = dict(title = 'Test Plot 2',
              xaxis = dict(title = 'X'),
              yaxis = dict(title = 'Y'),
              )


# third chart plots percent of population that is rural from 1990 to 2015
  graph_three = []
  graph_three.append(
    go.Scatter(
      x = [1,2,3,4],
      y = [1,3,5,7],
      mode = 'lines'
    )
  )

  layout_three = dict(title = 'Test Plot 3',
              xaxis = dict(title = 'X'),
              yaxis = dict(title = 'Y'),
              )

    
# fourth chart shows rural population vs arable land
  graph_four = []
  graph_four.append(
    go.Scatter(
      x = [1,2,3,4],
      y = [1,3,5,7],
      mode = 'lines'
    )
  )

  layout_four = dict(title = 'Test Plot 4',
              xaxis = dict(title = 'X'),
              yaxis = dict(title = 'Y'),
              )
  
  graph_five = []
  graph_five.append(
    go.Scatter(
      x = [1,2,3,4],
      y = [1,3,5,7],
      mode = 'lines'
    )
  )

  layout_five = dict(title = 'Test Plot 5',
              xaxis = dict(title = 'X'),
              yaxis = dict(title = 'Y'),
              )
  
  # append all charts to the figures list
  figures = []
  #figures.append(dict(data=graph_one, layout=layout_one))
  figures.append(fig_one)
  figures.append(fig_two)
  #figures.append(dict(data=graph_two, layout=layout_two))
  figures.append(dict(data=graph_three, layout=layout_three))
  figures.append(dict(data=graph_four, layout=layout_four))
  figures.append(dict(data=graph_five, layout=layout_five))

  return figures