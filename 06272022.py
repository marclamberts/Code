#%%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
from matplotlib import rcParams
import numpy as np
from highlight_text import fig_text
import pandas as pd

from PIL import Image
import urllib
import os

# --- Use this only if you have already downloaded fonts into your
# --- local directory.

# Add pretty fonts


# --- Reading the data

df = pd.read_csv("relegation_cost_06272022.csv", index_col = 0)

# We filter the adjusted data.
df = df[df["adj"] == "adjusted"].reset_index(drop = True)
df = df.sort_values(by = "season_relegated", ascending=False)

# -----------------------------
# The Visualization

nrows = df.shape[0]
ncols = 10 

fig = plt.figure(figsize=(10,6), dpi = 150, facecolor="#EFE9E6")
ax = plt.subplot(111)

ax.set_xlim(-2, ncols*2 + 3)
ax.set_ylim(-1, nrows + 2)

# --- Axes transformations
DC_to_FC = ax.transData.transform
FC_to_NFC = fig.transFigure.inverted().transform

# Native data to normalized data coordinates
DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))

# We plot all the team names & logos
fotmob_url = "https://images.fotmob.com/image_resources/logo/teamlogo/"
for index, x in enumerate(df["team_name"]):
    ax.annotate(
        xy = (0, index),
        text = x,
        ha = "left",
        va = "center",
        weight = "bold",
        size = 10
    )
    ax_coords = DC_to_NFC([-1.5, index - 0.3])
    logo_ax = fig.add_axes([ax_coords[0], ax_coords[1], 0.04, 0.04], anchor = "C")
    club_icon = Image.open(urllib.request.urlopen(f"{fotmob_url}{df['relegated_id'].iloc[index]:.0f}.png")).convert("LA")
    logo_ax.imshow(club_icon)
    logo_ax.axis("off")

# Seasons
for index, x in enumerate(df["season_relegated"]):
    ax.annotate(
        xy = (5, index),
        text = x,
        ha = "center",
        va = "center",
        size = 10
    )

# Initial valuation
for index, x in enumerate(df["value_0"]):
    ax.annotate(
        xy = (7.5, index),
        text = f"£ {x:,.1f}",
        ha = "center",
        va = "center",
        size = 10,
        weight = "bold"
    )

# Change in valuation
cols = [f"value_{x}" for x in range(1,8)]
for index_j, col in enumerate(cols):
    for index_i, row in enumerate(df[col]):
        if np.isnan(row):
            row_text = ""
            bg_color = "lightgrey"
            ec_color = "lightgrey"
            alpha = 0.85
        else:
            row_text = f"{row:.0%}"
            bg_color = "#de6f57"
            ec_color = "#de6f57"
            alpha = abs(row)

        # Add background patches
        rect = patches.Rectangle(
            (10 + index_j*2 - 1, index_i - .5),  # bottom left starting position (x,y)
            2,  # width
            1,  # height
            ec=ec_color,
            fc=bg_color,
            alpha = alpha,
            zorder=-1 #This is important to place the rectangles behind the label.
        )
        ax.add_patch(rect)
        text_ = ax.annotate(
            xy = (10 + index_j*2, index_i),
            text = row_text,
            ha = "center",
            va = "center",
            size = 10,
            color = "white",
            weight = "bold"
        )

        text_.set_path_effects(
            [path_effects.Stroke(linewidth=1.75, foreground="black"), path_effects.Normal()]
        )

# - Column titles 
ax.annotate(
    xy = (0, nrows),
    text = "Team relegated",
    weight = "bold"
)
ax.annotate(
    xy = (5, nrows),
    text = "Rel.\nseason",
    weight = "bold",
    ha = "center"
)
ax.annotate(
    xy = (7.5, nrows),
    text = "Mkt. value\n(mn)",
    weight = "bold",
    ha = "center"
)

for year in range(0,8):
    if year == 0:
        year_text = "year"
    else:
        year_text = "years"
    ax.annotate(
        xy = (10 + year*2, nrows),
        text = f"{year + 1} {year_text}",
        weight = "bold",
        ha = "center"
    )

# Years since relegation text

ax.plot([9, ax.get_xlim()[1]], [nrows + 1.1, nrows + 1.1], lw = 1.75, color = "black")
ax.annotate(
    xy = (17, nrows + 1.3),
    text = "Market value change since relegation",
    weight = "bold",
    ha = "center"
)


# Table borders
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [nrows - .35, nrows - .35], lw = 2, color = "black")
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [-.65, -.65], lw = 2, color = "black")
for x in range(nrows):
    if x == 0:
        continue
    ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [x - .5, x - .5], lw = 1, color = "lightgrey", ls = ":", zorder = -2)

ax.set_axis_off()

fig_text(
    x = 0.13, y = 0.965, 
    s = "The Cost of Premier League Relegation",
    va = "bottom", ha = "left",
    fontsize = 17, color = "black", font = "DM Sans", weight = "bold"
)
fig_text(
	x = 0.13, y = .95, 
    s = "Change in squad market value for sides relegated from the Premier League that <haven't regained promotion> after\nbeing dropped from the division. Figures adjusted by inflation | source: transfermarkt | viz by @sonofacorner\n<Market value is presented at the time of relegation>.",
    highlight_textprops=[{"weight":"bold"},{"weight":"bold"}],
	va = "top", ha = "left",
	fontsize = 10, color = "#4E616C", font = "Karla"
)

plt.savefig(
	"figures/06272022_epl_relegation.png",
	dpi = 600,
	facecolor = "#EFE9E6",
	bbox_inches="tight",
    edgecolor="none",
	transparent = False
)

plt.savefig(
	"figures/06272022_epl_relegation_tr.png",
	dpi = 600,
	facecolor = "none",
	bbox_inches="tight",
    edgecolor="none",
	transparent = True
)
