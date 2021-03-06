from typing import Dict, List, Optional, Text

_variables: Dict

def get_variable(name: Text, default: Optional[Text] = ...) -> Optional[Text]: ...

class Variables:
    attach_report: bool = ...
    launch_attributes: List = ...
    launch_id: Optional[Text] = ...
    launch_doc: Optional[Text] = ...
    log_batch_size: Optional[int] = ...
    mode: Optional[Text] = ...
    pool_size: Optional[int] = ...
    skip_analytics: Optional[Text] = ...
    test_attributes: Optional[List] = ...
    skipped_issue: bool = ...
    def __init__(self) -> None: ...
    @property
    def endpoint(self) -> Text: ...
    @property
    def launch_name(self) -> Text: ...
    @property
    def pabot_pool_id(self) -> int: ...
    @property
    def pabot_used(self) -> Optional[str]: ...
    @property
    def project(self) -> Text: ...
    @property
    def uuid(self) -> Text: ...
