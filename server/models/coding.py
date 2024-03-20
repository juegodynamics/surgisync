from typing import Optional
from pydantic.v1 import Field

from models.base import Base


class Coding(Base):
    system: str = Field(
        default=None,
        alias="system",
        title="Identity of the terminology system",
        description=(
            "The identification of the code system that defines"
            "the meaning of the symbol in the code."
        ),
    )

    code: str = Field(
        default=None,
        alias="code",
        title="Symbol in syntax defined by the system",
        description=(
            "A symbol in syntax defined by the system. The symbol"
            "may be a predefined code or an expression in a syntax"
            "defined by the coding system (e.g. post-coordination)."
        ),
    )

    display: Optional[str] = Field(
        default=None,
        alias="display",
        title="Representation defined by the system",
        description=(
            "A representation of the meaning of the code in the"
            "system, following the rules of the system."
        ),
    )
