def len2mask(len):
    
    mask = ''
   
    for t in range(4):
        if len > 7:
            mask += '255.'
        else:
            dec = 255 - (2**(8 - len) - 1)
            mask += str(dec) + '.'
        len -= 8
        if len < 0:
           len = 0
    
    return mask[:-1]


rao = input("Enter Netmask number: ")
for len in range(rao, -1, -1- rao):
       
    print '%d = %s' % (len, len2mask(len))
