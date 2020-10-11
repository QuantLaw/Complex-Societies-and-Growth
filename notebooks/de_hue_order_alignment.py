# this is a helper file for the community sankey plot and cluster family regressions notebooks

import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap


def move_to_pos(items, item, pos):
    items = list(items)
    if item in items:
        idx = items.index(item)
        items.pop(idx)
        items.insert(pos, item)
    return items


def cluster_family_colors(dataset):
    if dataset.lower() == 'us':
        return sns.color_palette("tab20")
    elif dataset.lower() == 'de':
        palette = [
            sns.color_palette("tab20")[i]
            for i in [
                1, 3, 2, 0, 5, 4, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19
            ]
        ]
        return palette
    else:
        raise Exception(f'Dataset {dataset} unknown')


def cluster_family_plt_colors(dataset):
    colors = np.array(
        [np.array([*c, 1]) for c in cluster_family_colors(dataset)] +
        [np.array([0.75, 0.75, 0.75, 1])]
    )
    return ListedColormap(colors)
