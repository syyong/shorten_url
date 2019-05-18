import id_encoder

def main():
    for aa in range(200):
        bb = id_encoder.encode(aa)
        cc = id_encoder.enbase(bb)
        dd = id_encoder.debase(cc)
        ee = id_encoder.decode(dd)
        while len(cc) < 7:
            cc = ' ' + cc
        print('%6d %6d %s %6d %6d' % (aa, bb, cc, dd, ee))

if __name__ == '__main__':
    main()