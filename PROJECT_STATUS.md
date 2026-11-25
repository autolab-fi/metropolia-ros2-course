# ROS2 course status — 2026-11-25

Production: [ROS2 course](https://ondroid.org/user/20/ros2).
Latest frontend [PR401](https://github.com/autolab-fi/autolab-fe/pull/401) is merged
as `822a407`; publication workflow `45585862613` succeeded for frontend and simulator.
The production browser rechecked personal node discovery, saved physical nodes,
node-to-topic links, sensor display, video playback and source switching without
page JavaScript errors. Full qualification is recorded in the Inspector section below.
The previous PR399 checkpoint passed all three terminal/practice flows, sensor
lab check **25872**, and the same stand's LineRobot simulation **25873** and physical
check **25874** with live video.
Detailed architecture, immutable pins and qualification evidence are in the
[release report](https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/LINE_SENSOR_DEMOS_20261123.md).

## 55-second line-following update — 2026-11-24

Lesson 1.4 now follows the track for 55 seconds in both the personal simulator
and physical checks, then publishes zero velocity and logs completion. It no
longer stops at the first green square/nearby goal. The node remains running
until Ctrl+C. The physical 60-second active limit and all existing motion,
sensor-freshness and stop guards remain in force. Only this timed activity can
use the full-track pose region; older target activities retain their original
smaller region. Timed grading independently requires actual travel/displacement
and sustained forward commands, not just waiting for the timer.

Longer physical runs exposed several distinct dark regions over coloured-zone
edges. The reference now tracks one contiguous sensor region nearest the previous
line position instead of averaging unrelated regions. Recorded readings have
four real-rclpy regression tests. Physical check **25877 passed**: 55 seconds of
following, 0.775 m camera-measured travel, all 421 readings line-visible, and
confirmed stop/device release. A subsequent production LineRobot test drive
**25879 passed**, proving the shared stand/queue can serve the next course.
The final published program was also run through the production browser for the
full duration. Its ROS container simulation measured about 2.2 m travel.

The same frontend remains deployed; this update changes course, runtime, API and
physical ROS activity only. Starting a new session upgrades an exact unmodified
old reference, including the first timed reference. Edited student files are
preserved. Save nano, stop the old node, End session and Start session to load the
updated reference. Check-in-sim uses the same 55-second requirements.

Details: [timed release report](https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/TIMED_LINE_FOLLOW_20261124.md).

## Laboratory video and topics update — 2026-11-24

Lab contains the shared LineRobot video player: live overhead camera during a
physical check, followed by the authorized saved recording. Physical pose,
commands, line sensors and distance appear in ROS Topics with a Laboratory label.
Selecting Simulator returns to personal-session values. This does not add a ROS
camera topic. The existing media server retains the last three recordings per user.

Physical ROS **25883 passed** with 55 seconds of line following, advancing live
video, 102 physical topic updates, a playable 640×480 recording, and confirmed
stop/release. The next ordinary Metropolia LineRobot **25884 passed**. Browser
checks covered desktop, tablet and mobile playback/source switching with no page
JavaScript errors. The final queues are empty and the charging cron is idle.

Details: [video/topics release report](https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/LAB_VIDEO_TOPICS_20261124.md).
Frontend: [PR400](https://github.com/autolab-fi/autolab-fe/pull/400), merged and
published to production. Recording playback and source switching were rechecked
on production with no page JavaScript errors.

## ROS Inspector update — 2026-11-25

The existing ROS Topics module becomes **ROS Inspector**, with **Topics** and
**Nodes** views in the same dock panel. Topics discovers learner-created names,
types, endpoint counts, observed frequency and bounded message previews. Nodes
shows actual node names and their publishers/subscriptions, linking to Topics.
System topics are hidden by default. The eight-channel line sensor display is
reused when that topic is selected. No file browser, editor or additional panel
is added. Lab continues to show only live camera and recorded video.

The same observer runs in personal simulation and each isolated lab check.
Selecting Simulator returns to the personal graph; Check in lab or selecting a
lab result selects the physical graph. After completion the latest snapshot keeps
its timestamp. The terminal always belongs to the personal simulation. Snapshots
are diagnostic only and cannot supply grading/motion evidence. Standard-message
student topics require no registration; custom interface types need to be installed
in the runtime for message previews. Large sensor payloads have metadata only.

All current examples passed through the PR401 browser and on the real robot:
**25885** sandbox, **25886** sensor monitor, **25887** distance with an additional
student node publishing `/student/error`, **25888** 55-second line following.
The custom node/topic appeared in both environments. Each check had live graph
updates, live camera, playable recording and confirmed release. The following
ordinary LineRobot **25889 passed**, and both queues were empty. Inspector was
checked at desktop, tablet and mobile widths with no page JavaScript errors.

Frontend CI passed 110 unit and 29 browser foundation tests; runtime tests 21,
API/claim tests 13. Real ROS container acceptance passed all four existing demos
and custom publisher discovery/removal through the PTY. Lessons explain how to
find each demonstration node and inspect its topics.

[PR401](https://github.com/autolab-fi/autolab-fe/pull/401) is merged and published
to production. See the [architecture/qualification report](https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/INSPECTOR_20261125.md).

## Current interactive demonstrations

Course 20 contains complete English integration demonstrations, with independent
saved sources for each activity:

| Lesson | Native task | Behavior | Browser simulator | Metropolia laboratory submission |
| --- | --- | --- | --- | --- |
| 1.1 ROS2 sandbox | 409 | Inspect graph, drive, edit and run a node | Passed | **25885 passed** |
| 1.2 Read the eight line sensors | 410 | Subscribe to UInt16MultiArray; remain stopped | Passed | **25886 passed** |
| 1.3 Move and publish a distance topic | 411 | Pose feedback, Twist and Float32 displacement | Passed | **25887 passed** |
| 1.4 Follow the line with the line sensor | 412 | Track one sensor region for 55 seconds | Passed | **25888 passed** |
| 2.6 Reach a target point | 401 | Original pose-feedback reference | Passed again in container acceptance | Previously qualified; controller path unchanged |

These are runnable playgrounds for testing the environment, not the completed
beginner curriculum. The 24-lesson plan still needs step-by-step teaching material.

Starting Linux starts the personal ROS simulation on the server. Up to four PTYs
share the same source files, ROS graph and simulator; they do not reserve the Pi.
`bash run.sh` launches the single-file demos directly in ROS (about 2 seconds on
the server), while the full ament package and optional colcon workflow remain.
`check-in-sim` resets/runs practice; Check in lab freezes the actual `src/` and
`run.sh` for an isolated ARM64 run through the existing exclusive robot queue.
The first explicit zero command starts hardware telemetry while stopped.

On 2026-11-23, physical demo startup measured 10.7–11.2 seconds. Active checks measured 3.5 seconds
(sensor monitor), 17.6 seconds (pose movement) and 15.6 seconds (the former short line-following demo). The 2026-11-24 timed version is qualified above.
The first movement trial at 0.03 m/s stalled and timed out; the complete movement
starters now use the previously qualified 0.04 m/s, within unchanged platform caps.
Simulation remains ideal kinematics: it does not model this low-speed motor limit.

## Interface and live data

Simulator and Lab are separate Dockview modules, visible in their own right-hand
panels on desktop. Layout version 5 gives the simulator and physical observation
usable height; students can rearrange them. Simulator contains only the scene.
ROS Inspector automatically shows physical attempt messages after Check in lab or
selecting a lab result, including measured pose, commands, eight physical sensor
readings and student-published displacement. Selecting Simulator returns to the
personal session topics. A source label identifies Laboratory or Simulator;
there are no source buttons, sample counters or Saved attempt / Live workspace
labels. Completed physical values retain their observation timestamps. Lab contains
only the shared LineRobot video player: real overhead camera during a check,
then its authorized saved recording. Old attempts without video show an empty state.
Saved outcomes and logs remain in Checks and Output.

The ROS scene interpolates live pose packets between browser polls without
extrapolating. Saved observations/reset/new sessions snap, and rendering stops
at rest/hidden. Eight sensor highlights reflect the selected data source;
ADC noise with the same detection pattern does not trigger idle redraws.
The goal/tolerance comes from the selected exercise; stationary and timed
line-following demos have no destination marker. New UI and renderer changes are isolated to ROS.
Shared dashboard typography/styles and LineRobot/OpenCV players are unchanged.
The new ROS video adapter uses the existing player without modifying it.

Real browser tests covered manual terminal execution, changing live pose, actual
sensor/custom topics, terminal practice, snapshot submission, physical readings
and completed checks. ROS panels were checked at 1920×1080, 1440×900, 1024×768 and
390×844. An existing shared header can overflow by 8 px at 390 px with the long QA
display name “Test administrator”; the ROS dock fits, and no shared header styles
were changed for this release. With a short QA name the full page fits all sizes.

## Sensor bridge and execution boundaries

`/ondroid_bridge` publishes `/robot/pose` (PoseStamped) and
`/robot/line_sensors` (UInt16MultiArray), and receives `/robot/cmd_vel` (Twist).
The eight ADC channels are ordered from 0/right to 7/left. Demo nodes publish
`/demo/distance` (Float32); this learner-controlled topic is display-only.
The simulator samples the existing Metropolia line mask at a provisional virtual
sensor bar. Its ADC values/board geometry are illustrative, not hardware calibration.

The physical worker optionally adds trusted Octoliner polling to its existing
bounded MicroPython motion controller. SoftI2C transactions and telemetry writes
are bounded; readings carry a controller execution ID and monotonic sequence.
The host rejects retained, invalid, out-of-order or wrong-execution messages and
uses its own receipt time for freshness. No firmware flash was necessary. The
old ROS target and OpenCV use the original controller path without sensor I/O.

Course metadata selects the checker/goal/launch preset, never browser input.
The stationary checker rejects movement before dispatch. Sensor-dependent checks
stop on missing/stale readings; following also stops on persistent line loss.
Pose grading still uses the camera independently. Existing deadman, 60-second
active limit, wheel/velocity caps, exclusive allocation, reset, confirmed stop
and device release remain in force. Sensor cutoff and forbidden monitor movement
were also tested with real ROS containers.

## Dock observation from the 2026-11-23 release

All course qualifications above passed. On the final return to the magnetic dock,
normal AutoCharge confirmed three samples twice, but later idle telemetry changed
to charging false. An existing zero-offset DockAlignment cycle could not confirm
dock exit. The final fleet sample is true again; sustained charging is therefore
not established. Check physical contact/telemetry separately before relying on
unattended docking. No docking settings or firmware were changed. Worker/camera
remain online, no checks or QA sessions are active, maintenance is off and the
normal charging cron is restored. See the backend release report for evidence.

## Remaining extensions

Camera, encoders, IMU, range and battery have no learner-facing ROS topics yet.
The OpenCV simulator already renders 640×480 overhead frames, but this is not a
ROS image publisher. The ROS orbit scene is visualization, not a camera feed.
`cv2` and `cv_bridge` are not installed in the current development image.

A next camera extension can publish `sensor_msgs/Image` on `/camera/image_raw`,
install OpenCV/cv_bridge and let ordinary rclpy nodes publish `/camera/processed`.
It needs a canonical frame producer per server workspace; authoritative grading
must not silently depend on an open browser renderer. Begin at 640×480 / 5 fps
and measure resources. A robot-mounted virtual view is an additional mode, not
an existing onboard physical camera. Students should continue to use ROS topics,
without MQTT credentials or a special control library.

---

## Historical checkpoints

## Previous live sandbox checkpoint

## Live sandbox checkpoint

The pilot now includes **1.1 ROS2 sandbox: observe, drive and run a node** and
**2.6 Reach a target point**. Sandbox uses the same proven physical goal, with
additional simulation-only CLI experiments. Both complete starters use ordinary
rclpy. The first is an integration playground, not the finished beginner module.

Starting a terminal session starts a real ROS2 simulator in that server container.
Run `bash run.sh` or publish `/robot/cmd_vel` from any of its four shared-file
terminals: the scene updates without a check. `/robot/pose` is published at 10 Hz;
the browser requests current telemetry about every 250 ms. ROS Topics now has
separate Live workspace and Saved attempt sources. A host-received pose sequence
advances even when stationary; lack of updates is labelled interrupted after
2 seconds. This is interactive feedback, not a hard real-time guarantee.

Each exercise retains its own source backup. Switching lessons saves and ends
the prior session; save nano first. Check in lab freezes that selected exercise's
`src/` and `run.sh`. Shell commands, transient ROS parameters and processes do not
transfer. Lab grading still observes the physical camera independently and uses
the same exclusive Python/OpenCV/ROS robot worker, reset and stop workflow.
Physical firmware, queues and worker images are unchanged by this checkpoint.

Runtime tests qualify ordinary terminal-driven movement (without check-in-sim),
Ctrl+C stopping, reset, independent sources, four terminals, terminal close,
restore, source-only project execution and owner isolation. Backend tests cover
sandbox task/template selection and immutable attempt identity. Deployment and
browser qualification details are maintained in the backend release report.

The original frontend pilot PR 387 has merged; the ROS course is available from
production at https://ondroid.org/user/20/ros2. Live sandbox UI is reviewed in a
new frontend PR [#399](https://github.com/autolab-fi/autolab-fe/pull/399), with
preview https://pr-399.ondroid-org.pages.dev/user/20/ros2.

Sandbox laboratory check **25862** passed on Metropolia on 2026-11-23: the
saved package rebuilt on ARM64 (28.487 s startup), reached the goal and stopped
(14.786 s active execution, 114 commands, 0.0148 m final distance). The complete
interactive terminal/scene/topic workflow also passed in a real browser without
API mocks. Existing physical worker/firmware and queue were retained.

Remaining: author the beginner curriculum step by step, additional topics and
sensors, simulated camera/encoder realism, and an actual physical video panel.
The current Lab attempt view shows measured pose trajectories, not camera video.

---

The following is the historical 2026-11-19 technical qualification.

## Original delivered milestone — 2026-11-19

## Delivered milestone

The first complete technical slice is **2.6 Reach a target point**. It runs normal
Python/rclpy in native ROS2 Jazzy, on the server for simulation and on the
Metropolia Raspberry Pi for real robot checks. The starter is complete for
integration testing. This is a technical pilot, not the complete beginner course.

Preview: https://pr-387.ondroid-org.pages.dev/user/20/ros2
Frontend draft PR: https://github.com/autolab-fi/autolab-fe/pull/387

The native main database contains course 20/task 401. Existing course permissions,
submission history and progress are used. The seed grants no new roles. The
frontend reuses the course header, dock, assignment view, output timeline
and checks components through separate ROS adapters. ROS Topics displays selected
message field paths, units and original observation times. The robot view uses
the existing Metropolia 3D scene, including for saved pose trails.

There is one physical worker for Python/LineRobot, OpenCV and ROS. It keeps the
same atomic device claim, Temporal device queue and single physical activity
slot. ROS is a separate sandbox container inside an allocated activity. Existing
reset, motion limits, robot-local deadman, confirmed stop and workflow completion
are reused. No robot firmware flash was required.

Learner code has no MQTT credentials, Docker socket or host network. The host
observes the camera independently and controls grading. Request keys and source
hashes link each result to one saved submission; old results never replay code.
The server also repairs lost completion listeners by observing the exact
Temporal run ID, without starting another execution.

Simulation has real ROS2 execution and ideal fixed-step differential-drive
kinematics. Its browser scene is display-only. It does not model motor PID,
magnetic docking or slip. Physical `robot/pose` currently describes the camera
tag centre, converted to a right-handed ROS map (metres/radians), not wheel
odometry or calibrated base_link. Requested speed can differ from measured speed.

## Interactive environment checkpoint

The ROS route now opens a personal Linux workspace on the server, with up to four
real bash/PTY terminals and nano. All terminals share `/workspace/ros2_ws`; shell
working directories and environment changes remain separate. The former
single-file browser editor adapter was removed. Existing Linux, LineRobot and
OpenCV course components/gateways are unchanged.

Students inspect ROS nodes/topics, edit their package, build with colcon and run
it continuously in their own simulator. `check-in-sim` resets the practice model,
builds/runs `run.sh` and prints practice feedback. This never reserves the robot
or grants a laboratory grade. The view can switch between Simulator and Lab
attempt. The model is still ideal differential-drive kinematics, not camera
simulation or wheel/physics modeling.

Check in lab freezes `src/` and `run.sh` into the native submission, then uses the
existing shared physical queue. The Pi rebuilds for ARM64 in its isolated
sandbox. A complete project has a separate 45-second startup limit; active motion
remains at most 60 seconds. Plain Python startup stays at 15 seconds. Users can
continue editing while the submitted snapshot waits or executes. Laboratory Stop
remains available even after the personal development session ends.

Each development session is limited to 1 CPU, 768 MiB RAM, 128 PIDs, 256 MiB
workspace tmpfs and 128 MiB temporary storage, with no network/host mounts. Pilot
capacity is two concurrent sessions, not a measured production capacity. The
manager runs on the server and does not consume the robot Pi's resources.

Sessions last 30 minutes, with a 10-minute keyboard idle limit. Sources are backed
up every 30 seconds, before a lab check and on explicit End; one latest backup
per user/course is retained privately. Only UTF-8 source files in src/ and run.sh
are portable (64 files, 64 KiB per file, 192 KiB total); build/install/log,
unsaved nano buffers and running processes are temporary. A new session restores
the last saved sources. HTTP terminal input has retry acknowledgments and browser
ownership fencing; terminal output is bounded. An init process reaps terminated
ROS children. Manager cleanup is scoped to its own container label.

Before scaling beyond this pilot: load-test simultaneous builds and continuous
nodes, replace/batch the current bounded HTTP terminal polling as needed, add
session routing and durable shared source storage for multiple managers. No
multi-server automatic scaling or full beginner curriculum is claimed yet.

## Qualification

The interactive workspace milestone additionally passed browser nano editing,
shared files, practice simulation, reload recovery and four viewport sizes.
The project check on the real robot passed with 29.422 s startup, 17.115 s active
control and 1.47 cm endpoint error. Ending development and then stopping the lab
check confirmed cancellation/device release in 5.143 s. Existing native LineRobot
test_drive and OpenCV 3.5 checks passed on the final worker, and both browser
simulations passed. Backend: 38 tests; project format: 3 tests; ARM64: 13 tests.

The initial dock-release attempt failed its existing movement confirmation, and
the old 15-second startup budget was too short for package build/ROS launch.
The qualified project path now has a separate 45-second startup budget; active
motion remains limited to 60 seconds. Dock limits were not relaxed. Normal
AutoCharge subsequently confirmed charging with three stable samples and its
cron was restored. No maintenance lease or active ROS attempt was left behind.

Interactive qualification and deployment evidence:
https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/WORKSPACE_QUALIFICATION_20261119.md

The results below are the earlier single-file pilot qualification:

- Real ROS2 target check passed on Metropolia: 127 commands, 15.843 s active
  control, about 1.65 cm endpoint error (3 cm tolerance). A final Check in lab
  from the published frontend also passed in 31.552 s with 2.45 cm endpoint error.
- Published frontend simulation passed with the shared 3D scene and no browser
  errors. The physical-motion Stop test cancelled the attempt and confirmed
  cleanup/device release in 4.626 s.
- Existing native LineRobot welcome and three-second test-drive checks passed.
- OpenCV 3.5 passed on the updated worker, with original and processed H.264
  recordings, both 640×480 and 75 frames. Existing LineRobot and OpenCV browser
  simulation checks also passed in the same preview.
- Backend: 32 isolated PostgreSQL/queue/stop tests pass. Worker: 13 ARM64 tests
  pass. Four real-container ROS sandbox scenarios have their expected outcomes.
  Frontend type check/build pass; four viewport sizes were checked.

The magnetic dock observer now waits for delayed camera evidence after two fresh
battery receipts. It does not repeat or strengthen the release pulse, and retains
all existing movement/contact limits. A real dock departure passed with this
observer. Ordinary docking can still require retries; do not claim unattended
reliability before repeated dock-cycle qualification.

Two independent baseline checks remain red: the simulator's old HAMK metadata
assertion expects all lessons to use one execution mode, and frontend npm audit
flags the existing SvelteKit dependency. The former reproduces on untouched main;
the latter uses a lockfile identical to main. The frontend remains a draft PR.

Detailed evidence and installed versions:
https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/ros2/QUALIFICATION_20261119.md

## Next implementation order

The agreed course is four modules (24 lessons) and a capstone. Only the technical
2.6 fixture is runnable so far. Before student publication:

1. Author module 1 from zero: Python/ROS concepts, nodes, timers, publishers,
   subscribers, reactions and parameters. Add independent lesson fixtures and
   checkers, and expose only each lesson's relevant panels/topics.
2. Build module 2's progression toward the proven target-point lesson: read pose,
   velocity, explicit stop, measured distance and turn-toward-target feedback.
3. Extend the trusted robot service-program telemetry bridge for encoders,
   line/color sensors and battery. Preserve cumulative encoder session values
   across the existing primitive/stop resets. Do not publish synthetic physical
   readings. Qualify base_link/TF, requested speed and odometry before teaching it.
4. Author modules 3/4: sensor interpretation, line error, proportional steering,
   limits, line-loss stop, speed changes and target-color state transitions.
5. Qualify the capstone and normal course publishing/admin/LTI/certificate flows,
   repeated dock cycles, cancellation/failure cases and representative existing
   LineRobot/OpenCV checks. Other labs need their own qualified geometry and
   start/dock profiles; none are enabled by this pilot.

The accepted full plan is maintained in the backend:
https://github.com/autolab-fi/ondroid-backend-server/blob/main/devops/docker/METROPOLIA_ROS2_PLAN.md

The final normal charge cycle was confirmed with three stable samples, and the
charging cron was restored. The native pilot card directs to PR 387 while the
production frontend still awaits review.
