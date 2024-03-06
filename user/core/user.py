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
        "": "https://github.com/haeussma/test_failed_action@6220961b5310b48385e02042a0485cbcdc68dcbb#User"
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
        default="6220961b5310b48385e02042a0485cbcdc68dcbb"
    )

    def time_consuming_function(self):
        for _ in tqdm(range(100)):
            pass
