"""Recorded Octoliner readings: do not merge track and coloured-zone edges."""
import importlib.util
from pathlib import Path
import unittest
import rclpy
from std_msgs.msg import UInt16MultiArray
spec=importlib.util.spec_from_file_location('line_demo',Path(__file__).resolve().parents[1]/'lessons/1.4/solution.py')
demo=importlib.util.module_from_spec(spec);spec.loader.exec_module(demo)
class RegionTracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):rclpy.init()
    @classmethod
    def tearDownClass(cls):rclpy.shutdown()
    def setUp(self):self.node=demo.FollowLine()
    def tearDown(self):self.node.destroy_node()
    def sense(self,raw):self.node.sense(UInt16MultiArray(data=raw));return self.node.error
    def test_recorded_extra_left_edge_does_not_pull_the_line_away(self):
        self.sense([74,63,62,77,980,968,551,76])
        error=self.sense([72,63,371,979,948,71,927,940])
        self.assertLess(abs(error),.05)
    def test_extra_right_edge_also_stays_separate(self):
        error=self.sense([980,970,70,950,980,70,70,70])
        self.assertLess(abs(error),.05)
    def test_single_off_centre_line_can_still_steer_both_ways(self):
        self.assertLess(self.sense([960,960,100,100,100,100,100,100]),-.7)
        self.assertGreater(self.sense([100,100,100,100,100,100,960,960]),.7)
    def test_flat_reading_stops_without_forgetting_the_tracked_position(self):
        self.sense([100,100,100,960,960,100,100,100]);previous=self.node.line_index
        self.assertIsNone(self.sense([950]*8));self.assertEqual(previous,self.node.line_index)
if __name__=='__main__':unittest.main()
