#
#
#
#
#



class reverse:
    def bitreverse(self,onebyte):
        tmp = 0
        for i in range(8):
            tmp = (tmp << 1) | (onebyte & 0x01)
            onebyte = onebyte >> 1
        return tmp

    def bytereverse(self,listbuffer):
        listbuffer.reverse()
        return listbuffer

    def reverse(self,listbuffer,turnbit,turnbyte):
        if turnbyte == True:
            listbuffer.reverse()
        if turnbit == True:
            for i in range(len(listbuffer)):
                listbuffer[i] = self.bitreverse(listbuffer[i])
        return listbuffer

class hexstr:
    def hex2str(self,hexbuffer):
        ans = str()
        for listn in hexbuffer:
            lists = list()
            for listm in listn:
                lists.append(hex(listm))
            if len(lists)!=0:
                ans += ','.join(lists)
                ans += ";\r"
        return ans

    def str2hex(self, strbuffer):
        hexstrs = strbuffer.split(';')
        hexl = list()
        for stri in hexstrs:
            hexs = stri.strip().strip('\r').strip().strip(';').split(',')
            hexli = list()
            for strn in hexs:
                strn = strn.strip()
                if strn != '':
                    hexli.append(int(strn,16))
            if len(hexli)!=0:
                hexl.append(hexli)
        return hexl
