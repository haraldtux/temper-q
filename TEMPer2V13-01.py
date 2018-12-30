#!/usr/bin/python3

'''
   ^H> HucDuino 16-12-2018

   USB IDs 413d:2107 , TEMPer2V1.3

       https://github.com/marook/temper-q
       https://github.com/haraldtux/temper-q

       Requirements
       You need hidaip wrappers for python. Install on debian for example via
       $ apt install python3-hidapi
'''       
       
import hidapi

def main():
    for dev_info in hidapi.enumerate(vendor_id=0x413d, product_id=0x2107):
        if(dev_info.interface_number != 1):
            continue
        dev = hidapi.Device(info=dev_info)
        dev.write(b'\x01\x80\x33\x01\x00\x00\x00\x00')
        temp_raw = dev.read(8)
        dev.close()
        print(dump_to_temperature(temp_raw[2:4]))
        exit(0)
    print('No temper thermometer found')
    exit(1)

def dump_to_temperature(bytes):
    temp = (bytes[0] <<8) + bytes[1]
    return float(temp) / 100 -4

if __name__ == '__main__':
    main()
