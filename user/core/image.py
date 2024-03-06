import sdRDM
from plotly import graph_objects as go


from typing import Optional
from uuid import uuid4
from pydantic import PrivateAttr
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature


@forge_signature
class Image(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/haeussma/test_failed_action@4f255cf31d744edfd1931fd853db97b5197c2ba2#Image"
    },
):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    url: Optional[str] = element(
        description="description",
        default=None,
        tag="url",
        json_schema_extra=dict(),
    )

    size: Optional[float] = element(
        description="size in MB",
        default=None,
        tag="size",
        json_schema_extra=dict(),
    )

    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test_failed_action"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4f255cf31d744edfd1931fd853db97b5197c2ba2"
    )

    def plot(self):
        return go.Figure(go.Image(source=self.url))
