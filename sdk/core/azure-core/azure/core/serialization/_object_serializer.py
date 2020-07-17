# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import abc
from typing import IO, BinaryIO, Union, Generic, Type, TypeVar


try:
    ABC = abc.ABC
except AttributeError:  # Python 2.7, abc exists, but not ABC
    ABC = abc.ABCMeta("ABC", (object,), {"__slots__": ()})  # type: ignore

ObjectType = TypeVar("ObjectType")


class ObjectSerializer(ABC):

    @abc.abstractmethod
    def serialize(
        self,
        stream,  # type: BinaryIO
        value,  # type: ObjectType
        schema,  # type: Type[ObjectType]
    ):
        # type: (...) -> None
        """Convert the provided value to it's binary representation and write it to the stream.

        :param stream: A stream of bytes or bytes directly
        :type stream: BinaryIO
        :param value: An object to serialize
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def deserialize(
        self,
        data,  # type: Union[bytes, BinaryIO]
        return_Type,  # type: Type[ObjectType]
    ):
        # type: (...) -> ObjectType
        """Read the binary representation into a specific type.

        :param data: A stream of bytes or bytes directly
        :type data: BinaryIO or bytes
        :param return_type: The type of the object to convert to and return
        :returns: An instanciated object
        :rtype: ObjectType
        """
        raise NotImplementedError()