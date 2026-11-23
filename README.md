# ROS2 for Mobile Robotics

An English, self-paced beginner course for the Metropolia mobile robot and its
simulator. The agreed curriculum contains four modules (24 lessons) and a final
project. Development starts with the technical vertical slice **2.6 Reach a target
point**, so the complete execution path can be qualified before authoring all the
prerequisite exercises.

`manifest.json` lists runnable pilot lessons. **1.1 ROS2 sandbox** is a guided
interactive test of terminal commands, live topics, movement, reset, editing,
project execution and a saved-project laboratory check. Its files are separate
from lesson 2.6. Complete demonstrations **1.2 Read the eight line sensors**,
**1.3 Move and publish a distance topic**, and **1.4 Follow the line with the
line sensor** use ordinary ROS publishers/subscribers in both personal simulation
and the physical laboratory. Each activity has independent saved sources. `lessons/2.6/README.md` explains the
exercise and `solution.py` is its complete starter for integration testing.
`examples/reach_target.py` is the reference solution. This repository is lesson
content; execution belongs to `ondroid-ros2-runtime` and the existing physical
worker. It contains no credentials or user submissions.

The production pilot is a normal course in the main platform database. Its card
opens a separate ROS workspace using the existing dashboard header, dock,
lesson view, output timeline and checks history, with real terminal tabs and nano.
Terminals share one server-side workspace and live simulator. `check-in-sim` runs
practice from the terminal; Check in lab submits a saved project through the
physical robot's exclusive queue. Access remains controlled by
native course roles; this seed does not grant any user new privileges.

See `PROJECT_STATUS.md` for tested behavior and unfinished curriculum work.
