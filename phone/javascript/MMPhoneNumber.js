// Myanmar Phone Number validation & normalization for ES6 
//
// Copyright 2016 Melomap (www.melomap.com)
// Copyright 2018 Thura Hlaing (trhura@gmail.com)
// Copyright 2018 Aye Chan Mon (polestar.mon20@gmail.com)
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

const mobileCode = "(0?9)";
const countryCode = "(\\+?95)";
const ooredooNumber = "(?:9(?:7|6|5)\\d{7})$";
const telenorNumber = "(?:7(?:9|8|7|6)\\d{7})$";
const mptNumber ="(?:5\\d{6}|4\\d{7,8}|2\\d{6,8}|3\\d{7,8}|6\\d{6}|8\\d{6}|7\\d{7}|9(?:0|1|9)\\d{5,6})$";
const allOperators = `(${ooredooNumber}|${telenorNumber}|${mptNumber})$`;
const mmNumber = `^${countryCode}?${mobileCode}?${allOperators}`;

module.exports = class MMPhoneNumber {
  static isValid(number) {
    let phone = number.toString();
    return phone.match(mmNumber) != null;
  }

  static normalize(number) {
    let phone = number.toString();
    let matches = phone.match(mmNumber);

    if (matches == null) {
      throw new TypeError(`${number} is not a valid phone number.`);
    }

    return parseInt("959" + matches[3]);
  }
}