"""
Data models and typed schemas for Agent-WebRTC-Stream.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Any
import time


class MotionType(str, Enum):
    SMOOTH_MOVE = "smooth_move"
    DRAG_DROP = "drag_drop"
    INERTIAL_SCROLL = "inertial_scroll"
    SUBPIXEL_CLICK = "subpixel_click"


@dataclass
class KinestheticMotion:
    action_type: MotionType
    start_pos: Tuple[int, int]
    end_pos: Tuple[int, int]
    trajectory_points: List[Tuple[int, int]] = field(default_factory=list)
    duration_ms: float = 150.0
    pressure: float = 1.0


@dataclass
class VideoTileFrame:
    frame_id: int
    timestamp: float
    width: int = 1280
    height: int = 800
    fps: int = 60
    bitrate_kbps: int = 2500
    dirty_rects: List[Tuple[int, int, int, int]] = field(default_factory=list) # [(x, y, w, h)]
    is_keyframe: bool = False
    delivery_latency_ms: float = 8.5


@dataclass
class StreamSessionStats:
    total_frames_rendered: int
    avg_latency_ms: float
    fps_delivered: float
    dropped_frames: int
    bandwidth_kbps: float
    cursor_events_dispatched: int
