import abc
import typing

from pydantic.v1 import BaseModel, Field

from models.extension import Extension


class Base(BaseModel, abc.ABC):

    extension: typing.Optional[typing.List[Extension]] = Field(
        default=None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that "
            "is not part of the basic definition of the resource. "
            "To make the use of extensions safe and managable, there "
            "is a strict set of governance applied to the definition "
            "and use of extensions. Though any implementer can define "
            "an extension, there is a set of requirements that SHALL be "
            "met as part of the definition of the extension."
        ),
    )
