import sdRDM

from typing import Optional
from uuid import uuid4
from pydantic import PrivateAttr
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature


from .image import Image


@forge_signature
class User(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/haeussma/test_failed_action@4f255cf31d744edfd1931fd853db97b5197c2ba2#User"
    },
):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: Optional[str] = element(
        description="description",
        default=None,
        tag="name",
        json_schema_extra=dict(),
    )

    email: Optional[str] = element(
        description="description",
        default=None,
        tag="email",
        json_schema_extra=dict(),
    )

    image: Optional[Image] = element(
        description="description",
        default_factory=Image,
        tag="image",
        json_schema_extra=dict(),
    )

    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test_failed_action"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4f255cf31d744edfd1931fd853db97b5197c2ba2"
    )
