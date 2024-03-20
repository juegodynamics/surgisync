from typing import Optional, Dict, Any, List
from pydantic.v1 import BaseModel, Field


class Extension(BaseModel):
    url: str = Field(
        default=None,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - "
            "a logical name or a URL."
        ),
    )

    value: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="value",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data types"
        ),
    )

    extension: Optional[List["Extension"]] = Field(
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
