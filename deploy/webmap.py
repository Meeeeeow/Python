# -*- coding: utf-8 -*-
"""webmap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/141ilkS7ycppTokd4uGLHlRDAZkZde-8W
"""

pip install folium

import folium



fg = folium.FeatureGroup("map");
fg.add_child(folium.GeoJson(data =open("india_states.json","r",encoding="utf-8-sig").read()));

map = folium.Map(location=[20.0000, 75.0000], zoom_start = 4);

map.add_child(fg);

map.save("sample_map.html");

