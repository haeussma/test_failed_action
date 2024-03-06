import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from tqdm import tqdm
from .image import Image


@forge_signature
class User(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/haeussma/test_failed_action@f9f0e8c3a2523cf520a3c3de355622cc4604225b#User"
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
        default="f9f0e8c3a2523cf520a3c3de355622cc4604225b"
    )

    def time_consuming_function(self):
        for _ in tqdm(range(100)):
            pass
