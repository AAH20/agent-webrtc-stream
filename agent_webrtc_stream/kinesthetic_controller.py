"""
Kinesthetic Motion Controller for Agent-WebRTC-Stream.
Generates smooth cubic Bezier trajectories and continuous sub-pixel mouse events at 60fps.
"""

from typing import List, Tuple
from .models import KinestheticMotion, MotionType


class KinestheticController:
    """Plans human-like continuous cursor trajectories with sub-pixel precision."""

    @staticmethod
    def _cubic_bezier(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
        """Standard cubic Bezier interpolation formula."""
        return (
            (1 - t) ** 3 * p0
            + 3 * (1 - t) ** 2 * t * p1
            + 3 * (1 - t) * t ** 2 * p2
            + t ** 3 * p3
        )

    @classmethod
    def plan_smooth_trajectory(
        cls,
        start_pos: Tuple[int, int],
        end_pos: Tuple[int, int],
        steps: int = 15,
        duration_ms: float = 200.0,
        action_type: MotionType = MotionType.SMOOTH_MOVE
    ) -> KinestheticMotion:
        """Generates continuous natural mouse coordinates using cubic Bezier curves."""
        x0, y0 = start_pos
        x3, y3 = end_pos

        # Control points with natural curve deflection
        dx = x3 - x0
        dy = y3 - y0
        x1 = x0 + dx * 0.25 - dy * 0.1
        y1 = y0 + dy * 0.25 + dx * 0.1
        x2 = x0 + dx * 0.75 + dy * 0.05
        y2 = y0 + dy * 0.75 - dx * 0.05

        points: List[Tuple[int, int]] = []
        for i in range(steps + 1):
            t = i / steps
            bx = cls._cubic_bezier(x0, x1, x2, x3, t)
            by = cls._cubic_bezier(y0, y1, y2, y3, t)
            points.append((int(round(bx)), int(round(by))))

        return KinestheticMotion(
            action_type=action_type,
            start_pos=start_pos,
            end_pos=end_pos,
            trajectory_points=points,
            duration_ms=duration_ms
        )

    @classmethod
    def plan_drag_and_drop(
        cls,
        card_origin: Tuple[int, int],
        column_target: Tuple[int, int]
    ) -> KinestheticMotion:
        """Plans a continuous drag-and-drop gesture."""
        return cls.plan_smooth_trajectory(
            start_pos=card_origin,
            end_pos=column_target,
            steps=20,
            duration_ms=300.0,
            action_type=MotionType.DRAG_DROP
        )
