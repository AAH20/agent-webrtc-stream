"""
Unit tests for Agent-WebRTC-Stream using standard unittest.
"""

import unittest
from agent_webrtc_stream.models import MotionType
from agent_webrtc_stream.webrtc_pipeline import WebRTCPipeline
from agent_webrtc_stream.kinesthetic_controller import KinestheticController


class TestAgentWebRTCStream(unittest.TestCase):
    def test_webrtc_frame_generation(self):
        pipeline = WebRTCPipeline(target_fps=60, width=1280, height=800)
        frame1 = pipeline.generate_next_frame()

        self.assertEqual(frame1.frame_id, 1)
        self.assertTrue(frame1.is_keyframe)
        self.assertLess(frame1.delivery_latency_ms, 15.0)

        frame2 = pipeline.generate_next_frame()
        self.assertEqual(frame2.frame_id, 2)
        self.assertFalse(frame2.is_keyframe)

    def test_bezier_trajectory_planning(self):
        start = (100, 100)
        end = (500, 500)
        motion = KinestheticController.plan_smooth_trajectory(start, end, steps=10)

        self.assertEqual(motion.action_type, MotionType.SMOOTH_MOVE)
        self.assertEqual(len(motion.trajectory_points), 11)
        self.assertEqual(motion.trajectory_points[0], start)
        self.assertEqual(motion.trajectory_points[-1], end)

    def test_drag_and_drop_planning(self):
        motion = KinestheticController.plan_drag_and_drop((50, 50), (200, 200))
        self.assertEqual(motion.action_type, MotionType.DRAG_DROP)
        self.assertEqual(len(motion.trajectory_points), 21)

    def test_session_stats_aggregation(self):
        pipeline = WebRTCPipeline(target_fps=60)
        for _ in range(5):
            pipeline.generate_next_frame()

        stats = pipeline.get_session_stats(cursor_events_count=10)
        self.assertEqual(stats.total_frames_rendered, 5)
        self.assertEqual(stats.fps_delivered, 60.0)
        self.assertLess(stats.avg_latency_ms, 12.0)
        self.assertEqual(stats.cursor_events_dispatched, 10)


if __name__ == "__main__":
    unittest.main()
