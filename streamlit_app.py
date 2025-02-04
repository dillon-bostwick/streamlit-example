from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# NRF Any-Time Demo Concept

Adjust data freshness and get real-time capabilities when you need them without complex tech stack changes

"""

FRESHNESS_FORMAT = "%f minutes"

with st.echo(code_location='below'):
    total_points = st.slider("POS System - Data Freshness", 1, 5, 60*24, format=FRESHNESS_FORMAT)
    total_points = st.slider("ERP (SAP HANA) - Data Freshness", 1, 120, 60*24, format=FRESHNESS_FORMAT)
    total_points = st.slider("Oracle EDW - Data Freshness", 1, 24*60, 60*24, format=FRESHNESS_FORMAT)
    num_turns = st.slider("Cost tolerance", 1, 100, 9, format="$%.2f")
    btn = st.button("Continuous Mode")

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
