import streamlit as st
import streamlit.components.v1 as st_components

from string import Template

nglviewer_template = """
<html>
  <head>
    <script src="https://unpkg.com/ngl@2.2.2/dist/ngl.js"></script>
  </head>
  <body>
    <div id="viewport" style="width:100%; height:400px;"></div>
    <div style="margin-top:12px;display:flex;align-item:center">
      <button id="playBtn"></button>
      <input id="slider" type="range" style="flex-grow:1" value="0" />
    </div>
    <script>
        const playIcon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:24px"><path fill-rule="evenodd" d="M4.5 5.653c0-1.427 1.529-2.33 2.779-1.643l11.54 6.347c1.295.712 1.295 2.573 0 3.286L7.28 19.99c-1.25.687-2.779-.217-2.779-1.643V5.653Z" clip-rule="evenodd" /></svg>'

        const pauseIcon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:24px"><path fill-rule="evenodd" d="M6.75 5.25a.75.75 0 0 1 .75-.75H9a.75.75 0 0 1 .75.75v13.5a.75.75 0 0 1-.75.75H7.5a.75.75 0 0 1-.75-.75V5.25Zm7.5 0A.75.75 0 0 1 15 4.5h1.5a.75.75 0 0 1 .75.75v13.5a.75.75 0 0 1-.75.75H15a.75.75 0 0 1-.75-.75V5.25Z" clip-rule="evenodd" /></svg>'

        let player;
        let playStatus = false;

        const __playBtn = document.getElementById("playBtn")
        const __slider = document.getElementById("slider")

        const handlePlayStatusChange = (status) => {
        playStatus = status;
        if (playStatus) {
            __playBtn.innerHTML = pauseIcon;
        } else {
            __playBtn.innerHTML = playIcon;
        }
        }

        const handlePlayFrameChange = (value, max) => {
            // console.log(value, max, __slider.max)
            __slider.value = value;
            __slider.setAttribute('max', max)
        }

        const handleSliderChange = (evt) => {
            const value = evt.target.value;
            if (!player) {
                return;
            }
            // console.log(player.traj.currentFrame, value)
            if (player.traj.currentFrame !== value) {
                player.traj.setFrame(value);
            }
        }

        const handlePlayBtnClick = () => {
            // console.log({playStatus})
            if (playStatus) {
                
                player.pause();
                handlePlayStatusChange(false)
            } else {
                player.play();
                handlePlayStatusChange(true)
            }
        }

        __playBtn.addEventListener("click", handlePlayBtnClick);
        __slider.addEventListener("input", handleSliderChange);
        __slider.addEventListener("mousedown", () => {
        if (player) {
            player.pause();
        }
        });
        __slider.addEventListener("mouseup", () => {
        if (player && playStatus) {
            player.play();
        }
        });

      const stage = new NGL.Stage("viewport", {
        backgroundColor: "$BACKGROUND_COLOR",
        clipMode: "camera",
        clipScale: "absolute",
        clipNear: 0.01,
        clipFar: 100000,
        fogNear: 0.01,
        fogFar: 100000,
        });

      window.addEventListener( "resize", function( event ){
            stage.handleResize();
      }, false );

      stage.loadFile("$STRUCTURE_URL").then(function (o) {
        o.addRepresentation("ball+stick");
        o.autoView();

        NGL.autoLoad("$TRAJ_URL").then(function (frames) {
          const traj = o.addTrajectory(frames).trajectory;
          player = new NGL.TrajectoryPlayer(traj, {
            step: 1,
            timeout: 90,
            interpolateStep: 16,
            start: 0,
            end: traj.numframes,
            interpolateType: "linear",
            // mode: "once",
            // direction: "bounce",
          });
          player.play();
          handlePlayStatusChange(true)
          player.traj.signals.frameChanged.add(value => {
            handlePlayFrameChange(value, frames.coordinates.length)
          });
        });
      });
    </script>
  </body>
</html>
""".strip()


ngl_html = Template(nglviewer_template).substitute(
        STRUCTURE_URL='/app/static/dump.cif',
        TRAJ_URL='/app/static/dump.nc',
        BACKGROUND_COLOR='#ffffff'
    )

st_components.html(ngl_html, height=600, width=600)