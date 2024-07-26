import streamlit as st
import streamlit.components.v1 as st_components

from string import Template

nglviewer_template = """
<html>
<head>
    <script src="https://unpkg.com/ngl@2.2.2/dist/ngl.js"></script>
</head>
<body>
    <div id="viewport" style="width:100%; height:100vh"></div>
    <script>
        const stage = new NGL.Stage("viewport");
        stage.loadFile("$STRUCTURE_URL").then(function (o) {

        o.addRepresentation("licorice")
        o.autoView()

        NGL.autoLoad("$TRAJ_URL").then(function (frames) {
            const traj = o.addTrajectory(frames).trajectory;
            const player = new NGL.TrajectoryPlayer(traj, {
            step: 1,
            timeout: 90,
            interpolateStep: 16,
            start: 0,
            end: traj.numframes,
            interpolateType: "linear",
            mode: "once",
            direction: "bounce",
            });
            player.play();
        })
        })
        </script>
        </body>
        </html>
""".strip()


ngl_html = Template(nglviewer_template).substitute(
        STRUCTURE_URL='/app/static/dump.cif',
        TRAJ_URL='/app/static/dump.nc',
    )

st_components.html(ngl_html, height=600, width=600)