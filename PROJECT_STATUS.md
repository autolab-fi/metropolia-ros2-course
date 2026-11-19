# ROS2 course status — 2026-11-19

## Delivered milestone

The first complete technical slice is **2.6 Reach a target point**. It runs normal
Python/rclpy in native ROS2 Jazzy, on the server for simulation and on the
Metropolia Raspberry Pi for real robot checks. The starter is complete for
integration testing. This is a technical pilot, not the complete beginner course.

Preview: https://pr-387.ondroid-org.pages.dev/user/20/ros2
Frontend draft PR: https://github.com/autolab-fi/autolab-fe/pull/387

The native main database contains course 20/task 401. Existing course permissions,
submission history and progress are used. The seed grants no new roles. The
frontend reuses the course header, dock, assignment view, editor, output timeline
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

## Qualification

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
