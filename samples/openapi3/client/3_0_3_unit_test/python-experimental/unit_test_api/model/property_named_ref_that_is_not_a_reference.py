# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401
import uuid  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class PropertyNamedRefThatIsNotAReference(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            ref = schemas.StrSchema
            locals()["$ref"] = ref
            del locals()['ref']
            """
            NOTE:
            openapi/json-schema allows properties to have invalid python names
            The above local assignment allows the code to keep those invalid python names
            This allows properties to have names like 'some-name', '1 bad name'
            Properties with these names are omitted from the __new__ + _from_openapi_data signatures
            - __new__ these properties can be passed in as **kwargs
            - _from_openapi_data these are passed in in a dict in the first positional argument *arg
            If the property is required and was not passed in, an exception will be thrown
            """
        additional_properties = schemas.AnyTypeSchema
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'PropertyNamedRefThatIsNotAReference':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )