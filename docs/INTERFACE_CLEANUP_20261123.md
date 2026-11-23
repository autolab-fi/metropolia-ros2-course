# ROS interface cleanup and smooth display — 2026-11-23

Preview: https://pr-399.ondroid-org.pages.dev/user/20/ros2
Frontend PR: https://github.com/autolab-fi/autolab-fe/pull/399

Frontend source 959309a is deployed to PR 399; production frontend is unchanged.
Simulator source 3650baf is in main and deployed to the existing simulator host.
The ROS-only adapter is backward compatible with older ROS frontends. Shared
HamkThreeView/LineRobot/OpenCV renderer code was not modified.

## Final interface

- Independent Simulator and Lab Dockview modules replace the combined panel.
  Lab initially shares the Output tab group and can be moved independently.
- Simulator contains only the scene, without source buttons, counters or status
  banners. The obsolete RobotView and WorkspaceStatus components were removed.
- TopicsPanel shows only current-session ROS messages. There are no Live
  workspace/Saved attempt controls. Selecting check history cannot replace these
  messages. Lab receives only physical-attempt data and shows measured trajectory.
- RobotScene is a ROS-only iframe adapter; SimulationPanel and LabPanel supply
  their own data and interpolation settings. Existing shared players/dock/terminal
  transport components are unchanged. ROS layout v4 replaces the obsolete panel
  layout without affecting project sources or check history.

## Motion

The model still publishes at 10 Hz; the browser polls around every 250 ms plus
request time. Previously the scene jumped directly between those sparse poses.
PoseTween now renders intermediate received positions and shortest angular
transitions with a bounded adaptive 100–600 ms display interval. It never predicts
new motion beyond the last received target. Reset/new sessions/large jumps and
saved observations snap immediately. Stationary and hidden views stop drawing.
No control loop, physical motion, grading, timeout or velocity limit changed.

## Validation

- Simulator unit tests: 68 passed, including four new interpolation cases.
- TypeScript and frontend build passed; svelte-check: zero errors, existing
  warnings retained.
- ROS renderer browser tests: two passed. Changing/sparse telemetry interpolates;
  idle/saved observations stop rendering; camera interaction and resize still work.
- HAMK/Metropolia selected simulator browser tests: two passed, including actual
  embedded Python execution for Metropolia.
- Existing OpenCV image/video/stop browser test: passed, including continuous
  virtual-camera processing with the unchanged camera renderer.
- ROS UI fixture: passed for separate panels, removal of counters/source buttons,
  current workspace topics and preserved selected-task submission identity.
- Real PR-preview browser with production APIs and ROS containers: passed at
  1920×1080, 1440×900, 1024×768 and 390×844. Actual terminal-published velocity moved
  the virtual model. The scene drew 24 frames across two received pose packets;
  after stopping it drew zero frames in the measured idle interval. This verifies
  interpolation, not a promised hardware-independent FPS.
- Opening saved physical submission 25862 populated Lab while Simulator remained
  separate. ROS Topics continued showing the current personal model's pose rather
  than saved laboratory coordinates. Polling resumed/advanced with terminal panels
  hidden on mobile. Tests wait for editable terminal input and advancing data after
  resize instead of assuming fixed asynchronous startup/resize timing.
- No browser exceptions. The personal QA session was explicitly ended. No new
  physical robot execution, worker restart, firmware change or queue change was
  needed for this display-only update; saved physical history was read-only.

Evidence: [validation/interface-cleanup-20261123.json](validation/interface-cleanup-20261123.json).
Both frontend CI checks passed. The explicit simulator publishing workflow also
passed; it ran from the feature ref with production frontend publication false.
PR 399 remains the review URL.

## Actual interfaces and camera proposal

The ROS image currently provides rclpy, PoseStamped/Twist, sensor_msgs definitions,
colcon, nano and shared terminals. Robot interfaces are /robot/pose,
/robot/cmd_vel and /simulation/reset. The runtime image was probed: cv2 and
cv_bridge are absent. No camera, line-sensor, encoder, IMU, range or battery topic
is wired into the ROS pilot, even where geometry/sensor models exist elsewhere
in the common simulator.

OpenCV already uses HamkThreeView.captureCamera(640,480), an independent overhead
camera producing BGR pixels. It can underpin a future ROS sensor source. That
requires a bounded renderer/frame bridge, a sensor_msgs/Image publisher, native
OpenCV/cv_bridge in the ROS image and a separate image-view panel for original
and student-processed topics. Student nodes should use standard ROS messages and
cv2, then optionally publish the existing cmd_vel for vision control. Prefer the
same overhead perspective as the physical laboratory initially; an onboard virtual
viewpoint is another renderer mode, not existing onboard hardware. This proposal
is not implemented by the interface cleanup. See PROJECT_STATUS for its intended
server-side/session isolation boundaries.

## Documentation deployment

Only the published lesson 1.1/2.6 Markdown and project status were atomically
refreshed. Manifest, starter code, checker parameters and runtime image pins were
unchanged. No backend/ROS service restart was needed. Rollback copies and refresh
metadata are in /var/backups/ondroid/ros2-clean-ui-20261123 on the server. The source
instructions match the new module names and no longer reference removed controls.
