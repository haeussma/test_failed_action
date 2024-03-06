import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from plotly import graph_objects as go


@forge_signature
class Image(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/haeussma/test_failed_action@6d010318531f4217249085276ad65a3904f242e3#Image"
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

    type: Optional[str] = element(
        description="description",
        default=None,
        tag="type",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test_failed_action"
    )
    _commit: Optional[str] = PrivateAttr(
        default="6d010318531f4217249085276ad65a3904f242e3"
    )

    def plot(self):
        return go.Figure(go.Image(source=self.url))
