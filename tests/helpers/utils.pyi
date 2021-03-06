from typing import Dict, List, Any, Optional, Tuple

DEFAULT_VARIABLES: Dict[str, Any] = ...


def run_robot_tests(tests: List[str],
                    listener: str = 'robotframework_reportportal.listener',
                    variables: Optional[Dict[str, Any]] = None) -> int: ...


def get_launch_log_calls(mock) -> List[Tuple[List[Any], Dict[str, Any]]]: ...
