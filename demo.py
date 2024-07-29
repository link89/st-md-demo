import streamlit as st
import streamlit.components.v1 as st_components

from string import Template

with open("./template.html", "r") as f:
  nglviewer_template =  f.read().strip()


ngl_html = Template(nglviewer_template).substitute(
        STRUCTURE_URL='/app/static/dump.pdb',
        TRAJ_URL='/app/static/dump.nc',
        BACKGROUND_COLOR='#ffffff',
        BODY_STYLE='box-shadow: 0 0 1px 1px #eee;padding: 0 8px;background-color:#fff',
        AUTO_PLAY='false', # true | false
        PLAY_MODE='loop', # loop | once
    )

st_components.html(ngl_html, height=600)