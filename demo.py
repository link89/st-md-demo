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
        DEFAULT_MATRIX='[]', # Ref: https://threejs.org/docs/#api/en/math/Matrix4
        # DEFAULT_MATRIX='[2,0,0,0, 0,2,0,0, 0,0,2,0, 0,0,0,1]'
        # DEFAULT_MATRIX='[1,0,0,0, 0,0.5,0.866,0, 0,-0.866,0.5,0, 0,0,0,1]'
        # DEFAULT_MATRIX='[1,0,0,0, 0,1,0,0, 0,0,1,0, 10,0,10,1]'
        REPRESENTATIONS='''[
          {"type": "ball+stick", "params": {"sele": "_li", "radiusType": "covalent", "radiusScale": 0.2,}}, 
          {"type": "licorice", "params": {"sele": "not(_li)"}}
        ]
        '''
        # REPRESENTATIONS='''[
        #   {"type": "spacefill", "params": {"sele":"not(_AA)","radiusScale":0.5,"radiusSize":0.5,"radiusType":"covalent"}},
        #   {"type": "licorice", "params": {"sele":"not(_AA)","multipleBond":"symmetric","radiusScale":0.6}},
        # ]
        # '''
    )

st_components.html(ngl_html, height=600)