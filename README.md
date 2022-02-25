# pmt-voltage-controller

ABANDONED

A simple interface designed to endow PMT drivers with computer control.
Effectively this a USB interface to a single analog and single TTL output.

## Repository

This is an open source hardware project licensed under the CERN Open Hardware Licence Version 2 - Permissive.
Please see the LICENSE file for the complete license.

## PCB

This PCB was designed using KiCAD version 5.
Refer to `pmt-control.pdf` for schematic.
PCB images generated with [tracespace](https://github.com/tracespace/tracespace) follow.

<img src="./pmt-control-.top.svg" width="100%"/>
<img src="./pmt-control-.bottom.svg" width="100%"/>

## Bill of Materials

| reference      | value         | manufacturer  | part number          | vendors |
| :------------- | :------------ | :------------ | :------------------- | :------ |

## Firmware

### Photon Technology 914

PMT voltage controlled by a 0 to +5 V input on the High Voltage control line corresponding to 9 to -1250 V on the PMT.

### Hamamatsu M901X

PMT voltage controlled by a 0 to 900 mV input.

## Changelog
