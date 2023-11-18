#!/usr/bin/env python

import glob

def file_md5_checksum(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()

def main():
    # netCDF file
    files = glob.glob('*.nc')
    for ncf in files:
        prefix = ncf.split('.')[0]
        outf = '{}.md5'.format(prefix)
        with open(outf, 'w') as f:
            f.write(file_md5_checksum(ncf))

    # CSV file
    files = glob.glob('*.csv')
    for ncf in files:
        prefix = ncf.split('.')[0]
        outf = '{}.md5'.format(prefix)
        with open(outf, 'w') as f:
            f.write(file_md5_checksum(ncf))

if __name__ == '__main__':
    main()