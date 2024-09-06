import streamlit as st
import streamlit.components.v1 as st_components

from string import Template

with open("./template.html", "r") as f:
  nglviewer_template =  f.read().strip()


ngl_html = Template(nglviewer_template).substitute(
        STRUCTURE_URL='/app/static/dump.pdb',
        TRAJ_URL='',
        BACKGROUND_COLOR='#ffffff',
        BODY_STYLE='box-shadow: 0 0 1px 1px #eee;padding: 0 8px;background-color:#fff',
        AUTO_PLAY='false', # true | false
        PLAY_MODE='loop', # loop | once
        DEFAULT_MATRIX='[]' # Ref: https://threejs.org/docs/#api/en/math/Matrix4
        # DEFAULT_MATRIX='[2,0,0,0, 0,2,0,0, 0,0,2,0, 0,0,0,1]'
        # DEFAULT_MATRIX='[1,0,0,0, 0,0.5,0.866,0, 0,-0.866,0.5,0, 0,0,0,1]'
        # DEFAULT_MATRIX='[1,0,0,0, 0,1,0,0, 0,0,1,0, 10,0,10,1]'
    )

st_components.html(ngl_html, height=600)