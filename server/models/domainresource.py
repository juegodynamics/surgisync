import typing

from pydantic.v1 import Field
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import PydanticValueError

from . import base, common


class WrongResourceType(PydanticValueError):
    code = "wrong.resource_type"
    msg_template = "Wrong ResourceType: {error}"


class DomainResource(base.Base):
    resourceType: str = ...  # type: ignore

    id: typing.Optional[common.Id] = Field(
        default=None,
        alias="id",
        title="Logical id of this artifact",
        description=(
            "The logical id of the resource, as used in the URL"
            "for the resource. Once assigned, this value never changes"
        ),
    )

    identifier: typing.Optional[typing.List[common.Identifier]] = Field(
        default=None,
        alias="identifier",
        title="External Ids for this item",
        description=(
            "A string, typically numeric or alphanumeric, that "
            "is associated with a single object or entity within "
            "a given system. Typically, identifiers are used to "
            "connect content in resources to external content "
            "available in other frameworks or protocols. Identifiers "
            "are associated with objects and may be changed or "
            "retired due to human or system process and errors."
        ),
    )

    language: typing.Optional[common.LanguageCode] = Field(
        default=None,
        alias="language",
        title="Language of the resource content",
        description="The base language in which the resource is written.",
    )

    contained: typing.Optional[typing.List[typing.Any]] = Field(
        default=None,
        alias="contained",
        title="Contained, inline Resources",
        description=(
            "These resources do not have an independent existence "
            "apart from the resource that contains them - they cannot "
            "be identified independently, nor can they have their own "
            "independent transaction scope. This is allowed to be a "
            "Parameters resource if and only if it is referenced by a "
            "resource that provides context/meaning."
        ),
    )

    def __init__(self, **data: typing.Any) -> None:
        resource_type = data.pop("resourceType", None)
        expected_resource_type = self.__fields__["resourceType"].default

        errors = []

        if resource_type is not None and resource_type != expected_resource_type:
            error = (
                f"``{self.__class__.__module__}"
                f".{self.__class__.__name__}``"
                f"expects ``.resourceType`` = ``{expected_resource_type}``. "
                f"Received ``{resource_type}`` instead."
            )
            errors.append(
                ErrorWrapper(WrongResourceType(error=error), loc="resourceType")
            )

        if errors:
            raise ValidationError(errors, self.__class__)

        base.Base.__init__(self, **data)

    def __str__(self) -> str:
        return f"{self.resourceType}/{self.id}"
