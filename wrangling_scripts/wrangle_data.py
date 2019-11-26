import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

data = pd.read_csv('data\\heart.csv')
sex_map = {1: 'male', 0: 'female'}
target_map = {1: 'No Heart Disease', 0: 'Heart Disease'}

data['target_name'] = data.target.map(target_map)

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
    
    fig = go.Figure(go.Heatmap(z=z, x=cols, y=cols, colorscale='Viridis'))
    
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

  group_labels = ["Heart Disease", "No Heart Disease"]
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

# third chart plots percent of population that is rural from 1990 to 2015
  proportions = data.groupby(['target', 'sex']).size().reset_index()
  proportions.columns = ['target', 'sex', 'number']
  proportions['totalsex'] = proportions.groupby('sex').number.transform('sum')
  proportions['proportion'] = proportions['number'] / proportions['totalsex']
  # turn it into a categorical variable

  proportions['sex'] = proportions['sex'].map(sex_map)
  proportions['target'] = proportions['target'].map(target_map)
  
  fig_three = px.bar(proportions, x='sex', y='proportion', color='target', barmode='group')
  fig_three.update_layout(
    title='Proportion of Sex with Heart Disease'
  )

# fourth chart shows rural population vs arable land
  fig_four = px.scatter_3d(
    data.loc[data.sex == 1],
    x="chol",
    y="trestbps",
    z="thalach",
    color="target_name"
  )
  fig_four.update_layout(showlegend=False, title='Max Heart Rate Achieved (Thalach), Cholestoral, and Resting Blood Pressure (trestbps) in Males')
  fig_four.update_traces(opacity=0.75, marker=dict(size=5))

  scatter_columns = list(data.drop('target', axis=1).columns)
  fig_five = px.scatter_matrix(
    data,
    dimensions=scatter_columns,
    color='target_name',
    symbol='target_name',
    title='Scatter matrix for Heart Disease Dataset'
  )
  fig_five.update_traces(diagonal_visible=False, opacity=0.15)
  # fig_five.update_layout(xaxis=dict(shoticklabels=False))

  
  # append all charts to the figures list
  figures = []
  #figures.append(dict(data=graph_one, layout=layout_one))
  figures.append(fig_one)
  figures.append(fig_two)
  figures.append(fig_three)
  figures.append(fig_four)
  #figures.append(dict(data=graph_two, layout=layout_two))
  #figures.append(dict(data=graph_three, layout=layout_three))
  #figures.append(dict(data=graph_four, layout=layout_four))
  #figures.append(dict(data=graph_five, layout=layout_five))
  figures.append(fig_five)

  return figures