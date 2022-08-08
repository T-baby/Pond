"""
Copyright 2022 Andy Qin. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import time
from typing import Any


class PooledObject(object):
    create_time: float
    last_borrow_time: float
    keeped_object:object

    def __init__(self, obj:Any) -> None:
        self.create_time = time.time()
        self.last_borrow_time = time.time()
        self.keeped_object = obj

    def use(self) -> object:
        return self.keeped_object

    def update_brrow_time(self) -> object:
        self.last_borrow_time = time.time()
        return self
