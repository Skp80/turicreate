# -*- coding: utf-8 -*-
# Copyright © 2017 Apple Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-3-clause license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause
from __future__ import print_function as _
from __future__ import division as _
from __future__ import absolute_import as _
from .plot import Plot
import sys
import os
import turicreate as tc

def _get_client_app_path():
    (tcviz_dir, _) = os.path.split(os.path.dirname(__file__))

    if sys.platform != 'darwin' and sys.platform != 'linux2' and sys.platform != 'linux' :
        raise NotImplementedError('Visualization is currently supported only on macOS and Linux.')
    
    if sys.platform == 'darwin':
        return os.path.join(tcviz_dir, 'Turi Create Visualization.app', 'Contents', 'MacOS', 'Turi Create Visualization')

    if sys.platform == 'linux2' or sys.platform == 'linux':
        return os.path.join(tcviz_dir, 'Turi Create Visualization', 'visualization_client')

def _get_title(title):
    if title == "":
        title = " "
    if title == None:
        title = ""

    return title

def show(x, y, xlabel="X", ylabel="Y", title=None):
    """
    Plots the data in `x` on the X axis and the data in `y` on the Y axis
    in a 2d visualization, and shows the resulting visualization.
    Uses the following heuristic to choose the visualization:

    * If `x` and `y` are both numeric (SArray of int or float), and they contain
      fewer than or equal to 5,000 values, show a scatter plot.
    * If `x` and `y` are both numeric (SArray of int or float), and they contain
      more than 5,000 values, show a heat map.
    * If `x` is numeric and `y` is an SArray of string, show a box and whisker
      plot for the distribution of numeric values for each categorical (string)
      value.
    * If `x` and `y` are both SArrays of string, show a categorical heat map.

    This show method supports SArrays of dtypes: int, float, str.

    Notes
    -----
    - The plot will render either inline in a Jupyter Notebook, or in a
      native GUI window, depending on the value provided in
      `turicreate.visualization.set_target` (defaults to 'auto').

    Parameters
    ----------
    x : SArray
      The data to plot on the X axis of a 2d visualization.
    y : SArray
      The data to plot on the Y axis of a 2d visualization. Must be the same
      length as `x`.
    xlabel : str (optional)
      The text label for the X axis. Defaults to "X".
    ylabel : str (optional)
      The text label for the Y axis. Defaults to "Y".
    title : str (optional)
      The title of the plot. Defaults to None. If the value is None, the title
      will be "<xlabel> vs. <ylabel>". Otherwise, the string passed in as the
      title will be used as the plot title.

    Examples
    --------
    Show a categorical heat map of pets and their feelings.

    >>> x = turicreate.SArray(['dog', 'cat', 'dog', 'dog', 'cat'])
    >>> y = turicreate.SArray(['happy', 'grumpy', 'grumpy', 'happy', 'grumpy'])
    >>> turicreate.show(x, y)


    Show a scatter plot of the function y = 2x, for x from 0 through 9, labeling
    the axes and plot title with custom strings.

    >>> x = turicreate.SArray(range(10))
    >>> y = x * 2
    >>> turicreate.show(x, y,
    ...                 xlabel="Custom X label",
    ...                 ylabel="Custom Y label",
    ...                 title="Custom title")

    """
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot(path_to_client, x, y, xlabel, ylabel, title)
    Plot(plt_ref).show()

def scatter(x, y, xlabel="X", ylabel="Y", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_scatter(path_to_client, x, y, 
      xlabel, ylabel,title)
    return Plot(plt_ref)

def categorical_heatmap(x, y, xlabel="X", ylabel="Y", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_categorical_heatmap(path_to_client, x, y, 
      xlabel, ylabel, title)
    return Plot(plt_ref)

def heatmap(x, y, xlabel="X", ylabel="Y", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_heatmap(path_to_client, x, y, 
      xlabel, ylabel, title)
    return Plot(plt_ref)

def box_plot(x, y, xlabel="X", ylabel="Y", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_boxes_and_whiskers(path_to_client, x, y, 
      xlabel, ylabel, title)
    return Plot(plt_ref)

def columnwise_summary(sf):
    path_to_client = _get_client_app_path()
    plt_ref = tc.extensions.plot_columnwise_summary(path_to_client, sf)
    return Plot(plt_ref)

def histogram(sa, xlabel="Values", ylabel="Count", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_histogram(path_to_client, sa, 
      xlabel, ylabel, title)
    return Plot(plt_ref)

def item_frequency(sa, xlabel="Values", ylabel="Count", title=None):
    path_to_client = _get_client_app_path()
    title = _get_title(title)
    plt_ref = tc.extensions.plot_item_frequency(path_to_client, sa, 
      xlabel, ylabel, title)
    return Plot(plt_ref)
