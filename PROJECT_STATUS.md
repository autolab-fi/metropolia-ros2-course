# ROS2 course status — 2026-11-23

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
