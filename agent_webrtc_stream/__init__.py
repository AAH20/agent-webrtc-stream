"""
Agent-WebRTC-Stream: Sub-10ms 60fps Computer-Use WebRTC Video & Kinesthetic Streamer.
Enables real-time 60fps video interaction and bezier-curve continuous cursor kinematics for GPT-6 Astra.
"""

from .models import (
    MotionType,
    KinestheticMotion,
    VideoTileFrame,
    StreamSessionStats,
)
from .webrtc_pipeline import WebRTCPipeline
from .kinesthetic_controller import KinestheticController

__version__ = "1.0.0"
__all__ = [
    "MotionType",
    "KinestheticMotion",
    "VideoTileFrame",
    "StreamSessionStats",
    "WebRTCPipeline",
    "KinestheticController",
]
